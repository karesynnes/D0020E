import requests
import json
import time
import urllib3
import socket

fibaro_ip = "130.240.114.44"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_ip = "130.240.114.51"
udp_port = 42069

sensor_dictionary = {
    "24" : ["switch_sensor"],
    "30" : ["switch_sensor"],
    "42" : ["switch_sensor"],
    "48" : ["switch_sensor"],
    "54" : ["switch_sensor"],
    "61" : ["switch_sensor"],
    "67" : ["switch_sensor"],
    "72" : ["switch_sensor"],
    "78" : ["switch_sensor"],
    "85" : ["switch_sensor"],
    "60" : ["switch_sensor"],
    "66" : ["switch_sensor"],
    "84" : ["switch_sensor"],
    "90" : ["switch_sensor"],
    "108" : ["switch_sensor"],
    "132" : ["switch_sensor"],
    "150" : ["switch_sensor"],
    "151" : ["switch_sensor"],
    "162" : ["switch_sensor"],
    "163" : ["switch_sensor"],
    "114" : ["switch_sensor"],
    "138" : ["switch_sensor"],
    "126" : ["switch_sensor"],
    "120" : ["switch_sensor"],
    "127" : ["switch_sensor"],
    "144" : ["switch_sensor"],
    "102" : ["switch_sensor"],
    "267" : ["power_sensor"],
    "271" : ["power_sensor"],
    "274" : ["power_sensor"],
    "277" : ["power_sensor"],
    "280" : ["power_sensor"],
    "284" : ["power_sensor"],
    "287" : ["power_sensor"],
    "290" : ["power_sensor"],
    "293" : ["power_sensor"],
    "299" : ["state_sensor"],
    "310" : ["state_sensor"],
    "312" : ["state_sensor"],
    "316" : ["state_sensor"],
    "318" : ["state_sensor"],
    "320" : ["state_sensor"],
    "322" : ["state_sensor"],
    "326" : ["state_sensor"],
    "352" : ["state_sensor"],
    "354" : ["state_sensor"],
    "358" : ["state_sensor"],
    "360" : ["state_sensor"],
    "362" : ["state_sensor"],
    "364" : ["state_sensor"],
    "366" : ["state_sensor"],
    "368" : ["state_sensor"],
    "372" : ["state_sensor"],
    "374" : ["state_sensor"],
    "376" : ["state_sensor"],
    "380" : ["state_sensor"],
    "382" : ["state_sensor"],
    "390" : ["state_sensor"],
    "392" : ["state_sensor"],
    "394" : ["state_sensor"],
    "396" : ["state_sensor"],
    "323" : ["other_sensor"],
    "335" : ["other_sensor"],
    "341" : ["other_sensor"],
    "347" : ["other_sensor"],
    "337" : ["other_sensor"],
    "343" : ["other_sensor"],
    "349" : ["other_sensor"],
    "336" : ["other_sensor"],
    "342" : ["other_sensor"],
    "348" : ["other_sensor"],
    "96" : ["dual_sensor", "370"], 
    "156" : ["dual_sensor", "314"] 
    }

def get_sensor_type(id):
    
    for key in sensor_dictionary:

        if (key == str(id)):
            return sensor_dictionary[key]

    raise KeyError

def UDP_send(ip, port, msg):

    msg = bytes(msg, "utf-8")
    sock.sendto(msg, (ip, port))
    
    


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

                if (sensor_type == None):
                    print("no sensor type")

                elif (sensor_type[0] == "switch_sensor"):
                    res1 = get_switch_sensor_data(id, sensor_type[0])
                    print(res1)
                    UDP_send(udp_ip, udp_port, res1)

                elif (sensor_type[0] == "power_sensor"):
                    res2 = get_power_sensor_data(id, sensor_type[0])
                    print(res2)
                    UDP_send(udp_ip, udp_port, res2)
                    
                elif (sensor_type[0] == "state_sensor"):
                    res3 = get_state_sensor_data(id, sensor_type[0])
                    print(res3)
                    UDP_send(udp_ip, udp_port, res3)

                elif (sensor_type[0] == "other_sensor"):
                    res4 = get_other_sensor_data(id, sensor_type[0])
                    print(res4)
                    UDP_send(udp_ip, udp_port, res4)

                elif (sensor_type[0] == "dual_sensor"):
                    id2 = int(sensor_type[1])
                    res4 = get_dual_sensor_data(id, sensor_type[0], id2)
                    print(res4)
                    UDP_send(udp_ip, udp_port, res4)
                    
                else:
                    print("no sensor type")

                
            except AttributeError as e:
                print("Fibaro REST api error", e)

        except KeyboardInterrupt:
            print("turning off")
            break

            
        
    

def get_switch_sensor_data(id, sensor):
    
    try:
        
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
        
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | value: ", data['properties']['value'], " | power: ", data['properties']['power'])
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value']) + ";" + str(data['properties']['power'])
        return temp_str

    

def get_power_sensor_data(id, sensor):
    
    try:
        
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | total wattage: ", data['properties']['energy'], " | power: ", data['properties']['power'])
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['energy']) + ";" + str(data['properties']['power'])
        return temp_str



def get_state_sensor_data(id, sensor):
    
    try:
        
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | value: ", data['properties']['value'], " | time since: ", data['properties']['lastBreached'])
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value']) + ";" + str(data['properties']['lastBreached'])
        return temp_str


def get_other_sensor_data(id, sensor):

    try:
        
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
    
    else:
        data = resp.json()
        print("ID: ", id, " | value: ", data['properties']['value'])
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value'])
        return temp_str


def get_dual_sensor_data(id, sensor, id2):

    try:
        
        resp1 = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)
        resp2 = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id2), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
    
    if((resp1.status_code or resp2.status_code) != 200):
        print("Error: ", resp1.status_code, resp2.status_code)
        raise AttributeError(str(resp1.status_code), str(resp2.status_code))
    
    else:
        data1 = resp1.json()
        data2 = resp2.json()

            
        print("ID: ", id, " | on: ", data1['properties']['value'], " | power: ", data1['properties']['power'], " | open: ", data2['properties']['value']," | time since: ", data2['properties']['lastBreached'])
            
        temp_str = str(id) + ";" + sensor + ";" + str(data1['properties']['value']) + ";" + str(data1['properties']['power']) + ";" + str(data2['properties']['value']) + ";" + str(data2['properties']['lastBreached'])
        return temp_str

        

    
            
