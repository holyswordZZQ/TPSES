import json
def readAdminAccount():
    with open("resources/jsons1/adminAccounts.json") as f:
        return json.load(f)