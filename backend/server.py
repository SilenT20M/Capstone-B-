
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class CapstoneHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            response = {
                "message": "Welcome to the Costco Smart Shopping Platform API",
                "status": "running"
            }
            self.send_response(200)

        elif self.path == "/api/health":
            response = {
                "status": "healthy"
            }
            self.send_response(200)

        else:
            response = {
                "error": "Endpoint not found"
            }
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CapstoneHandler)
    print("Capstone B backend running at http://localhost:8000")
    server.serve_forever()
