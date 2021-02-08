import requests
import json
import time
import urllib3
import socket

ip = "130.240.114.44"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP_PORT = 42069
UDP_IP = "130.240.114.51"

sensor_dictionary = {
    "24" : "power_switch",
    "30" : "power_switch",
    "42" : "power_switch",
    "48" : "power_switch",
    "54" : "power_switch",
    "61" : "power_switch",
    "67" : "power_switch",
    "72" : "power_switch",
    "78" : "power_switch",
    "85" : "power_switch",
    "132" : "power_switch",
    "150" : "power_switch",
    "151" : "power_switch",
    "162" : "power_switch",
    "163" : "power_switch",
    "60" : "power_switch",
    "66" : "power_switch",
    "84" : "power_switch",
    "90" : "power_switch",
    "114" : "power_switch",
    "138" : "power_switch",
    "108" : "power_switch",
    "126" : "power_switch",
    "120" : "power_switch",
    "127" : "power_switch",
    "144" : "power_switch",
    "96" : "power_switch",
    "156" : "power_switch",
    "102" : "power_switch",
    "267" : "power_usage",
    "271" : "power_usage",
    "274" : "power_usage",
    "277" : "power_usage",
    "280" : "power_usage",
    "284" : "power_usage",
    "287" : "power_usage",
    "290" : "power_usage",
    "293" : "power_usage",
    "299" : "state_sensor",
    "310" : "state_sensor",
    "312" : "state_sensor",
    "314" : "state_sensor",
    "316" : "state_sensor",
    "318" : "state_sensor",
    "320" : "state_sensor",
    "322" : "state_sensor",
    "326" : "state_sensor",
    "352" : "state_sensor",
    "354" : "state_sensor",
    "358" : "state_sensor",
    "360" : "state_sensor",
    "362" : "state_sensor",
    "364" : "state_sensor",
    "366" : "state_sensor",
    "368" : "state_sensor",
    "370" : "state_sensor",
    "372" : "state_sensor",
    "374" : "state_sensor",
    "376" : "state_sensor",
    "380" : "state_sensor",
    "382" : "state_sensor",
    "390" : "state_sensor",
    "392" : "state_sensor",
    "394" : "state_sensor",
    "396" : "state_sensor",
    }

def get_sensor_type(id):
    
    for key in sensor_dictionary:

        if (key == str(id)):
            return str(sensor_dictionary[key])

    raise KeyError


def sensor_call():
    
    while(True):

        try:

            id = input("Enter sensor id: ")

            try:
        
                sensor_type = get_sensor_type(id)
        
            except KeyError:
                print("Could not find id")
                sensor_type = None

            try:

                if (sensor_type == "power_switch"):
                    res1 = get_power_switch_data(id)
                    print(res1)
                    msg1 = bytes(res1, "utf-8")
                    sock.sendto(msg1, (UDP_IP, UDP_PORT))

                elif (sensor_type == "power_usage"):
                    res2 = get_power_usage_data(id)
                    print(res2)
                    msg2 = bytes(res2, "utf-8")
                    sock.sendto(msg2, (UDP_IP, UDP_PORT))
                    
                elif (sensor_type == "state_sensor"):
                    res3 = get_state_sensor_data(id)
                    print(res3)
                    msg3 = bytes(res3, "utf-8")
                    sock.sendto(msg3, (UDP_IP, UDP_PORT))
                    
                else:
                    print("no sensor type")

                
            except AttributeError as e:
                print("Fibaro REST api error", e)

        except KeyboardInterrupt:
            print("turning off")
            break

            
        
    

def get_power_switch_data(id):
    
    try:
        
        resp = requests.get("http://"+ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
        
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | value: ", data['properties']['value'], " | power: ", data['properties']['power'])
        temp_str = str(id) + ";" + str(data['properties']['value']) + ";" + str(data['properties']['power'])
        return temp_str

    

def get_power_usage_data(id):
    
    try:
        
        resp = requests.get("http://"+ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | total wattage: ", data['properties']['energy'], " | power: ", data['properties']['power'])
        temp_str = str(id) + ";" + str(data['properties']['energy']) + ";" + str(data['properties']['power'])
        return temp_str



def get_state_sensor_data(id):
    
    try:
        
        resp = requests.get("http://"+ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | value: ", data['properties']['value'], " | time since: ", data['properties']['lastBreached'])
        temp_str = str(id) + ";" + str(data['properties']['value']) + ";" + str(data['properties']['lastBreached'])
        return temp_str

        

    
            
