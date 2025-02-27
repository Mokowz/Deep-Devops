from prometheus_client import start_http_server, Summary, Histogram, Counter
import random, time, http.server

TOTAL = Counter('hello_worlds_total', 'Total Number of Hello Worlds called')
LATENCY = Histogram('hello_world_latency_seconds', 'Time for a request Hello World')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        TOTAL.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
