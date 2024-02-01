#!/usr/bin/env python
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"<html><body><h1>Hello, FastCGI World!</h1></body></html>"]

if __name__ == '__main__':
    WSGIServer(app).run()