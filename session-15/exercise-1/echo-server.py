import http.server
import socketserver
import termcolor

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            with open('index.html', 'r') as file:
                file =
                    content = str(content)



        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server stopped")
