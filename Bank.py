from Wallet import Wallet

class Bank:
	'Database for accounts/wallets'
	def __init__(self):
		self.numAccts = 0
		self.accts = {}
		
	def getAccts(self):
		return self.accts
		
	def newAcct(self, addr, pswd):
		self.numAccts = self.numAccts + 1
		newWallet = wallet(addr, pswd)
		self.accts[addr] = newWallet
		
	
	
