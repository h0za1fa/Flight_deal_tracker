from http.client import responses

import requests, json
from data_manager import DataManager

client_id= "T4SHkBCdfWAt0GfErt5KWOBxgbFdLUDU"
client_secret = "qbWq5aMtLe4SjAfI"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = ''
        self.destination_sheet = DataManager()
        self.destination_sheet_json = self.destination_sheet.prices()

    def get_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=body)
        self.access_token = response.json()['access_token']

    def search_flight(self):
        responses = []   #tur gai yar mohabtan wale
        for i in range(0,9):
            destination = self.destination_sheet_json["prices"][i]["iataCode"]

            headers = {"Authorization": f"Bearer {self.access_token}"}

            # Flight-dates API call
            params = {
                "originLocationCode": "LON",
                "destinationLocationCode": destination,
                "departureDate": "2026-06-15",  # Use a specific date in the future
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": 1
            }
            response = requests.get(
                url="https://test.api.amadeus.com/v2/shopping/flight-offers",
                headers=headers,
                params=params
            )
            if response.status_code == 401:
                print("Getting token...")
                self.get_token()  # Call your method that updates self.access_token

                # Update headers with the NEW token
                headers["Authorization"] = f"Bearer {self.access_token}"

                # Retry the request
                response = requests.get(
                    url="https://test.api.amadeus.com/v2/shopping/flight-offers",
                    headers=headers,
                    params=params
                )
            responses.append(response.json())
        return responses
