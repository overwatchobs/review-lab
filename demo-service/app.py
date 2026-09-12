from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"running","service":"demo-service"}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f'Starting demo server on {port}...')
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()
