from http.server import BaseHTTPRequestHandler
import json
import re

from services import get_page, get_sub_pages, get_breadcrumbs


class PageDetailView(BaseHTTPRequestHandler):
    def do_GET(self):
        path = re.match(r'^/api/v1/page/(\d+)$', self.path)
        if path:
            try:
                page_id = int(path.group(1))  
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                                
                page = get_page(page_id)
                
                sub_pages = get_sub_pages(page_id)
                
                breadcrumbs = get_breadcrumbs(sub_pages)
                
                context = {
                    'pageId': page.id,    
                    'title': page.title,
                    'subPages': sub_pages,
                    'breadcrumbs': breadcrumbs,
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