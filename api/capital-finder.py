from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url_components = parse.urlsplit(self.path)
    query = parse.parse_qsl(url_components.query)

    if query:
      if query[0][0] == 'country':
        country = query[0][1].lower()
        url = f'https://restcountries.com/v3.1/name/{country}'
        data = requests.get(url).json()
        capital = data[0]['capital'][0]
        message = f'The capital of {query[0][1]} is {capital}'
      elif query[0][0] == 'capital':
        capital = query[0][1].lower()
        url = f'https://restcountries.com/v3.1/capital/{capital}'
        data = requests.get(url).json()
        country = data[0]['name']['common']
        message = f'{query[0][1]} is the capital of {country}'
    else:
      message = "Please enter a valid country or capital query"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    self.wfile.write(message.encode())
    return
