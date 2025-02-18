#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='text/plain'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self._set_headers('application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b"OK")
        else:
            self.send_error(404, "Endpoint not found")


def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
