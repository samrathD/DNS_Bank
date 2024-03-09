import dns_network_api as dns
import dns_bank_api as dns_bank
import bank_interact as bank
import re
import time


TEMP_VENDOR = "12216819421512709190"
PORT = "105"
# print(dns.network_check(PORT))
# def process():
#     while dns.network_status() == "Status: Server Is Online":
#             if dns.network_check(PORT)!="Check: {}: 0".format(PORT) :
#                 transcation = dns.network_request(PORT)
#                 print(transcation)
#                 pattern = r'\{([^}]*)\}'
#                 matches = re.findall(pattern,transcation)

#                 if matches:
#                      card_data = matches[0]
#                      price = matches[1]
#                      vendor = matches[2]
#                      card_data=card_data.split("_")
#                      id = card_data[0]
#                      code = card_data[1]
#                      print(id)
#                      print(code)
#                      print(price)
#                      print(vendor)
#                 else:
#                      print("no Match")
                
#                 bank.process_bank_transfer(id, TEMP_VENDOR, code, price)
#                 time.sleep(5)
#                 break
#             else:
#                 print("No good")
#                 print(dns.network_check(PORT))

#                 break
        
# process()

print(dns_bank.bank_get_info(TEMP_VENDOR))
print(dns.network_check(PORT))

