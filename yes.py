import requests

ip = "130.240.114.44"
id = 85


resp = requests.get("http://"+ip+"/api/devices/"+str(id), auth=("unicorn@ltu.se", "jSCN47bC"))
if(resp.status_code != 200):
    print("something went wrong")
    print(resp.status_code)
for todo_item in resp:
    print(todo_item)
