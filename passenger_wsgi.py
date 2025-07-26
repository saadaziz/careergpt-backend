import sys, os, imp
from fastapi import Request
from starlette.responses import Response
from starlette.testclient import TestClient

# Add current folder to sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Load FastAPI app from app/main.py
wsgi = imp.load_source('wsgi', 'app/main.py')
fastapi_app = wsgi.app

# Use Starlette TestClient to bridge ASGI → WSGI
client = TestClient(fastapi_app)

def application(environ, start_response):
    # Build request from WSGI environ
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    query = environ['QUERY_STRING']
    body = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0) or 0))

    # Make request to FastAPI via TestClient
    response = client.request(method, path + ("?" + query if query else ""), data=body)

    # Send response back to WSGI
    status = f"{response.status_code} OK"
    headers = [(k, v) for k, v in response.headers.items()]
    start_response(status, headers)
    return [response.content]
