import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url="https://api.sheety.co/ab0bae948bb33844b2269233fe476690/flightDealsTrackerSheet/prices")

    def prices(self):
        return self.response.json()