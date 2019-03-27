import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing the request line
        global le, bases_operations
        termcolor.cprint(self.requestline, 'green')
        path = self.path

        if self.path == '/':
            with open("main.html", "r") as f:
                contents = f.read()
            resp = 200
        elif path[:4] == '/get':
            resp = 200
            msg = path.split('&')
            my_seq = msg[0].split('=')[1]
            if my_seq.upper().strip('ACGT') == '':
                my_seq = Seq(my_seq)

                # i create new dics for the options
                count = {'base=A': ('Count A: ' + str(my_seq.count('A'))),
                         'base=C': ('Count C: ' + str(my_seq.count('C'))),
                         'base=G': ('Count G: ' + str(my_seq.count('G'))),
                         'base=T': ('Count T: ' + str(my_seq.count('T')))}
                perc = {'base=A': ('Percentage A: ' + str(my_seq.perc('A')) + '%'),
                        'base=C': ('Percentage C: ' + str(my_seq.perc('C')) + '%'),
                        'base=T': ('Percentage T: ' + str(my_seq.perc('T')) + '%'),
                        'base=G': ('Percentage G: ' + str(my_seq.perc('G')) + '%')}

                # now, i create another dic to place both previous dics
                pos_ops = {'count': count, 'perc': perc}

                # when you write no message you get a len of 3, so you have to star from there

                if len(msg) == 3:
                    # now a create an empty list with the length, so when i don choose it i get no answer from it
                    le = ''
                    operation = msg[1].split('=')[1]
                    bases = msg[2]
                    # i try to find things inside the dics with the function key, that introduces inside the dics
                    if bases in pos_ops[operation]["base=" + bases]:
                        bases_operations = pos_ops[operation]["base=" + bases]

                elif len(msg) == 4:  # that means that i actually wrote a message
                    le = 'Length: ' + str(my_seq.len())
                    operation = msg[3].split('=')[1]
                    bases = msg[2].split('=')[1]
                    if bases in pos_ops[operation]["base=" + bases]:
                        bases_operations = pos_ops[operation]["base=" + bases]

                fs = open('response.html', 'w')
                data = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RESPONSE</title>
</head>
<body style="background-color: yellow;">
    <h1>RESULTS:</h1>
    <p>msg</p>
    <a href="/">[Main Page]</a>

</body>
</html>""".format(my_seq.strbases.upper(), le, bases_operations)
                fs.write(data)
                with open('response.html', 'r') as f:
                    contents = f.read()
            else:
                with open('seqerror.html', 'r') as f:
                    contents = f.read()
        else:
            resp = 404
            with open("error.html", "r") as f:
                contents = f.read()

        self.send_response(resp)
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
