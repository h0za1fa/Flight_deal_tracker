import data_manager
import flight_search


class FlightData:
    #This class is responsible for structuring the flight data.
    # def __init__(self):



    def search_flight(self):
        flightData_obj = flight_search.FlightSearch()
        flightData = flightData_obj.search_flight()
        return flightData

    def min_prices(self):
        sheet_data = data_manager.DataManager()
        sheetData = sheet_data.prices()
        return sheetData