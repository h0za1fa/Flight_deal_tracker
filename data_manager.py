import requests

api_sheety = 'ab0bae948bb33844b2269233fe476690'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.page = ''
        self.api_sheety = api_sheety
        self.base_url=f"https://api.sheety.co/{self.api_sheety}/flightDealsTrackerSheet/"


    def prices(self):
        self.page = 'prices'
        url = f'{self.base_url}prices'
        response = requests.get(url)
        return response.json()

    def add_user(self,f_name,l_name,email):
        self.page = 'users'
        url = f'{self.base_url}users'
        body = {
            'user': {
                'firstName': f_name,
                'lastName': l_name,
                'email': email,
            }
        }
        response = requests.post(url, json=body)
        return response.status_code