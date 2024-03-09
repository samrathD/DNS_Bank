import dns_network_api as dns
import bank_interact as bank
import re

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
                     vendor = matches[2]
                     card_data=card_data.split("_")
                     id = card_data[0]
                     code = card_data[1]
                     print(id)
                     print(code)
                     print(price)
                     print(vendor)
                else:
                     print("no Match")
                
                
                break
            else:
                print("No good")
                print(dns.network_check(PORT))

                break
        
process()
print(dns.network_check(PORT))

