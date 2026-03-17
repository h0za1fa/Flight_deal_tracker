from twilio.rest import Client

account_sid = 'ACc6b338fd254d315932a0de624711189a'
auth_token = '33c3ae9200c7cc8a16b608c2ee192f28'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, message):
        self.message = message
        self.message = self.client.messages.create(
            from_= '+16693143684',
            body=self.message,
            to='+923262976625',
        )
