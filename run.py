#!/usr/bin/env python3

# Python 3 server example

import os
import time
import emoji
import argparse

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# -----------------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-l", "--local", help="Respond to localhost only", action="store_true")

args = parser.parse_args()

# -----------------------------------------------------------------------------

if args.verbose:
    print("verbosity turned on")

if args.local:
    print("locahost turned on")
    hostName = "localhost"
else:
    hostName = "0.0.0.0"

serverPort = 8080

page = """
<html>
  <head>
    <title>A Simple HTTP Server</title>
  </head>
  <body>
    <p>This is an example web server. - :thumbs_up:</p>
    <p>Request: {}</p>
  </body>
</html>
"""

# -----------------------------------------------------------------------------

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page.format(self.path), "utf-8"))

        print(f"      Requestline: {self.requestline}")

        url = urlparse(self.path)

        print(f"         URL/path: {url}")
        print(f"       Query path: {url.path}")
        print(f"  Query component: {url.query}")
        print(f"       Query args: {parse_qs(url.query)}")
        print(f"   Query fragment: {url.fragment}")
        params = parse_qs(url.query)
        print(f"           Params: {params}")
        print(emoji.emojize(':thumbs_up:'))

# -----------------------------------------------------------------------------

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

# -----------------------------------------------------------------------------
