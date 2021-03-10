import socket
import time

flag = True

def client(msg, ttl):
    
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address1 = ("130.240.114.14", 42069)


    msg = bytes(msg, "utf-8")
    socket1.sendto(msg, address1)

    end_time = ttl + time.time()

    while(end_time > time.time()):
            
        data = socket1.recvfrom(1024)
        if (data != None):
            print(data)

    flag = False


if __name__ == "__main__":

        ttl = input("TTL: ")
        msg = "widefind;" + str(ttl)

        client(msg, float(ttl))


            

        

    
