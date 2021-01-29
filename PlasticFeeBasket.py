import paho.mqtt.client as mqtt #import the client1
import time
import random
from threading import Thread
import json
import datetime



class ThreadBasket():
	def __init__(self,idBasket):
		self.broker_address="127.0.0.1" 
		self.client = mqtt.Client("mqtt-spy") 
		self.client.connect(self.broker_address) 
		self.client.subscribe("plasticDelivery")
		self.idBasket = idBasket

	def doDelivery(self,weight,idUser):
		self.x = {
			"idUser" : idUser ,
			"idBasket" : self.idBasket,
			"date" : str(datetime.datetime.now()),
			"weight" : weight
		}
		self.delivery = json.dumps(self.x)
		self.client.publish("plasticDelivery",self.delivery)





idBasket = "B001";
t = ThreadBasket(idBasket);
print("Welcome to plastifFee Basket: "+idBasket)

valore = "no";

while True:

	if valore == "no" :
		userCode = input('Hi, Insert your user code please: ')	

	weightDelivery =int(input('Insert the weight of the plastic into the basket: '))

	t.doDelivery(weightDelivery,userCode)
	print("Your delivery is done! Thank you!")
	
	print("Do you need to make another deposit?")
	risposta = input('')
	if risposta == "no":
		valore = "no";
		print("Bye");
	elif risposta == "yes":
		valore = "yes";
	


		
	


