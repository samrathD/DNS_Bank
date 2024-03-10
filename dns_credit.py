import dns_bank_api as dns_bank
import bank_interact as bank

vendors = {
    "1": ["Samrath","12216819421512709190",0],
    "2": ["Martin", "7581189392171227832", 0],
    "3" : ["Bank","11343867294248593023", 0]
}
CODE = 2098533117

# Value to search for

# Find the key based on the search value

def credit(vendor,amount):
    index = next((key for key, value in vendors.items() if value[1] == vendor), None)
    print(vendors["3"][1])
    if vendors[str(index)][2] + int(amount) <= 300 :
        print(dns_bank.bank_transfer(vendors["3"][1],vendor, CODE,amount))
        vendors[str(index)][2]+=int(amount)
        print("Your credit is - {}".format(vendors[str(index)][2]))
        return 0
    else:
        print("Too much debt broke boi!!")
        return 1
