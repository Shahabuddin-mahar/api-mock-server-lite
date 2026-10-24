#!/usr/bin/env python3
"""
API Mock Server Lite
Zero-dependency lightweight mock HTTP REST API server
"""
import http.server, socketserver, json, sys

PORT = 8080

MOCK_DATABASE = {
    "/api/users": [
        {"id": 1, "name": "Sarah Connor", "role": "Lead Architect"},
        {"id": 2, "name": "John Doe", "role": "Frontend Developer"}
    ],
    "/api/products": [
        {"id": 101, "title": "Micro-SaaS Starter Kit", "price": 19.99},
        {"id": 102, "title": "Lead Scraper Pro", "price": 49.00}
    ]
}

class MockHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in MOCK_DATABASE:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(MOCK_DATABASE[self.path]).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    print(f"[*] API Mock Server running at http://localhost:{PORT}")
    print("    Available endpoints: /api/users, /api/products")
    with socketserver.TCPServer(("", PORT), MockHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
