import json

with open('userInfo.json', 'r') as f:
    data = json.load(f)
    f.close()
vendors = data['vendors']
bank = data['bank']
creditUsers = data['creditUsers']

def write(id, user):
    creditUsers[id] = user
    
    update()

def update():
    dict = {
        "vendors":vendors,
        "bank":bank,
        "creditUsers":creditUsers
    }
    jsonObj = json.dumps(dict)

    with open('userInfo.json', 'w') as oF:
        oF.write(jsonObj)
        oF.close()