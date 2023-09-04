import socketserver

from views import PageDetailView

PORT = 8000

try:
    with socketserver.TCPServer(("", PORT), PageDetailView) as httpd:
        httpd.timeout = 10
        print(
            f"""
            Serving at port http://localhost:{PORT} 
            Press Ctrl+C to quit
            """
        )
        httpd.serve_forever()
except OSError as e:
    if e.errno == 48:
        print(f"Port {PORT} is already in use. Please choose a different port.")
    else:
        print(f"An error occurred: {e}")
