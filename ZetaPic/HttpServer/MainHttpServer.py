import time
import BaseHTTPServer

HOST_NAME = '192.168.1.78' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.send_header("random", "Hello World")
        s.end_headers()
        s.wfile.write("<html><body><p>Thank you for your submission.</p></body></html>")
        print s.rfile
        
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.send_header("random", "Hello World")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        s.wfile.write("<a href='http://www.google.com'>Google</a>")
        s.wfile.write("<form action='demo_form.asp' method='get' id='form1'> First name: <input type='text' name='fname'><br>Last name: <input type='text' name='lname'><br><input type='submit' value='Submit'></form>")
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")
        print s.params
        print s.path
        print s.headers.getheaders('User-Agent')

httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
