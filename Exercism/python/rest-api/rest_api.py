class RestAPI(object):
    def __init__(self, database=None):
        self.database = database
        self.payload = 0
        self.response = 0
        self.all_user_names_list = []

    def get(self, url, payload=None):
        import json
        if url == "/users":
            users_list = []
            if payload:
                self.payload = json.loads(payload)
                for user_name in self.payload["users"]:
                    for user in self.database["users"]:
                        if user["name"] == user_name:
                            users_list.append(user)
                            break

            else:
                for user in self.database["users"]:
                    users_list.append(user)
            return json.dumps({"users": sorted(users_list, key=lambda user: user["name"])})

    def post(self, url, payload=None):
        import json
        if url == "/add":

            self.payload = json.loads(payload)
            self.response = {
                    "name": self.payload["user"],
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                }
            self.database["users"].append(self.response)
            return json.dumps(self.response)

        if url == "/iou":
            import json
            self.payload = json.loads(payload)
            self.all_user_names_list = self.all_user_names()
            for user in self.database["users"][:]:
                if user["name"] == self.payload["lender"]:
                    self.database["users"].remove(user)
                    try:
                        user["owed_by"][self.payload["borrower"]]
                        user["owed_by"][self.payload["borrower"]] += self.payload["amount"]
                    except:
                        user["owed_by"][self.payload["borrower"]] = self.payload["amount"]
                    user = self.calculate_the_due(user)
                    user["balance"] = self.calculate_balance(user)
                    self.database["users"].append(user)
                if user["name"] == self.payload["borrower"]:
                    self.database["users"].remove(user)
                    try:
                        user["owes"][self.payload["lender"]]
                        user["owes"][self.payload["lender"]] += self.payload["amount"]
                    except:
                        user["owes"][self.payload["lender"]] = self.payload["amount"]
                    user = self.calculate_the_due(user)
                    user["balance"] = self.calculate_balance(user)
                    self.database["users"].append(user)
            return self.get("/users", json.dumps({
                "users": [
                    self.payload["lender"],
                    self.payload["borrower"]
                        ]
                }))

    def calculate_balance(self, user):
        self.owes = sum(user["owes"].values())
        self.owed_by = sum(user["owed_by"].values())
        return self.owed_by - self.owes

    def calculate_the_due(self, user):
        for user_name in self.all_user_names_list:
            try:
                if user["owes"][user_name] > user["owed_by"][user_name]:
                    user["owes"][user_name] -= user["owed_by"][user_name]
                    user["owed_by"].pop(user_name)
                elif user["owes"][user_name] < user["owed_by"][user_name]:
                    user["owed_by"][user_name] -= user["owes"][user_name]
                    user["owes"].pop(user_name)
                else:
                    user["owes"].pop(user_name)
                    user["owed_by"].pop(user_name)
            except:
                pass
        return user

    def all_user_names(self):
        for user in self.database["users"]:
            self.all_user_names_list.append(user["name"])
        return self.all_user_names_list
