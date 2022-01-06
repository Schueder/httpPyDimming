from http.server import BaseHTTPRequestHandler, HTTPServer
import screen_brightness_control as sbc
import cgi
import ast
current = 100;

class GP(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()
        
    def do_GET(self):
        global current
        if current != self.path.split("=")[1] :
            print("Great, you made it! Backlight will set to: ",self.path.split("=")[1], "%");
            sbc.set_brightness(self.path.split("=")[1])

        current = self.path.split("=")[1]
           
    
def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ("################################################################")
    print ("#                                                              #")
    print ("#                  BRILLIANCE SAMPEL SERVER                    #")
    print ("#                                                              #")
    print ("#  To change the brightness you can call following             #")
    print ("#  code sample in a browser, which will change the brigtness   #")
    print ("#  of your monitor to 10%                                      #")
    print ("#                                                              #")
    print ('#     var oReq = new XMLHttpRequest();                         #')
    print ('#     oReq.open("GET", "http://localhost:8088/?brightness=10"  #')
    print ("#     oReq.send()                                              #")
    print ("#                                                              #")
    print ("################################################################")
    print ("  Brilliance Server ( localhost:", port ,") started ...");
    print ("                                     Let's rock ... ");
    
    httpd.serve_forever()


run()
