import data_manager
import flight_search
from dotenv import dotenv_values

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.env_values = dotenv_values("constants.env")

    def search_flight(self):
        flightData_obj = flight_search.FlightSearch(amadeus_client_id=self.env_values["AMADEUS_CLIENT_ID"],amadeus_client_secret=self.env_values["AMADEUS_CLIENT_SECRET"])
        flightData = flightData_obj.search_flight()
        return flightData

    def min_prices(self):
        sheet_data = data_manager.DataManager()
        sheetData = sheet_data.prices()
        return sheetData