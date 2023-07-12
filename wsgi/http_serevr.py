#python -m http.server [port]
#python -m http.server [post] --bind [host] or -b
#python -m htt.server 9999 -b 128.152.124.12
from http.server import HTTPServer, BaseHTTPRequestHandler

host = "127.0.0.1"
port = 5000


class server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("get","utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes("post","utf-8"))


server = HTTPServer((host, port),server)
print("server is running ...")
server.serve_forever()
print("server break")
server.server_close()


