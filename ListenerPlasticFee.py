import paho.mqtt.client as mqtt #import the client1
import time
from datetime import datetime
import json

hashmap = {}
hashmap_deposits = {}

def hash_function(info):
    chiave = info['idUser'];
    valore = info['weight'];
    presente = False;
    for k in hashmap:
        if k == chiave:
            presente = True;
            hashmap[chiave] += valore;
            hashmap_deposits[chiave] += 1;
    if presente == False:
            hashmap[chiave] = valore;
            hashmap_deposits[chiave] = 1;
           
    print("hash utente e kg: ", hashmap);
    print("hash utente e deposits: ", hashmap_deposits);
            
            
def print_user(self,user,hashmap):
	totale = hashmap[user];

def on_message(client, userdata, message):
    print("message received: " ,str(message.payload.decode("utf-8")))
    print("message topic: ",message.topic)
    info = json.loads(str(message.payload.decode("utf-8")));
    hash_function(info);
  


broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","plasticDelivery")
print(datetime.now())
client.subscribe("plasticDelivery")


time.sleep(300000) # wait
client.loop_stop() #stop the loop


