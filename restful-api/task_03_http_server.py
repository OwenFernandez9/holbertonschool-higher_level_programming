#!/usr/bin/python3
import http.server
import json


def Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.response(404, 'Not Found')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

    



