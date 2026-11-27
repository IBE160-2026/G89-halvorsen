#!/usr/bin/env python3
"""Local structural-signal feasibility only; emits no course text or screenshots.

Operator presence is not visibility, importance, completeness or factual support.
No OCR, shape reconstruction, significance thresholds or application detector.
"""
from __future__ import annotations

import collections
import hashlib
import importlib.metadata
import json
import logging
import platform
import time
import unicodedata
import warnings
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, DictionaryObject, NameObject

ROOT = Path('/private/tmp/ai-study-buddy-coverage-probe')
INPUT = Path.cwd() / 'test-data/pdfs'
PAINT = {'S','s','f','F','f*','B','B*','b','b*'}
KNOWN = set(('b b* B B* BDC BI BMC BT BX c cm CS cs d d0 d1 Do DP EI EMC ET EX f F f* G g gs h i ID j J K k l m M MP n q Q re rg RG ri s S SC SCN sc scn sh T* Tc Td TD Tf Tj TJ TL Tm Tr Ts Tw Tz v w W W* y \' "').split()) | {'INLINE IMAGE'}


def hash_value(value):
    if isinstance(value, str): value = value.encode('utf-8', 'replace')
    return hashlib.sha256(value).hexdigest()


def fingerprint(text):
    normalized = unicodedata.normalize('NFC', text)
    return hash_value(''.join(c for c in normalized if not c.isspace()))


def op_name(raw):
    return raw.decode('latin1') if isinstance(raw, bytes) else str(raw)


def error_info(exc):
    return {'type':type(exc).__name__, 'message_sha256':hash_value(str(exc))}


def counter_output(counter):
    known = {name:count for name,count in sorted(counter.items()) if name in KNOWN}
    unknown = [{'operator_sha256':hash_value(name),'operator_bytes':len(name.encode('latin1','replace')),'count':count} for name,count in sorted(counter.items()) if name not in KNOWN]
    return {'known':known, 'unknown':unknown}


class Capture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.context = {}
        self.events = []

    def emit(self, record):
        self.events.append({**self.context,'logger':record.name,'level':record.levelname,'message_sha256':hash_value(record.getMessage())})


def obj(value):
    return value.get_object() if value is not None and hasattr(value,'get_object') else value


def identity(value):
    reference = getattr(value, 'indirect_reference', None)
    if reference is not None: return (reference.idnum, reference.generation)
    if hasattr(value,'idnum'): return (value.idnum,value.generation)
    return id(value)


def resource_inventory(resources):
    counts=collections.Counter()
    visited=set()
    def visit(res):
        res=obj(res) or {}
        xobjects=obj(res.get('/XObject')) or {}
        for value in xobjects.values():
            value=obj(value)
            key=identity(value)
            if key in visited: continue
            visited.add(key)
            subtype=str(value.get('/Subtype',''))
            if subtype=='/Image': counts['image_xobjects']+=1
            elif subtype=='/Form':
                counts['form_xobjects']+=1
                visit(value.get('/Resources'))
            else: counts['other_xobjects']+=1
    visit(resources)
    return dict(counts)


def walk_invoked(contents, resources, reader):
    """Inspect syntax and follow invoked Forms; this does not emulate rendering."""
    operators=collections.Counter()
    signals=collections.Counter()
    render_modes=collections.Counter()
    errors=[]
    def visit(stream, res, ancestors, depth):
        if depth>20:
            signals['form_depth_limit']+=1
            return
        res=obj(res) or {}
        try:
            operations=ContentStream(stream,reader).operations if stream is not None else []
        except Exception as exc:
            errors.append({'operation':'parse_content_stream',**error_info(exc)})
            return
        for operands,raw_operator in operations:
            operator=op_name(raw_operator)
            operators[operator]+=1
            if operator in PAINT: signals['path_paint']+=1
            elif operator=='sh': signals['shading_paint']+=1
            elif operator=='INLINE IMAGE': signals['inline_image']+=1
            elif operator not in KNOWN: signals['unknown_operator']+=1
            if operator=='Tr':
                try: render_modes[str(int(operands[0]))]+=1
                except Exception: signals['invalid_text_render_mode']+=1
            if operator=='Tf':
                try:
                    fonts=obj(res.get('/Font')) or {}
                    font=obj(fonts.get(operands[0]))
                    if font is None: signals['unresolved_font_selection']+=1
                    elif str(font.get('/Subtype',''))=='/Type3': signals['type3_font_selected']+=1
                except Exception as exc:
                    errors.append({'operation':'resolve_font',**error_info(exc)})
            if operator!='Do': continue
            signals['Do_invocations']+=1
            try:
                objects=obj(res.get('/XObject')) or {}
                target=obj(objects.get(operands[0])) if operands else None
                if target is None:
                    signals['unresolved_Do']+=1
                    continue
                subtype=str(target.get('/Subtype',''))
                if subtype=='/Image': signals['image_Do']+=1
                elif subtype=='/Form':
                    signals['form_Do']+=1
                    key=identity(target)
                    if key in ancestors:
                        signals['recursive_form_cycle']+=1
                        continue
                    child_resources=target.get('/Resources')
                    if child_resources is None: child_resources=res
                    visit(target,child_resources,ancestors|{key},depth+1)
                else: signals['other_Do_subtype']+=1
            except Exception as exc:
                errors.append({'operation':'resolve_Do',**error_info(exc)})
    visit(contents,resources,set(),0)
    return {'operators':counter_output(operators),'signals':dict(signals),'text_render_modes_invoked':dict(render_modes),'errors':errors}


