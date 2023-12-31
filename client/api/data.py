import requests
from ..app.settings import NETWORK_URL


class Api:
    def __init__(self, auth):
        self.auth = auth
        self.url = NETWORK_URL

    def get(self, endpoint=""):
        self.url = f"{NETWORK_URL}{endpoint}"
        r = requests.get(self.url, auth=self.auth)
        return r.status_code, r.json()

    def post(self, endpoint="", data=None):
        self.url = f"{NETWORK_URL}{endpoint}"
        r = requests.post(self.url, auth=self.auth, json=data)
        return r.status_code, r.json()

    def update(self, endpoint="", data=None):
        self.url = f"{NETWORK_URL}{endpoint}"
        r = requests.put(self.url, auth=self.auth, json=data)
        return r.status_code

    def delete(self, endpoint=""):
        self.url = f"{NETWORK_URL}{endpoint}"
        r = requests.delete(self.url, auth=self.auth)
        return r.status_code
