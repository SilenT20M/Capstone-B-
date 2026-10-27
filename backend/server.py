
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "capstone_b.db"


class CapstoneHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_json(200, {
                "message": "Welcome to the Costco Smart Shopping Platform API",
                "status": "running"
            })

        elif self.path == "/api/health":
            self.send_json(200, {"status": "healthy"})

        elif self.path == "/api/products":
            try:
                with sqlite3.connect(DATABASE_PATH) as connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        "SELECT * FROM Product"
                    ).fetchall()

                products = [dict(row) for row in rows]
                self.send_json(200, {
                    "count": len(products),
                    "products": products
                })

            except sqlite3.Error as error:
                self.send_json(500, {
                    "error": "Database query failed",
                    "details": str(error)
                })

        elif self.path == "/api/categories":
            try:
                with sqlite3.connect(DATABASE_PATH) as connection:
                    connection.row_factory = sqlite3.Row
                    rows = connection.execute(
                        "SELECT * FROM Category"
                    ).fetchall()

                categories = [dict(row) for row in rows]
                self.send_json(200, {
                    "count": len(categories),
                    "categories": categories
                })

            except sqlite3.Error as error:
                self.send_json(500, {
                    "error": "Database query failed",
                    "details": str(error)
                })

        else:
            self.send_json(404, {"error": "Endpoint not found"})


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CapstoneHandler)
    print("Capstone B backend running at http://localhost:8000", flush=True)
    server.serve_forever()
