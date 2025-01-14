import http.server
import socketserver


def make_app(PORT, DIRECTORY):
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, directory=DIRECTORY, **kwargs):
            super().__init__(*args, directory, **kwargs)

    # Start the server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server...")
            httpd.shutdown()
