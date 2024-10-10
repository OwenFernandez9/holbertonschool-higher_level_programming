#!/usr/bin/python3
import http.server
import json


class Server(http.server.BaseHTTPRequestHandler):
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
            self.response_send(404)
            self.wfile.write(b'Endpoint not found')

def run(server_class=http.server.HTTPServer, handler_class=Server):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
