import http.server
import socketserver

PORT = 8009


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)

        content = ''
        if self.path == '/':
            with open('index.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        else:
            with open('error.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header("Content-Length", len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
