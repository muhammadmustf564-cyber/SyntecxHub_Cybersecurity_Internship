from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class TestServer(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        parameters = parse_qs(parsed_url.query)

        user_id = parameters.get("id", [""])[0]

        if "'" in user_id or "OR" in user_id.upper() or "AND" in user_id.upper():
            response = """
            <html>
            <body>
            <h1>Database Error</h1>
            <p>You have an error in your SQL syntax.</p>
            </body>
            </html>
            """
        else:
            response = f"""
            <html>
            <body>
            <h1>Test Application</h1>
            <p>User ID: {user_id}</p>
            </body>
            </html>
            """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())


server = HTTPServer(("127.0.0.1", 8000), TestServer)

print("Test server running at http://127.0.0.1:8000")
print("Press CTRL+C to stop.")

server.serve_forever()