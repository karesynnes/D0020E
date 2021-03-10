import paho.mqtt.client as MQTT
import time
import json;

class widefind:
    def __init__(self, time_to_live, client_socket, client_address, print_lock):
        self.TTL = time_to_live
        self.client_socket = client_socket
        self.client_address = client_address
        self.broker_ip = '130.240.74.55';
        self.broker_port = 1883;
        self.client = MQTT.Client();
        self.print_lock = print_lock


    def send_json(self, msg):
    
        self.json_object = json.loads(msg);
        if(self.json_object["message"][0:6] == "REPORT"):
            self.a = self.json_object["message"].split(",")
            if (str(self.a[0][7:23]) == "67BA3CF4E0622323"):
                self.x = self.a[2]
                self.y = self.a[3]
                self.z = self.a[4]

                self.res = "widefind;" + self.x + ";" + self.y + ";" + self.z

                with self.print_lock:
                    print("Sending: {} to {}".format(self.res, self.client_address[0]))
                
                self.response = bytes(self.res, "utf-8")
                self.client_socket.sendto(self.response, self.client_address)
        

    def on_connect(self, client, msg, flags, rc):
        
        if (rc == 0):
            pass
        
        else:
            pass
    

    def on_message(self, client, userdata, message):
        
        self.send_json(str(message.payload.decode("utf-8")))
        

    def run(self):

        self.client.connect(self.broker_ip, self.broker_port);
        self.client.on_connect = self.on_connect
    
        self.client.subscribe("ltu-system/messages/", 0)
        self.client.loop_start()

        self.end_time = self.TTL + time.time()

        while (time.time() < self.end_time):

            self.client.on_message = self.on_message

        self.client.disconnect()


