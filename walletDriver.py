import sys

class WalletDriver:
	'Driver for wallet project'
	def __init__(self):
		bank = Bank() #problem here
		accts = bank.getAccts() #dictionary of accounts

	def getInput(self):
		option1 = raw_input("New or returning user? (new/return)" )
		if(option1.lower() == "new"):
			self.newWallet()
		elif(option1.lower() == "return"):
			self.returnUser()
		else:
			print("Invalid input")
		
	
	def newWallet(self):
		addr = raw_input("Enter email address")
		#check if address is taken
		if(accts.has_key(addr)):
			return "Email address is already in use"
		pswd = raw_input("Enter password")
		bank.newAcct(addr, pswd)
		accts = bank.getAccts()
	
	
	def returnUser(self):
		addr = raw_input("Enter email address")
		if(login(addr) == True):
			toContinue = 1
			while toContinue == 1:
				user = accts[addr]
				option2 = input("1 - Check balance \n 2 - Make a Payment")
				if(option2 == 1):
					return user.getBalance()
				elif(option2 == 2):
					recipient = raw_input("Enter email address of recipient")
					#check if valid recipient
					if(accts.has_key(recipient)):
						amount = raw_input("Enter amount in USD")
						if(user.sufFunds(amount)):
							signature = user.sign(amount)
							request = user.sendRequest(signature)
							if(accts[recipient].verifySig(request)):
								user.payment(amount)
								accts[recipient].addFunds(amount)
							else:
								print("Signature verification failed")
					else:
						print("Invalid recipient")	
				else:
					print("Invalid Input")
				toContinue = 0
				toContinue = raw_input("Enter 1 to continue")
				
	def login(self, addr):
		if not bank.getAccts().has_key(addr):
			print("Invalid address")
		else:
			pswd = raw_input("Enter password")
			if(pswd == accts[addr].getPassword()):
				return True	
			else:
				print("Invalid password")
				return False
		
driver = WalletDriver()
driver.getInput()