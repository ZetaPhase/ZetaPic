import time
import BaseHTTPServer
import os

HOST_NAME = os.getenv("IP", "0.0.0.0") # c9 Listen IP
PORT_NUMBER = int(os.getenv("PORT", 8080)) #c9 listen port
DOCUMENT_ROOT = "htdocs"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("random", "Hello World")
        self.end_headers()
        self.wfile.write("<html><body><p>Thank you for your submission.</p></body></html>")
        #print self.rfile
        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("random", "Hello World")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
        self.wfile.write("<a href='http://www.google.com'>Google</a>")
        self.wfile.write("<form action='demo_form.asp' method='get' id='form1'> First name: <input type='text' name='fname'><br>Last name: <input type='text' name='lname'><br><input type='submit' value='Submit'></form>")
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")
        #print self.params
        print self.path
        print self.headers.getheaders('User-Agent')

httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)

if __name__ == '__main__':
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
