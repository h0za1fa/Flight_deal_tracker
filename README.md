I'll create a professional, copy-paste ready README.md file for your GitHub repository:
markdown# ✈️ Flight Deal Tracker

An automated Python-based tool that monitors real-time flight prices for your dream destinations and sends instant alerts when prices drop below your budget threshold. No more manual price checking—let the bot do the work!

## 🎯 Overview

Manually checking flight prices daily is tedious and time-consuming. Flight prices fluctuate constantly, and you often miss narrow "deal windows." This automation tool solves that problem by continuously monitoring prices and notifying you the moment a deal appears.

**How it works:**
1. 📊 Reads your destination wishlist and price targets from Google Sheets
2. 🔍 Automatically verifies and updates IATA airport codes
3. 🔎 Searches flight APIs for the cheapest available flights (next 6 months)
4. 💰 Compares found prices against your budget thresholds
5. 📲 Sends instant SMS/Email alerts when deals are detected

## ✨ Features

- **Automated Price Monitoring**: Checks flight prices across multiple destinations without manual intervention
- **Google Sheets Integration**: Use a spreadsheet as your dashboard—add cities without touching code
- **Smart IATA Lookup**: Automatically resolves city names to airport codes (e.g., "Paris" → "CDG/ORY")
- **Multi-Channel Alerts**: Supports both SMS (via Twilio) and Email (via SMTP)
- **Flexible Date Search**: Scans a 6-month window to find the absolute best price
- **Secure Credential Management**: All API keys stored safely in environment variables

## 🏗️ Project Structure
```
Flight_deal_tracker/
│
├── main.py                    # Main orchestrator - manages the workflow
├── data_manager.py            # Google Sheets interface via Sheety API
├── flight_search.py           # Flight API integration (Amadeus)
├── flight_data.py             # Data model for parsing flight responses
├── notification_manager.py    # Alert system (SMS/Email)
├── requirements.txt           # Python dependencies
└── .env                       # API credentials (not tracked in git)
```

### Key Components

| File | Purpose |
|------|---------|
| `main.py` | Entry point that coordinates data retrieval, flight searches, and notifications |
| `data_manager.py` | Handles GET/PUT requests to Google Sheets via Sheety API |
| `flight_search.py` | Manages Amadeus API authentication and flight queries |
| `flight_data.py` | Structured class for parsing complex JSON flight data |
| `notification_manager.py` | Encapsulates SMS (Twilio) and Email (SMTP) logic |

## 🛠️ Tech Stack

**Language:** Python 3.x

**APIs & Services:**
- [Amadeus Flight API](https://developers.amadeus.com/) - Real-time flight search and IATA lookup
- [Sheety API](https://sheety.co/) - Google Sheets REST API bridge
- [Twilio](https://www.twilio.com/) - SMS/WhatsApp notifications
- Gmail SMTP - Email notifications

**Python Libraries:**
- `requests` - HTTP requests to external APIs
- `python-dotenv` - Environment variable management
- `twilio` - Twilio SDK for messaging
- `smtplib` - Built-in email functionality

## 🚀 Setup & Installation

### Prerequisites

- Python 3.x installed
- Accounts for the following services:
  - [Sheety](https://sheety.co/) (free tier available)
  - [Amadeus for Developers](https://developers.amadeus.com/) (free tier available)
  - [Twilio](https://www.twilio.com/) (optional, for SMS) or Gmail account (for email)

### Installation Steps

1. **Clone the repository**
```bash
   git clone https://github.com/h0za1fa/Flight_deal_tracker.git
   cd Flight_deal_tracker
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Set up Google Sheet**
   
   Create a Google Sheet with these columns:
   | City | IATA Code | Lowest Price |
   |------|-----------|--------------|
   | Paris | | 500 |
   | Tokyo | | 800 |
   | New York | | 600 |

   Connect it to Sheety and get your API endpoint.

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
```env
   # Sheety API
   SHEETY_ENDPOINT=your_sheety_endpoint_url
   
   # Amadeus API
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_API_SECRET=your_amadeus_api_secret
   
   # Twilio (Optional - for SMS)
   TWILIO_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   YOUR_PHONE_NUMBER=your_destination_phone_number
   
   # Email (Optional - for email alerts)
   EMAIL_PROVIDER_SMTP=smtp.gmail.com
   EMAIL_PROVIDER_PASSWORD=your_gmail_app_password
```

   **⚠️ Security Note:** Never commit your `.env` file to GitHub! It's already in `.gitignore`.

## 💻 Usage

Run the tracker:
```bash
python main.py
```

The script will:
1. Load your destination list from Google Sheets
2. Update any missing IATA codes automatically
3. Search for flights from your origin city
4. Send you an alert if any price is below your threshold

### Setting Your Origin City

Edit `main.py` and set your departure city:
```python
ORIGIN_CITY = "LON"  # London - change to your city's IATA code
```

## 📚 What I Learned

Building this project involved several technical challenges that deepened my understanding of API integration and automation:

### 1. **OAuth2 Token Management**
Implementing the Amadeus API authentication flow with token expiration and refresh logic taught me about session management in API-based applications.
```python
def get_destination_code(self, city_name):
    headers = {"Authorization": f"Bearer {self._token}"}
    query = {"keyword": city_name, "subType": "CITY"}
    response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
    return response.json()["data"][0]["iataCode"]
```

### 2. **Complex JSON Parsing**
The Amadeus API returns deeply nested JSON with hundreds of flight options. Extracting the cheapest price required careful navigation of the data structure.
```python
for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY, destination["iataCode"])
    if flight and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly to {flight.destination_city}!"
        )
```

### 3. **API Rate Limiting**
Learned to implement throttling mechanisms to avoid hitting Sheety and Amadeus API limits during iteration loops.

### 4. **Secure Credential Handling**
Implemented environment variable management using `python-dotenv` to prevent credential exposure in version control.
```python
self._api_key = os.environ.get("AMADEUS_API_KEY")
self._api_secret = os.environ.get("AMADEUS_API_SECRET")
```

### 5. **Data Validation**
Built checks to ensure IATA codes exist before attempting flight searches, preventing unnecessary API calls and errors.

## 🔮 Future Enhancements

- [ ] Add scheduling with GitHub Actions or cron jobs for automated daily checks
- [ ] Implement multi-city route search (e.g., London → Paris → Tokyo)
- [ ] Add web scraping fallback for alternative flight sources
- [ ] Create a simple web dashboard for monitoring
- [ ] Support for flexible date ranges (±3 days)
- [ ] Price history tracking and trend analysis

## 🤝 Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Amadeus for Developers](https://developers.amadeus.com/) for the flight data API
- [Sheety](https://sheety.co/) for the Google Sheets API integration
- [Twilio](https://www.twilio.com/) for SMS notification capabilities

---

**Made with ☕ by [h0za1fa](https://github.com/h0za1fa)**
This README is now ready to copy and paste directly into your GitHub repository! It's professional, comprehensive, and highlights the technical depth of your project—perfect for showcasing on your resume. 🚀