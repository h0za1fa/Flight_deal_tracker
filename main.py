#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import dotenv_values
import flight_data
import notification_manager
import data_manager

env = dotenv_values("constants.env")

notification = notification_manager.NotificationManager()
res = flight_data.FlightData()
dict_prices = res.min_prices()
data_manager = data_manager.DataManager()

logged_in = False
looping = True

while looping:
    if logged_in:
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
                    message = f'Congrats! Go to {city} in just {price}£ on {departure_date}'
                    email_list = data_manager.get_users()
                    notification.send_notification(email_list ,message)
                    print(message)
                    looping = False

                elif not looping:
                    print('Sorry no deal could be found')
    else:
        sign_in = input('Are you an existing user? (y/n)')
        if sign_in.lower() == 'n':
            f_name = input('First Name: ')
            l_name = input('Last Name: ')
            mail = input('Email: ')
            confirm_email = input('Confirm Email: ')
            if mail != confirm_email:
                print('Mail not valid')
            elif mail == confirm_email and data_manager.add_user(f_name, l_name, mail) == 200:
                print('Congrats! You have successfully Signed up!')
                signed_mail = [mail]
                message = f'Congrats! You have successfully Signed up!'
                notification.send_notification(signed_mail ,message)
        elif sign_in.lower() == 'y':
            print('Welcome to Flight Search!')
            print('Mails are being sent shortly!')
            logged_in = True
