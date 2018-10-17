import pycrypto as pyc
from Crypto.PublicKey import RSA
from Crypto import Random

rgen = Random.new().read

def __init__(self, email, password):
	self.email = email
	self.password = password
	key = RSA.generate(256, rgen)
	#addr = 
	balance = 0
	
def payment(self, amount, recipient, password):
	if(self.password = password):
		self.balance = balance - amount
	else:
		print("invalid password")
	
def checkBalance(self, password):
	if(self.password = password):
		print(self.balance)
	else: print("invalid password")
	
def addFunds(self, amount, target, password):
	if(self.password = password):
		self.balance = balance + amount
	else: print("invalid password")
	
