from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import logging
import sys

# Configure logging to output to stdout (visible in docker logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override default logging to use our logger
        logger.info(f"{self.client_address[0]} - {format % args}")
    
    def do_GET(self):
       if self.path == '/':
           self.path = '/index.html'
       
       logger.info(f"GET request for: {self.path}")
       
       try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
           logger.info(f"Successfully served: {self.path}")
       except FileNotFoundError:
           file_to_open = "File not found"
           self.send_response(404)
           logger.warning(f"File not found: {self.path}")
       except Exception as e:
           file_to_open = "Error reading file"
           self.send_response(500)
           logger.error(f"Error serving {self.path}: {str(e)}")
       
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

def run(server_class=HTTPServer, handler_class=Handler , port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f'Starting server on port {port}...')
    logger.info(f'Server address: {server_address}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info('Server interrupted by user')
    finally:
        logger.info('Server shutdown')

if __name__ == '__main__':
    run()