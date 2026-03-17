Flight Deal Tracker

This is a small project I made as a learning experiment to track flight deals from London to different countries. The idea is simple: if a flight drops below a certain price listed in a Google Sheet, the program sends an email alert to anyone who signed up. I built it to practice working with APIs, automating tasks, and sending emails from Python.

What It Does

Tracks flights from London to destinations listed in a Google Sheet.

Checks if the flight price is below a specific threshold.

Lets new users sign up for email alerts right in the program.

Sends emails automatically using Gmail whenever a deal is found.

Basically, you run the program, it checks flights, and emails you if there’s a good deal.

Tech Stuff I Used

Python 3

Libraries: requests, amadeus, dotenv, smtplib

APIs: Amadeus API for flights, Sheety API for Google Sheet data

Gmail SMTP for sending emails

.env file for API keys and email credentials

How to Run It

Clone the repo:

git clone https://github.com/h0za1fa/Flight_deal_tracker.git
cd Flight_deal_tracker

Install dependencies:

pip install -r requirements.txt

Make a .env file with your credentials:

AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
SHEETY_ENDPOINT=your_sheety_endpoint
EMAIL=your_gmail_address
EMAIL_PASSWORD=your_gmail_app_password

Tip: If you use 2FA with Gmail, you need an app password.

Run the program:

python main.py

It will ask if you’re a new user and want to sign up for email alerts. After that, it checks flights and emails you if there’s a deal.

Project Files
main.py                 # Entry point of the program
flight_search.py        # Gets flights using Amadeus API
data_manager.py         # Reads/writes data to Google Sheet
notification_manager.py # Sends emails to users
user_manager.py         # Handles new user signup
What I Learned

How to work with APIs in Python

Automating tasks like checking flights and sending emails

Managing user input and storing data

Using environment variables to keep credentials safe

Future Plans

Allow tracking flights from cities other than London

Filter by travel dates

Make a small web dashboard for users

Support more email providers

License

MIT License
