import paho.mqtt.client as MQTT
import time
import json;

def print_json(msg):
    json_object = json.loads(msg);
    
    
    if(json_object["message"][0:6] == "REPORT"):
        a = json_object["message"].split(",")
        print(a[0][7:23])
        if (str(a[0][7:23]) == "67BA3CF4E0622323"):
        
            x = a[2]
            y = a[3]
            z = a[4]

            print("x:{}, y:{}, z:{}".format( x,y,z))
        

def on_connect(client, msg, flags, rc):
        
    if (rc == 0):
        print("Connect succesfull to broker: ", rc)
        
    else:
        print("Connect error: ", rc)
    

def on_message(client, userdata, message):
    print_json(str(message.payload.decode("utf-8")))
    


def widefind_conn():

    #ltu-system/messages/ topic for position.
    broker_ip='130.240.74.55';
    broker_port=1883;
    client = MQTT.Client();
    
    client.connect(broker_ip,broker_port);
    print("Awaiting connect callback...")

    client.on_connect = on_connect

    print("Subscribing to everything...")
    client.subscribe("ltu-system/messages/", 0)
    #client.subscribe("#", 0)
    flag = True
        
    try:
        client.loop_start()
        while (flag):
            
            client.on_message = on_message

    except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()
        flag = False
        print("turning off")
        

    
    