def inspect_pdf(path, label):
    start=time.perf_counter()
    capture=Capture()
    logger=logging.getLogger('pypdf')
    old_handlers,old_propagate=logger.handlers[:],logger.propagate
    logger.handlers,logger.propagate=[capture],False
    document={'document':label,'file_bytes':path.stat().st_size,'source_sha256':hash_value(path.read_bytes()),'pages':[],'errors':[]}
    reader=None
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        try:
            capture.context={'physical_page':None,'operation':'open'}
            reader=PdfReader(path,strict=False)
            document['encrypted']=bool(reader.is_encrypted)
            if reader.is_encrypted:
                document['rejected_encrypted_without_decryption']=True
            else:
                document['physical_page_count']=len(reader.pages)
                for number,page in enumerate(reader.pages,1):
                    record={'physical_page':number,'errors':[]}
                    visitor=collections.Counter()
                    def before(operator, operands, cm, tm): visitor[op_name(operator)]+=1
                    capture.context={'physical_page':number,'operation':'plain_with_visitor'}
                    plain=''
                    try: plain=page.extract_text(visitor_operand_before=before) or ''
                    except Exception as exc: record['errors'].append({'operation':'plain',**error_info(exc)})
                    capture.context={'physical_page':number,'operation':'layout'}
                    layout=''
                    try: layout=page.extract_text(extraction_mode='layout') or ''
                    except Exception as exc: record['errors'].append({'operation':'layout',**error_info(exc)})
                    record['text']={'plain_chars':len(plain),'layout_chars':len(layout),'plain_nonempty':bool(plain.strip()),'layout_nonempty':bool(layout.strip()),'plain_replacement_chars':plain.count('\ufffd'),'layout_replacement_chars':layout.count('\ufffd'),'plain_order_sha256':fingerprint(plain),'layout_order_sha256':fingerprint(layout),'same_nfc_nonwhitespace_order':fingerprint(plain)==fingerprint(layout)}
                    record['visitor']=counter_output(visitor)
                    record['visitor_requested_paints']={name:visitor.get(name,0) for name in sorted(PAINT|{'Do','INLINE IMAGE','sh'})}
                    capture.context={'physical_page':number,'operation':'invoked_stream_walk'}
                    try:
                        resources=page.get('/Resources')
                        record['invoked_walk']=walk_invoked(page.get('/Contents'),resources,reader)
                        record['declared_resource_inventory']=resource_inventory(resources)
                    except Exception as exc: record['errors'].append({'operation':'content_walk',**error_info(exc)})
                    try: record['annotations']=len(obj(page.get('/Annots')) or [])
                    except Exception as exc: record['errors'].append({'operation':'annotations',**error_info(exc)})
                    record['diagnostic_count']=sum(event.get('physical_page')==number for event in capture.events)
                    document['pages'].append(record)
                    # Drop course text before the next page; no raw strings enter output.
                    del plain,layout
        except Exception as exc: document['errors'].append(error_info(exc))
        finally:
            if reader is not None:
                try: reader.close()
                except Exception as exc: document['errors'].append({'operation':'close',**error_info(exc)})
            logger.handlers,logger.propagate=old_handlers,old_propagate
        document['python_warnings']=[{'category':warning.category.__name__,'message_sha256':hash_value(str(warning.message))} for warning in caught]
    document['diagnostics']=capture.events
    document['elapsed_seconds']=time.perf_counter()-start
    return document


def create_synthetic():
    from PIL import Image,ImageDraw
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    folder=ROOT/'synthetic'
    folder.mkdir(exist_ok=True)
    raster=Image.new('RGB',(240,100),'white')
    ImageDraw.Draw(raster).text((10,35),'OWNED RASTER FIXTURE',fill='black')
    initial=folder/'base.pdf'
    c=canvas.Canvas(str(initial),pagesize=(420,300),invariant=1)
    c.drawString(30,250,'Plain native text')
    c.showPage()
    c.showPage()
    c.drawImage(ImageReader(raster),30,100,width=240,height=100)
    c.showPage()
    c.drawString(30,250,'Native text plus raster')
    c.drawImage(ImageReader(raster),30,100,width=240,height=100)
    c.showPage()
    c.drawString(30,250,'Native text plus vector')
    c.line(30,100,300,100)
    c.rect(30,140,80,40,stroke=1,fill=1)
    c.showPage()
    c.beginForm('inner',0,0,420,300)
    c.drawString(30,250,'Native text inside inner Form')
    c.line(30,100,300,100)
    c.endForm()
    c.beginForm('outer',0,0,420,300)
    c.doForm('inner')
    c.endForm()
    c.doForm('outer')
    c.showPage()
    c.drawString(30,250,'Plain text with unused image resource')
    c.showPage()
    c.drawString(30,250,'Plain text plus unknown operator')
    c._code.append('1 2 ZZ')
    c.showPage()
    c.save()
    # Attach an image resource to page7, without a corresponding Do invocation.
    reader=PdfReader(initial)
    writer=PdfWriter()
    writer.append(reader)
    image_resources=obj(reader.pages[2]['/Resources']['/XObject'])
    image=next(obj(value) for value in image_resources.values() if str(obj(value).get('/Subtype'))=='/Image')
    page7=writer.pages[6]
    resources=obj(page7['/Resources'])
    xobjects=DictionaryObject()
    xobjects[NameObject('/UnusedProbeImage')]=writer._add_object(image.clone(writer))
    resources[NameObject('/XObject')]=xobjects
    output=folder/'structural-fixtures.pdf'
    with output.open('wb') as stream: writer.write(stream)
    writer.close()
    reader.close()
    return output


