import sys

sys.path.append('../')

import dns_network_api as network
import time
import dns_bank_api as bank
import userInfo as db
import math

def send(vendorID, custID, custCode, money):
    print(bank.bank_transfer(custID, vendorID, custCode, money))
    time.sleep(5)
    print(bank.bank_get_info(db.vendors["1"]["ID"]))

def main():
    # while():
    time.sleep(2)
    print(network.network_check("105"))

    if(network.network_check("105").split(": ")[2] != "0"):
        
        info = network.network_request("105")
        # print(info)
        data = info.split("{")
        data.pop(0)
        for i in range(len(data)):
            data[i] = data[i].split("}")[0]
        merchant = data[0].split("_")
        # print(data)
        # print(merchant)

        if int(data[1]) < 0:
            return

        mode = data[2].split("_")
        vendor = mode[0]
        sys = 1
        if(len(mode) > 1 and mode[1] == "1"):
            sys = 2

        #vID, merchantID, pw, val
        if sys == 1:
            send(db.vendors[vendor]["ID"], merchant[0], merchant[1], data[1])
        else:
            #person exists in credit users
            if merchant[0] not in db.creditUsers.keys():
                print("user doesn't exist")
                return
            customer = db.creditUsers[merchant[0]]
            print(customer)
            if merchant[1] != merchant[1]:
                print("user key not correct")
                return
            total = float(data[1])
            if total > customer["credit"]:
                print("insufficient credit!")
                return
            #check personal account balance


            db.creditUsers[merchant[0]]["credit"] -= total
            db.creditUsers[merchant[0]]["debt"] += total
            print(send(db.bank["ID"], merchant[0], customer["code"], str(db.bank['fee'])))
            time.sleep(5)
            print(send(db.vendors[vendor]["ID"], db.bank["ID"], db.bank["code"], data[1]))
            db.creditUsers[merchant[0]]["points"] += math.ceil(total)
            db.update()


        time.sleep(5)

    else:
        print("FAIL")

main()
