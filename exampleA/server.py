from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Client!")

def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()