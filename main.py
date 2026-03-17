#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_data
import notification_manager

notification = notification_manager.NotificationManager()
res = flight_data.FlightData()
dict_prices = res.min_prices()
flights = res.search_flight()

for flight in flights:
    destination = flight["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    price = flight["data"][0]["price"]["total"]
    departure_date = flight["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]

    for min_flight in dict_prices['prices']:
        city = min_flight['city']
        city_iata = min_flight['iataCode']
        lowest_price = min_flight['lowestPrice']

        if city_iata == destination and float(price) <= float(lowest_price):
            message = f'Confrats! Go to {city} in just {price} 💷 on {departure_date}'
            notification.send_notification(message)

        else:
            print('Sorry no deal could be found')