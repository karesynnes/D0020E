#
#This application handles all communication with the Fibaro REST api for the fibaro home center hosted on the 'LTU-H2Al' network.
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

import requests
import json
import time
import urllib3

#The ip that fibaro home center is hosted on.
fibaro_ip = "130.240.114.44"

#This dictionary is essential, it contains all current available sensors in room u121.
#If more sensors have been added or current onces changed (glhf) one must manually go over all sensors
#on fibaro home center and add them to the dictionary.
#The sensors are categorized depending on what the do, or more accurately, how the json object they return is structured.
#switch_sensors are outlets, they look like on/off button in fibaro home center
#power_sensors are power readings i.e. stove, stove fan etc..
#state_sensors are doors, cupboards, drawers etc...
#other_sensors are humidity, temperature, light levels etc...
#dual_sensors are two sensors that represent the same object i.e. microwave door and power.
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

#method gets the type of sensor from the dictionary based on id
def get_sensor_type(id):
    
    for key in sensor_dictionary:

        if (key == str(id)):
            return sensor_dictionary[key]

    raise KeyError
    
#main method of this application, this is called when the server wants data of a specific sensor.
def fibaro_conn(id):
    
    while(True):

        try:

            try:
        
                sensor_type = get_sensor_type(id)
        
            except KeyError:
                print("Could not find id")
                sensor_type = None
            
            try:
                
                #checks what type of sensor belong to the id and calls appropriate type method
                if (sensor_type == None):
                    print("no sensor type")

                elif (sensor_type[0] == "switch_sensor"):
                    res1 = get_switch_sensor_data(id, sensor_type[0])
                    return res1

                elif (sensor_type[0] == "power_sensor"):
                    res2 = get_power_sensor_data(id, sensor_type[0])
                    return res2
                    
                elif (sensor_type[0] == "state_sensor"):
                    res3 = get_state_sensor_data(id, sensor_type[0])
                    return res3

                elif (sensor_type[0] == "other_sensor"):
                    res4 = get_other_sensor_data(id, sensor_type[0])
                    return res4

                elif (sensor_type[0] == "dual_sensor"):
                    id2 = int(sensor_type[1])
                    res5 = get_dual_sensor_data(id, sensor_type[0], id2)
                    return res5
                    
                else:
                    print("no sensor type")

                
            except AttributeError as e:
                print("Fibaro REST api error", e)

        except KeyboardInterrupt:
            print("turning off")
            break

            
        
    
#method for retrieving switch data 
def get_switch_sensor_data(id, sensor):

    try:

        #REST api call     
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
            
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
        
    else:
        data = resp.json()
        #this parsing of data is what separates sensor types
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value']) + ";" + str(data['properties']['power'])
        return temp_str

    
#method for retrieving power data
def get_power_sensor_data(id, sensor):

    try:

        #REST api call     
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
        
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
        
    else:
        data = resp.json()
        #this parsing of data is what separates sensor types
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['energy']) + ";" + str(data['properties']['power'])
        return temp_str


#method for retrieving state data
def get_state_sensor_data(id, sensor):

    try:

        #REST api call     
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
        
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
        
    else:
        data = resp.json()
        #this parsing of data is what separates sensor types
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value']) + ";" + str(data['properties']['lastBreached'])
        return temp_str


#method for retrieving other data
def get_other_sensor_data(id, sensor):

    try:

        #REST api call 
        resp = requests.get("http://"+fibaro_ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"), timeout = 5)

    except Exception as e:
        print("timeout", e)
        raise AttributeError(e)
        
    if(resp.status_code != 200):
        print("Error: ", resp.status_code)
        raise AttributeError(str(resp.status_code))
        
    else:
        data = resp.json()
        #this parsing of data is what separates sensor types
        temp_str = str(id) + ";" + sensor + ";" + str(data['properties']['value'])
        return temp_str


#method for retrieving dual data
def get_dual_sensor_data(id, sensor, id2):

    try:

        #REST api call     
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
        #this parsing of data is what separates sensor types
        temp_str = str(id) + ";" + sensor + ";" + str(data1['properties']['value']) + ";" + str(data1['properties']['power']) + ";" + str(data2['properties']['value']) + ";" + str(data2['properties']['lastBreached'])
        return temp_str

       
