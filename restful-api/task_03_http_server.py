#!/usr/bin/python3
"""
Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A class SimpleHTTPRequestHandler.
    """

    def do_GET(self):
        """
        Handle GET requests.
        """
        try:
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Hello, this is a simple API!')
            elif self.path == '/data':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                dataset = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(json.dumps(dataset).encode('UTF-8'))
            elif self.path == '/status':
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'OK')
            elif self.path == '/info':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                info = {"version": "1.0", "description": "A simple API built with http.server"}
                self.wfile.write(json.dumps(info).encode('UTF-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'404 Not Found')
        except Exception as e:
            logging.error(f"Error handling GET request: {e}")
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Internal Server Error')

    def do_POST(self):
        """
        Handle POST requests.
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"Received POST data: {post_data}")

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'POST request received')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    logging.info(f"Serving at port {server_address[1]}")
    httpd.serve_forever()

