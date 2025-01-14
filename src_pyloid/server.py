import http.server
import socketserver


def make_app(PORT, DIRECTORY):
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with open("test.txt", "w") as f:
        f.write("hello")

    # Start the server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()
