import sys
import random

#import pycrypto
from Crypto.Hash import SHA256

class Wallet:
	'Class for wallet object'
	def __init__(self, addr, password):
		self.addr = addr
		self.password = password
		self.keys = genKey() 
		self.balance = 0
		
	def getPassword():
		return password
		
	def getBalance():
		return balance
		
	def getPublicKey():
		return keys[2]
		
	def getMod():
		return keys[1]
	
	#assume recipient is registered with the bank (checked in driver)
	def payment(self, amount):
		#check for sufficient funds
		if(sufFunds):
			self.balance = balance - amount
	
	#assume target is registered with the bank (checked in driver)
	def addFunds(self, amount):
		self.balance = balance + amount
		
	#check for sufficient funds
	def sufFunds(self, amount):
		if(balance < amount):
			print("Insufficient funds")
			return False
		else:
			return True
		
	def genPrime(self, n, k):
		x = random.randint(3, n, 2)
		while not (isPrime(x, k)):
			x = random.randint(3, n, 2)
		return x
			
	#check if prime via miller-rabin test
	def isPrime(self, n, k):
		
		#calculate d
		n = temp
		s = 0
		while temp % 2 == 0:
			temp = temp/2
			s = s + 1
			
		d = n/(2**s)
		
		count = 0
		while count < k:
			#update counter
			count = count + 1
			#generate pseudorandom number
			a = random.randint(2, n - 1)
			x = a**d % n
			if (x == 1 or x == n - 1):
				continue
			for i in range (s-1):
				x = (x**2) % n
				if x == 1:
					return False
				if x == n - 1:
					continue
				
			return False
		return True
			
		
	def genCoprime(p, q):
		e = random.randint(3, n, 2)
		while not (e % p - 1 != 0 and e % p - 1 != 0):
			e = random.randint(3, n, 2)	
		return e
		
	def genKeys():
		#maximum number
		max = 10,000
		#number of iterations
		k = 10,000
		p = genPrime(max, k)
		q = genPrime(max, k)
				
		#modulus
		n = p * q
		
		#public exponent
		e = genCoprime(p, q)
		
		#integer k
		k = random.randint(2, n)
		
		#private exponent
		d = (1 + k(p - 1)(q - 1))/e
		
		#generate private key
		privKey = d
		#generate public key
		pubKey = e
		#modulus
		mod = n
		
		keys = (mod, pubKey, privKey)
		return keys
		
	def getHash(self, message):
		#get hash
		hash = SHA256.new(message)
		return hash
		
	#generates signature for a message	
	def sign(self, hashValue):
		#encrypt
		d = self.keys[3]
		n = self.keys[1]
		signature = hashValue**(d % n)
		return signature
		
	def sendRequest(self, message):
		hashValue1 = self.getHash(message)
		#modulus
		n = self.keys[1]
		#public key
		e = self.keys[1]
		signature = self.sign(hashValue1)
		request = (n, e, signature, hashValue1)
		return request
		
	#verifies that signature matches hash value	
	def verifySig(self, request):
		#decrypt
		n = request[1]
		e = request[2]
		signature = request[3]
		hashValue1 = request[4]
		
		hashValue2 = signature**(e % n)
		if hashValue1 == hashValue2:
			return True
		return False
		
		
		
		
		
