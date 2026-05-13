from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
       if self.path == '/':
           self.path = '/index.html'
       try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
       except:
           file_to_open = "File not found"
           self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

def run(server_class=HTTPServer, handler_class=Handler , port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()