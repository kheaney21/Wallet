import sys

bank = Bank()
accts = bank.getAccts() #dictionary of accounts

def getInput():
	option1 = raw_input("New or returning user? (new/return)" )
	if(option1.lower() == "new"):
		newWallet()
	elif(option1.lower() == "return"):
		returnUser()
	else:
		print("Invalid input")
		
	
def newWallet():
	addr = raw_input("Enter email address")
	#check if address is taken
	if(accts.has_key(addr)):
		return "Email address is already in use"
	pswd = raw_input("Enter password")
	bank.newAcct(addr, pswd)
	accts = bank.getAccts()
	
	
def returnUser():
	addr = raw_input("Enter email address")
	if(login(addr) == True):
		toContinue = 1
		while toContinue == 1:
			option2 = input("1 - Check balance \n 2 - Make a Payment")
			if(option2 == 1):
				return accts.getBalance()
			elif(option2 == 2):
				recipient = raw_input("Enter email address of recipient")
				#check if valid recipient
				if(accts.has_key(recipient)):
					amount = raw_input("Enter amount in USD")
					if(accts[addr].sufFunds(amount)):
						accts[addr].payment(amount)
						accts[recipient].addFunds(amount)
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
