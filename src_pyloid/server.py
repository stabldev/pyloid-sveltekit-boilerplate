import http.server
import socketserver


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # Handle the request after rewriting
        super().do_GET()


def make_app(PORT, DIRECTORY):
    # Custom factory to pass the directory to the handler
    def handler_factory(*args, **kwargs):
        return CustomHandler(*args, directory=DIRECTORY, **kwargs)

    # Start the server
    with socketserver.TCPServer(("", PORT), handler_factory) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server...")
            httpd.shutdown()
