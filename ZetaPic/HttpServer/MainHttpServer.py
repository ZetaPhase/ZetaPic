"""
LSC Server Beta

Main Server Logic

Base Version 2.4
"""
#2013

PRODUCT_ID = 'ExaPhaser LSC Server v0.3.1' 

from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket
import webbrowser

siteURL = ''
from os import curdir, sep
import os

from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

class OmniBeanHandler(BaseHTTPRequestHandler):
    #GET Handler
    def do_GET(self):
        requestUrl = self.path
        args = self.path.split('?')
        self.path = args[0]
        params = ''
        if (len(args) == 2):
            params = args[1]
        indexpage = 'index.html'
        reqURL = self.path[1:]
        
        print('REQUESTED ['+reqURL+']')
        if self.path.endswith("/"):
            self.path+=indexpage
            print('ADDED /'+indexpage)
        if (not os.path.exists(reqURL)):
            print ('ERR 404 ['+reqURL+']')
            #if (not os.path.exists('/index.html')):
            #    self.path = "/index.htm"
        try:
            #Check the file extension required and set the right MIME
            #type
            sendReply = False
            semdError = False
            errorCode = -1
            lsc = False
            mimetype='text/plain'
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
                
    
            if self.path.endswith(".lsc"):
                mimetype='text/html'
                sendReply = True
                lsc = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".xap"):
                mimetype='application/x-silverlight-app'
                sendReply = True
            if self.path.endswith(".xbap"):
                mimetype='application/x-ms-xbap'
                sendReply = True
            if self.path.endswith(".xaml"):
                mimetype='application/xaml+xml'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            else:
                sendError = True
                errorCode='1104 Not Found'
            if sendReply:
		#Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                content = f.read()
                if (lsc):
                    content = str.encode(LSC.parseToHTML(bytes.decode(content),params))
                self.wfile.write(content)
                f.close()
            else:
                if sendError:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    content = "Server rejected request.".encode()
                    self.wfile.write(content)
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

        

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""

def start_lsc_server(HOST,PORT):
    global siteURL
    #HOST = '127.0.0.1'
    httpd = HTTPServer((HOST, PORT), OmniBeanHandler)    
    print('Starting',PRODUCT_ID)
    url = 'http://'+HOST+':'+str(PORT)
    print('Server running on:',url)
    siteURL = url
    print('Close the python window to stop server.')
    #webbrowser.open_new(siteURL)
    httpd.serve_forever()

HOST_NAME = os.getenv("IP", "0.0.0.0") # c9 Listen IP
PORT_NUMBER = int(os.getenv("PORT", 8080)) #c9 listen port
start_lsc_server(HOST_NAME, PORT_NUMBER)