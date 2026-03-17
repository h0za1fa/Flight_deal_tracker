✈️ Flight Deal Tracker

An automated Python-based tool that monitors flight prices and alerts you via SMS or Email when prices drop below your target threshold. It uses Google Sheets as a database to manage destinations and price limits.

🚀 Key Features

Automated Price Monitoring: Periodically scans for the cheapest flights to your desired locations.

Google Sheets Integration: Uses the Sheety API to read and update your destination list and target prices.

Automatic IATA Code Resolution: Automatically finds and fills in missing IATA airport codes for cities in your sheet.

Smart Alerts: Sends instant notifications (via Twilio or SMTP) when a deal is detected.

Flexible Search: Configurable search windows (e.g., next 6 months) and trip durations.

📂 Project Structure

File

Description

main.py

The main orchestrator that coordinates data fetching, flight searching, and notification logic.

data_manager.py

Handles all interactions with the Google Sheet via the Sheety API.

flight_search.py

Manages API calls to flight search engines (Amadeus/Tequila) for IATA codes and prices.

flight_data.py

A data class that parses complex API responses into clean, usable Python objects.

notification_manager.py

Contains the logic for sending SMS or Email alerts when a price drop is found.

🛠️ Setup & Installation

1. Prerequisites

Python 3.10+

Sheety API Account: Link your Google Sheet (Columns: City, IATA Code, Lowest Price).

Flight Search API: Sign up for Amadeus for Developers or Kiwi Tequila.

Notification Service: A Twilio account for SMS/WhatsApp or an App Password for your Gmail account.

2. Installation

Clone the repository and install the required libraries:

git clone [https://github.com/h0za1fa/Flight_deal_tracker.git](https://github.com/h0za1fa/Flight_deal_tracker.git)
cd Flight_deal_tracker
pip install -r requirements.txt


3. Environment Variables

Create a .env file in the root directory and add your credentials:

SHEETY_PRICES_ENDPOINT=[https://api.sheety.co/your_id/flightDeals/prices](https://api.sheety.co/your_id/flightDeals/prices)
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_API_SECRET=your_amadeus_secret
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_VIRTUAL_NUMBER=your_twilio_number
TWILIO_VERIFIED_NUMBER=your_personal_number


🎮 Usage

Simply run the main script to start the tracking process:

python main.py


Syncing: The script reads your Google Sheet.

Updating: If a city is missing an IATA Code, it searches for it and updates your sheet automatically.

Searching: It searches for the cheapest flights from your "home" city to all destinations in the sheet.

Alerting: If a price is lower than the "Lowest Price" listed in your sheet, an alert is sent!

📝 License

This project is open-source and available under the MIT License.