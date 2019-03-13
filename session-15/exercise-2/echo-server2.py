import http.server
import socketserver
import termcolor

PORT = 8009


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print('Path: ' + self.path)
        path = self.path
        i = path.find('=')

        if self.path == '/':
            with open("capital.html", "r") as f:
                contents = f.read()
            print('Path: ' + self.path)
            path = self.path
            i = path.find('=')
        else:
            with open("error.html", "r") as f:
                contents = f.read()
        if i != -1:
            if path.find("&") != -1:
                ii = path.find("&")
                msg = path[i + 1: ii]
                msg = msg.replace("+", " ")
                msg = msg.upper()
            else:
                msg = path[i + 1:]
            with open('response.html', 'r') as f:
                contents = f.read()
            contents = contents.replace('msg', msg)


        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))
        return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server stopped")
