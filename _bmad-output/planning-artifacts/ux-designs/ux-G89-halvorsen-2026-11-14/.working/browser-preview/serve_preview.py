#!/usr/bin/env python3
"""Serve this isolated UX preview directory on the local machine."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    try:
        server = ThreadingHTTPServer(("127.0.0.1", 8765), handler)
    except OSError as error:
        if error.errno not in (48, 98):
            raise
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    print(f"http://127.0.0.1:{server.server_port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
