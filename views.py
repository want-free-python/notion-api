from http.server import BaseHTTPRequestHandler
import json


class PageDetailView(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/v1/page/{id}}':
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # TODO: Add Service Layer
                context = {
                    'data': "data",                    
                }
                
                json_data = json.dumps(context)
                self.wfile.write(json_data.encode())
                
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                context = {
                    'message': e,
                }
                json_data = json.dumps(context)
                self.wfile.write(json_data.encode())