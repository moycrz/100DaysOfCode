from twilio.rest import Client
import smtplib

TWILIO_SID = "ACee986c7e770dfb8039d211122c541951"
TWILIO_AUTH_TOKEN = "e1ad0574d2566eb6c7ff1927b6b9e1aa"
TWILIO_VIRTUAL_NUMBER = "+19206858193"
TWILIO_VERIFIED_NUMBER = "+527717051973"
MY_EMAIL = "moises.crza@gmail.com"
PASSWORD = "J@maicanegra2708"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message, to):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # make the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to,
                msg=f"Subject: Low price alert! :D\n\n{message}"
            )
