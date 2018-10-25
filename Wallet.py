import sys
import random

#import pycrypto as pyc
#from Crypto.PublicKey import RSA
#from Crypto import Random

#rgen = Random.new().read

class Wallet:
	'Class for wallet object'
	def __init__(self, addr, password):
		self.addr = addr
		self.password = password
		keys = genKey() 
		balance = 0
		
	def getPassword():
		return password
		
	def getBalance():
		return balance
		
	def getPublicKey():
		return keys[1]
	
	#assume recipient is registered with the bank
	def payment(self, amount):
		#check for sufficient funds
		if(sufFunds):
			self.balance = balance - amount
	
	#assume target is registered with the bank
	def addFunds(self, amount):
		self.balance = balance + amount
		
	#check for sufficient funds
	def sufFunds(self, amount):
		if(balance < amount):
			print("Insufficient funds")
			return False
		else:
			return True
		
	#generate a number and check if prime via
	def genPrime(self, n):
		
		#loop?
		
		#generate pseudorandom number
		x = random.randint(3, n, 2)
		
	def genKeys():
		#maximum number
		n = 10,000
		x = genPrime(n)
		
		#generate private key
		#privKey = 
		#generate public key
		#pubKey = 
		
		#keys = (pubKey, privKey)
		#return keys
		
		
		