import sys

sys.path.append('../')

import dns_network_api as dns
import dns_bank_api as bank
import time
import userInfo as db

def main():
	print()
	print("what would you like to do?")
	print("1) check vendor account statuses?")
	print("2) check credit statuses?")
	print("3) create a credit account?")
	print("4) create a credit account?")
	print("5) to exit")
	mode = int(input("input a number (1-5): "))

	if mode == 1:
		vendors()
	elif mode == 2:
		creditUsers()
	elif mode == 3:
		createAcc()
	elif mode == 4:
		regVendor()
	elif mode == 5:
		return
	main()

def creditUsers():
	for i in range(len(db.vendors)):
		pass

def regVendor():
	print("_____")
	name = input("what's your name: ")
	card = input("what's your card ID: ")
	print()
	print("Please confirm the information")
	print("Name: ", name)
	print("card ID: ", card)
	c = input("[1]confirm [2]cancel: ")
	
	if(c != "1"):
		return
	
	db.vendors[str(len(db.vendors) + 1)] = {
		"name": name,
		"ID": card
	}
	db.update()

def createAcc():
	print("_____")
	name = input("what's your name: ")
	card = input("what's your card ID: ")
	code = input("what's your card code: ")
	credit = 200
	points = 0
	print()
	print("Please confirm the information")
	print("Name: ", name)
	print("card ID: ", card)
	print("card code: ", code)
	print("credit limit:", credit)
	print("points:", points)
	c = input("[1]confirm [2]cancel: ")
	
	if(c != "1"):
		return

	user = {
		"name":name,
		"code":code,
		"creditLimit":credit,
		"points":points,
		"debt":0
	}
	#must double check that the account exists
	db.write(card, user)
	

def vendors():
	print("status:")
	print(dns.network_check("105"))
	print("_____________________")
	print("Vendors:")
	for i in range(len(db.vendors)):
		idx = str(i+1)
		print(idx + ":" + db.vendors[idx]["name"])
	id = input("Which vendor would you like to check? ")
	print()
	print(bank.bank_get_info(db.vendors[id]["ID"]))
	time.sleep(5)

main()