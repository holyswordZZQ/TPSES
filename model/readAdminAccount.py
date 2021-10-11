import json
def readAdminAccount():
    with open("resources/jsons/adminAccounts.json") as f:
        return json.load(f)