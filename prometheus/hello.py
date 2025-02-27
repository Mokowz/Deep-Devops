import http.server
from prometheus_client import start_http_server, Counter
import random


REQUESTS = Counter('hello_worlds_total', 'Hello Worlds Requested')
EXCEPTIONS = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')
SALES = Counter('hello_world_sales_euro_total', 'Euros made serving Hello World')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        euros = random.random()
        SALES.inc(euros)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} euros.".format(euros).encode())


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
