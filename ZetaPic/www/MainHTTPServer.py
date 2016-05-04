#import time
import BaseHTTPServer
import os
import string,cgi,time
from os import curdir, sep
import mimetypes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import skimage
from skimage import novice
from skimage import data
from skimage.viewer import ImageViewer
from skimage import io

HOST_NAME = os.getenv("IP", "0.0.0.0") # c9 Listen IP
PORT_NUMBER = int(os.getenv("PORT", 8080)) #c9 listen port
#HOST_NAME = "127.0.0.1"
#PORT_NUMBER = 80
DOCUMENT_ROOT = "htdocs"

def convertFileToString(fileName):
    with open(fileName, 'r') as myfile:
        htmlString = myfile.read()
    return htmlString

class LSC:
    def parseToHTML(lsc,args):
        html = LSCParser.LanguageService(lsc,args)
        return html

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
        args = self.path.split('?')
        self.path = args[0]
        indexpage = "index.html"
        params = ""
        lsc = False
        if self.path.endswith("/"):
            self.path+=indexpage
        mime = {".html":"text/html", ".css":"text/css", ".png":"image/png",
                ".xaml":'application/xaml+xml', ".xbap":'application/x-ms-xbap',
                ".jpg":"image/jpg", ".gif":"image/gif", ".js":"application/javascript",
                ".xap":"application/x-silverlight-app", ".lsc":"text/html"}
        reversePath = self.path[::-1]
        pathExtension = ""
        for char in reversePath:
            pathExtension += char
            if char == ".":
                break
        pathExtension = pathExtension[::-1]
        print pathExtension
        if pathExtension in mime.keys():
            if pathExtension == ".lsc":
                lsc = True
            self.send_response(200)
            print pathExtension
            self.send_header('Content-type', mime[pathExtension])
            self.end_headers()
            f = open(curdir + sep + self.path, 'rb')
            content = f.read()
            if (lsc):
                content = str.encode(LSC.parseToHTML(bytes.decode(content),params))
            self.wfile.write(content)              
            f.close()
            return

if __name__ == '__main__':
    try:
        httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

