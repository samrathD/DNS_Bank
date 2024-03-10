import dns_network_api as dns
import dns_bank_api as dns_bank
import dns_credit as credit
import bank_interact as bank
import re
import time


TEMP_VENDOR = "12216819421512709190"
TEMP_CREDIT = "12216819421512709190"

PORT = "105"
print(dns.network_check(PORT))
def process():
    while dns.network_status() == "Status: Server Is Online":
            if dns.network_check(PORT)!="Check: {}: 0".format(PORT) :
                transcation = dns.network_request(PORT)
                print(transcation)
                pattern = r'\{([^}]*)\}'
                matches = re.findall(pattern,transcation)

                if matches:
                     card_data = matches[0]
                     price = matches[1]
                    #  vendor_choice = matches[2].split("_")
                    #  vendor = vendor_choice[0]
                    #  choice = vendor_choice[1]
                     choice = 1
                     card_data=card_data.split("_")
                     id = card_data[0]
                     code = card_data[1]
                else:
                     print("no Match")
                

                if choice == 0:
                    bank.process_bank_transfer(id, TEMP_VENDOR, code, price)
                elif choice == 1:
                    if credit.credit(TEMP_VENDOR,price) == 0:
                         print("Transcation completed")
                    else:
                         print("Transcation denied")

                time.sleep(5)
            else:
                print("No good")
                print(dns.network_check(PORT))

                break
        
process()

print(dns_bank.bank_get_info(TEMP_VENDOR))
print(dns.network_check(PORT))
