import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8009


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print('Path: ' + self.path)
        path = self.path

        if self.path == '/':
            with open("main.html", "r") as f:
                contents = f.read()
            print('Path: ' + self.path)
            resp = 200
            path = self.path
        elif path[:4] == '/myserver':
            msg =path.split('&')
            my_seq = msg[0].split('=')[1]
            resp = 200
            if my_seq.upper().strip('ACGT') == '':
                my_seq = Seq(my_seq)

                # i create new dics for the options
                count = {'base=A': ('Count A: ' + my_seq.count('A')), 'base=C': ('Count C: ' + my_seq.count('C')), 'base=G': ('Count G: ' + my_seq.count('G')), 'base=T': ('Count T: ' + my_seq.count('T'))}
                perc = {'base=A': ('Percentage of A: ' + my_seq.perc('A') + '%'), 'base=C': ('Percentage of C: ' + my_seq.perc('C') + '%'), 'base=T': ('Percentage of T: ' + my_seq.perc('T') + '%'), 'base=G': ('Percentage of G: ' + my_seq.perc('G') + '%')}

                # now, i create another dic to place both previous dics
                pos_ops = {'count': count, 'perc': perc}

                # when you write no message you get a len of 3, so you have to star from there
                if len(msg) == 3:
                    # now a create an empty list with the length, so when i don choose it i get no answer from it
                    l = ''
                    operation = msg[1].split('=')[1]
                    bases = msg[2]
                    # i try to find things inside the dics with the function key, that introduces inside the dics
                    if bases in pos_ops[operation].keys():
                        bases_operation = pos_ops[operation][bases]

                elif len(msg) == 4: # that means that i actually wrote a message
                    l = 'Length: ' + str(my_seq.len())
                    operation = msg[2].split('=')[1]
                    bases = msg[3]
                    if bases in pos_ops[operation].keys():
                        bases_operations = pos_ops[operation][bases]
                    contents = contents.replace('msg', msg)
                else:
                    with open ('seqerror.html', 'r') as f:
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
