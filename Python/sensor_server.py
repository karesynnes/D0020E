import socketserver
import socket
import threading
import fibaro
import widefind


class ThreadedUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        
        self.client_socket = self.request[1]
        self.data = self.request[0].strip()
        self.data = self.data.decode("utf-8")
        self.data = self.data.split(";")

        try:
        
            if (self.data[0] == "fibaro"):
                self.id = int(self.data[1])
                self.res = fibaro.fibaro_conn(self.id)

            else:
                raise TypeError

        except TypeError:
            self.res = str(self.id) + ";error_sensor"
        
        self.string = "sending: " + self.res
        printer.println(self.string)
        
        self.response = bytes(self.res, "utf-8")
        printer.self.client_socket.sendto(self.response, self.client_address)


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):    
    pass
            

class SharedPrint(object):
  
    def __init__(self):
        self.lock = threading.Lock()
        self.val = 0
        
    def println(self, string):
        self.lock.acquire()
        try:
            print(string, self.val)
            self.val = self.val + 1
        finally:
            self.lock.release()
        


def main():
    
    HOST = "130.240.114.52"
    PORT = 42069

    printer = SharedPrint()

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPHandler)

    with server:

        server_thread = threading.Thread(target=server.serve_forever)

        server_thread.daemon = True
        server_thread.start()
        
        string = "Server loop in thread: " + str(server_thread.name)
        println(string)
        
        try:

            while server_thread.is_alive():
                pass
                
        except KeyboardInterrupt:
            Flag = False
            server.shutdown()
            server_thread.join()
            string = "Thread " + str(server_thread.name) + " running: " + str(server_thread.is_alive())
            printer.println(string)
            return

