#
#This application handles all communication with the MQTT broker for the widefind system hosted on the 'LTU-H2Al' network.
#This application will be started and used by the 'sensor_server.py' application which must be run with 'fibaro.py' and 'widefind.py' in the same
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

import paho.mqtt.client as MQTT
import time
import json;

#Since data publications with mqtt if done on callback this application has a built in TimeToLive, specified by the client
#it sends data to the client on callback as long as the TimeToLive is not exceeded.
#This class creates a widefind instance that will run in a unique dedicated thread for each instance.
#The class takes arguments for TimeToLive in seconds, the client socket/address for transmission and a asynchronous
#variable for printing to preserve the console output of the application as a whole.
class widefind:
    def __init__(self, time_to_live, client_socket, client_address, print_lock):
        self.TTL = time_to_live
        self.client_socket = client_socket
        self.client_address = client_address
        self.print_lock = print_lock

        #arguments for the MQTT topic broker/client
        self.broker_ip = '130.240.74.55'; 
        self.broker_port = 1883;
        self.client = MQTT.Client();
        

    #method called by 'on_message' callback method and it parses x, y, and z coordinates from the widefind system
    #and then sends that data back to the client of the main server.
    def send_json(self, msg):
    
        self.json_object = json.loads(msg);
        if(self.json_object["message"][0:6] == "REPORT"):
            self.a = self.json_object["message"].split(",")
            #if (str(self.a[0][7:23]) == "67BA3CF4E0622323"): #this if statement allows the client to only receive published messages
                                                              #from a specific widefind satelite. placeholder satelite id is 67BA3CF4E0622323'
                                                              #to listen to all satelites comment this line out.
            self.x = self.a[2]
            self.y = self.a[3]
            self.z = self.a[4]

            self.res = "widefind;" + self.x + ";" + self.y + ";" + self.z

            #asynchronous print
            with self.print_lock:
                print("Sending: {} to {}".format(self.res, self.client_address[0]))
                
            self.response = bytes(self.res, "utf-8")
            self.client_socket.sendto(self.response, self.client_address) #send to the client
        

    #This method is called on callback once a connection has been established with the broker
    def on_connect(self, client, msg, flags, rc):

        #it does nothing at the moment, no time to implement functionality for failure
        if (rc == 0):
            pass
        
        else:
            pass
    

    #This method is called on callback once a message has been published on the broker topic
    def on_message(self, client, userdata, message):
        
        self.send_json(str(message.payload.decode("utf-8")))
        

    #The 'main' function of this application, this method is the target method when a 'widefind' instance is started in a thread.
    def run(self):

        #conncets to the broker and sets up the 'on_connect' callback method
        self.client.connect(self.broker_ip, self.broker_port);
        self.client.on_connect = self.on_connect

        #subscribes to the messages topic
        self.client.subscribe("ltu-system/messages/", 0)
        self.client.loop_start()

        #handles TimeToLive
        self.end_time = self.TTL + time.time()

        while (time.time() < self.end_time):

            #sets up the 'on_message' callback method
            self.client.on_message = self.on_message

        self.client.disconnect()


