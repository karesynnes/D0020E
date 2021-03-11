import socket
import time

flag = True

def client(msg):
    
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address1 = ("130.240.114.14", 42069)
    data = None


    msg = bytes(msg, "utf-8")
    while (data == None):

        try:
            socket1.sendto(msg, address1)
            print("sent, ", msg)
            data = socket1.recvfrom(1024)
        except KeyboardInterrupt:
            break
        
    #end_time = ttl + time.time()

    #while(end_time > time.time()):
            
        #data = socket1.recvfrom(1024)
        #if (data != None):
            #print(data)

    #flag = False
    print("recv ", data)


if __name__ == "__main__":

        #ttl = input("TTL: ")
        msg = "fibaro;299"

        client(msg)


            

        

    
