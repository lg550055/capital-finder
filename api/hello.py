from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests


class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    # url_components = parse.urlsplit(self.path)
    # query = parse.parse_qsl(url_components)
    # dic = dict(query)
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "Howdy"
    self.wfile.write(message.encode())
    return