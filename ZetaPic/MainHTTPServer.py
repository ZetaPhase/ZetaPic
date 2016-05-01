import time
import BaseHTTPServer
import os
import cgi

#HOST_NAME = os.getenv("IP", "0.0.0.0") # c9 Listen IP
#PORT_NUMBER = int(os.getenv("PORT", 8080)) #c9 listen port
HOST_NAME = "127.0.0.1"
PORT_NUMBER = 80
DOCUMENT_ROOT = "htdocs"

def convertFileToString(fileName):
    with open(fileName, 'r') as myfile:
        htmlString = myfile.read()
    return htmlString

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        d = {}
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD": "POST"}
        )
        for item in form.list:
            d[item.name] = item.value
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(convertFileToString("test.html").format(**d))
        #self.wfile.write("<html><body><p>Thank you for your submission, {fname} {lname}.</p></body></html>".format(**d))

        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write(convertFileToString("test.txt"))
        self.wfile.write("<form action='demo_form.asp' method='post' id='form1'> First name: <input type='text' name='fname'><br>Last name: <input type='text' name='lname'><br><input type='submit' value='Submit'></form>")
        print os.getcwd()
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
