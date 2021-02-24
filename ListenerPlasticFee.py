import paho.mqtt.client as mqtt #import the client1
import time
from datetime import datetime
import json

hashmap = {}
hashmap_deposits = {}

def hash_function(info): # funzione hash che va ad aggiungere o assegnare il totale del peso versato per ogni utente.
    chiave = info['idUser']
    valore = info['weight']
    presente = False
    for k in hashmap:
        if k == chiave:
            presente = True
            hashmap[chiave] += valore
            hashmap_deposits[chiave] += 1
    if presente == False:
            hashmap[chiave] = valore
            hashmap_deposits[chiave] = 1
           
    print("hash utente e kg: ", hashmap)
    print("hash utente e deposits: ", hashmap_deposits)


def on_message(client, userdata, message): # funzione fornita dalla libreria paho di mqtt per ricevere i messaggi.
    print("message received: " ,str(message.payload.decode("utf-8")))
    print("message topic: ",message.topic)
    info = json.loads(str(message.payload.decode("utf-8")))
    hash_function(info)


broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("P1") #creazione dell istanza del client listener

client.on_message=on_message #link alla funzione on_message

print("connecting to broker")
client.connect(broker_address) #connessione al broker

client.loop_start() #Inizio del loop di ascolto

print("Subscribing to topic","plasticDelivery")
print(datetime.now())
client.subscribe("plasticDelivery") # il listerner si sottoscrive al topic plastic delivery
time.sleep(300000) # il loop rimane in aperto per 300 secondi

client.loop_stop() # fine del loop


