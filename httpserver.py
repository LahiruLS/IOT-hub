#!/usr/bin/env python
 
from socket import *
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import networkdiscover
import variables

#Create custom HTTPRequestHandler class
class httpReqestHandler(BaseHTTPRequestHandler):
  
  
  #handle GET command
    def do_GET(self):
        rootdir = 'open/' #file location
        pin=self.path.split('/?')[1]
        print(pin)
        try:
            if not self.path.endswith('.html'):
                            tm=123
                            time.sleep(0.1)
                            #f = open(rootdir + self.path) #open requested file
                            s.send(pin);
                            #get response back
                            while True:
                                    tm = s.recv(4096)
                                    if(tm!=123):
                                            break
                    #send code 200 response
                            self.send_response(200)

                    #send header first
                            self.send_header('Content-type','text-html')
                            self.end_headers()

                    #send file content to http client
                            self.wfile.write('Message From the IOT HUB \n Device '+tm)
                    #f.close()
                            return

        except IOError:
            self.send_error(404, 'file not found')

  
  #handle POST command
def do_POST(self):
	ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
	if ctype == 'multipart/form-data':
		postvars = cgi.parse_multipart(self.rfile, pdict)
	elif ctype == 'application/x-www-form-urlencoded':
		length = int(self.headers.getheader('content-length'))
		postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
	else:
		postvars = {}

	print(postvars.get("listName", "didn't find it"))






def run():	
	print('http server is starting...')

	#ip and port of servr
	#by default http server port is 80
	server_address = ('localhost', 80)
	httpd = HTTPServer(server_address, httpReqestHandler)
	print('http server is running...')
	httpd.serve_forever()

  
if __name__ == '__main__':
	#as a client connect varible
	#connect_to_device_port('192.168.43.8',23)
	run()


