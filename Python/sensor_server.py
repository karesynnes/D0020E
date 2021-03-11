#
#This application sets up a threaded UDP server for communication between a client and the Fibaro REST api as well as the mqtt broker that publishes
#updates on the 'ltu-system/messages/' topic. This server can only hosted on a machine within the 'LTU-H2Al' network as both the mqtt broker as
#well as the REST api will be unreachable form any othe network. This application must be run with 'fibaro.py' and 'widefind.py' in the same
#directory and the interchange of data between the components must follow current structures.
#Both of these separate python files accually contain the functionallty for communicating with both fibaro and widefind systems
#
#This application was written as a part of the 'Unreal visualization of a smart home' project active during the course D0020E from 11-2020 to
#03-2021.
#
#Author: Jakob Moregård
#
#If you have any issue with how this code is written, don't flame me, just work to improve areas you think are lacking 5head.
#

import socketserver
import socket
import threading
import fibaro
import widefind
import time

#create a asynchronous locking variable for printing
print_lock = threading.Lock()

#the handler class, this class handles all incomming connections
#when a new connection has been received, a class instance will run in a new thread
#class inherits 'BaseRequestHandler' that is designed to work with any 'ThreadingMixIn' class
class ThreadedUDPHandler(socketserver.BaseRequestHandler):

    #overwrites the inherited handle method of 'BaseRequestHandler'
    def handle(self):
        
        #all information of the client that sent the request
        self.client_socket = self.request[1] #client socket
        self.data = self.request[0].strip()
        self.data = self.data.decode("utf-8")
        self.data = self.data.split(";") #data of the request

        if (self.data[0] == "fibaro"):
            
            try:
                self.id = int(self.data[1])
                self.res = fibaro.fibaro_conn(self.id) #calls the 'main' function in the 'fibaro.py' file

            except Exception as e:
                self.res = str(self.id) + ";error_sensor"

            #asynchronous print
            with print_lock:
                print("Sending: {} to {}".format(self.res, self.client_address[0]))
        
            self.response = bytes(self.res, "utf-8")
            self.client_socket.sendto(self.response, self.client_address) #send data back to client


        elif (self.data[0] == "widefind"):

            try:
                
                self.TTL = int(self.data[1])

                #creates widefind instance with TimeToLive, client socket/address, and asynchronous print variable
                self.wf = widefind.widefind(self.TTL, self.client_socket, self.client_address, print_lock) 

                #runs widefind instance in new thread
                widefind_thread = threading.Thread(target=self.wf.run())

                widefind_thread.daemon = True
                widefind_thread.start()

            except Exception as e:
                with print_lock:
                    print(e)

#the class of the actual UDP server, it inherits the ThreadingMixIn class
#no base variables or methods are overwritten because of 'pass'     
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):    
    pass
    
#application starts when the file is run, this is the 'Main' function of the entire application.
if __name__=="__main__":
    
    HOST = "" #ip of the host machine
    PORT = 42069

    #create the server instance and tell or server class that the handler class is 'ThreadedUDPHandler'
    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPHandler)

    with server:

         try:

            #starts main thread that will run the server class
            server_thread = threading.Thread(target = server.serve_forever)

            server_thread.daemon = True
            server_thread.start()
        
            print("Server loop in thread: {}".format(server_thread.name))
 
            try:

                while server_thread.is_alive():
                    pass
                
            except KeyboardInterrupt: #attempt to kill the server thread, works by clicking ctrl+c a few times lol. (no time to fix it)
                    server.shutdown()
                    server_thread.join()
                    print("Thread {} running: {}".format(server_thread.name, server_thread.is_alive()))

         except Exception as e:
            print(e)
            


