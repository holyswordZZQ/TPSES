import json
def readAdminAccount():
    with open("resources/material/adminAccounts.json") as f:
        return json.load(f)