def verify_synthetic(document):
    pages={page['physical_page']:page for page in document['pages']}
    signals=lambda number:pages[number]['invoked_walk']['signals']
    graphics=lambda number:sum(signals(number).get(key,0) for key in ('image_Do','inline_image','path_paint','shading_paint','form_Do'))
    tests={
        'physical_slots_preserved':document.get('physical_page_count')==8 and list(pages)==list(range(1,9)),
        'plain_text_has_no_nontext_paint_signal':pages[1]['text']['plain_nonempty'] and graphics(1)==0,
        'truly_blank_no_text_or_graphic_signal':not pages[2]['text']['plain_nonempty'] and graphics(2)==0,
        'image_only_empty_text_but_invoked_image':not pages[3]['text']['plain_nonempty'] and signals(3).get('image_Do',0)==1,
        'text_raster_both_detected':pages[4]['text']['plain_nonempty'] and signals(4).get('image_Do',0)==1,
        'text_vector_path_paints_detected':pages[5]['text']['plain_nonempty'] and signals(5).get('path_paint',0)>=2,
        'nested_forms_followed_to_inner_path_paint':signals(6).get('form_Do',0)==2 and signals(6).get('path_paint',0)>=1,
        'unused_declared_image_not_invoked':pages[7]['declared_resource_inventory'].get('image_xobjects',0)==1 and signals(7).get('Do_invocations',0)==0 and graphics(7)==0,
        'unknown_operator_signalled':signals(8).get('unknown_operator',0)==1,
        'visitor_sees_nested_form_path_paint':pages[6]['visitor_requested_paints'].get('S',0)>=1,
    }
    return {'checks':tests,'passed':sum(tests.values()),'total':len(tests),'failed':[name for name,passed in tests.items() if not passed]}


def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    documents=[inspect_pdf(INPUT/(label+'.pdf'),label) for label in ('T1','T2','T3')]
    synthetic=inspect_pdf(create_synthetic(),'owned_synthetic')
    checks=verify_synthetic(synthetic)
    output={
        'scope':'Local syntax/callback structural-signal feasibility; no detector, significance classification, OCR or semantic validation',
        'python':platform.python_version(),
        'pypdf':importlib.metadata.version('pypdf'),
        'documents':documents,
        'owned_synthetic':synthetic,
        'synthetic_checks':checks,
        'limitations':[
            'Painting operators can be clipped, off-page, invisible, decorative or in optional content; this probe does not decide visibility or importance.',
            'The pypdf visitor has no explicit nested-resource-scope argument. A separate syntax walk resolves invoked XObjects with Form resources; neither path is a PDF renderer.',
            'The walk follows invoked Forms only, with cycle detection/depth20; unresolved names, recursion, parse errors and unknown operators are uncertainty signals.',
            'Annotation count does not inspect or execute annotation appearance streams; annotations remain uncertain.',
            'Type3 font selection is flagged; glyph CharProcs, patterns and transparency/soft-mask resources are not comprehensively interpreted.',
            'Plain/layout fingerprints compare NFC nonwhitespace character sequence only. Equality does not prove correct order; difference alone does not prove one mode wrong.',
            'Absence of these signals is not proof of complete extraction or PDF semantic equivalence. All proposed acceptance criteria remain subject to implementation validation.',
        ]
    }
    (ROOT/'summary.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'synthetic_checks':checks,'documents':[{'document':d['document'],'pages':d.get('physical_page_count'),'errors':len(d['errors']),'diagnostics':len(d['diagnostics']),'order_differences':[p['physical_page'] for p in d['pages'] if not p['text']['same_nfc_nonwhitespace_order']],'graphic_signal_pages':[p['physical_page'] for p in d['pages'] if any(p.get('invoked_walk',{}).get('signals',{}).get(k,0) for k in ('image_Do','inline_image','path_paint','form_Do','shading_paint'))]} for d in documents]},indent=2))
    return int(bool(checks['failed']))


if __name__=='__main__':
    raise SystemExit(main())
