import smtplib
from email.message import EmailMessage

from dotenv import dotenv_values

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        env = dotenv_values("constants.env")
        self.sender_email = env["EMAIL"]
        self.sender_password = env["PASSWORD"]

    def send_notification(self, email_list, content,):
        for to_email in email_list:
            msg = EmailMessage()
            msg.set_content(content)
            msg["Subject"] = "New Flight Deal Found! ✈️"
            msg["From"] = self.sender_email
            msg["To"] = to_email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)