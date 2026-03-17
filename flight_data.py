import data_manager
import flight_search


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.sheet_data = data_manager.DataManager()
        self.sheetData = self.sheet_data.prices()
        self.flightData_obj = flight_search.FlightSearch()
        self.flightData = self.flightData_obj.search_flight()

    def search_flight(self):
        return self.flightData

    def min_prices(self):
        return self.sheetData