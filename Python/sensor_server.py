import socketserver
import socket
import threading
import fibaro
import widefind
import time

print_lock = threading.Lock()

class ThreadedUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        
        self.client_socket = self.request[1]
        self.data = self.request[0].strip()
        self.data = self.data.decode("utf-8")
        self.data = self.data.split(";")

        if (self.data[0] == "fibaro"):
            
            try:
        
                self.id = int(self.data[1])
                self.res = fibaro.fibaro_conn(self.id)

            except Exception as e:
                self.res = str(self.id) + ";error_sensor"


            with print_lock:
                print("Sending: {} to {}".format(self.res, self.client_address[0]))
        
            self.response = bytes(self.res, "utf-8")
            self.client_socket.sendto(self.response, self.client_address)
            

        elif (self.data[0] == "widefind"):

            try:
                
                self.TTL = int(self.data[1])
                self.wf = widefind.widefind(self.TTL, self.client_socket, self.client_address, print_lock)

                widefind_thread = threading.Thread(target=self.wf.run())

                widefind_thread.daemon = True
                widefind_thread.start()

            except Exception as e:
                with print_lock:
                    print(e)
            
            

class ThreadingUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):    
    pass

        

if __name__ == "__main__":
    
    HOST = "130.240.114.52"
    PORT = 42069

    server = ThreadingUDPServer((HOST, PORT), ThreadedUDPHandler)

    with server:

        try:

            server_thread = threading.Thread(target = server.serve_forever)

            server_thread.daemon = True
            server_thread.start()
        
            print("Server loop in thread: {}".format(server_thread.name))

        
            try:

                while server_thread.is_alive():
                    pass
                
            except KeyboardInterrupt:
                server.shutdown()
                server_thread.join()
                print("Thread {} running: {}".format(server_thread.name, server_thread.is_alive()))

        except Exception as e:
            print(e)
            
            

