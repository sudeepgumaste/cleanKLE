import smtplib
import os
from email.message import EmailMessage

EMAIL=os.environ.get('CA_MAIL')
PASS = os.environ.get('CA_PASS')


class Mail():
    def __init__(self,to,content):
        self.msg = EmailMessage()
        self.msg['To'] = to 
        self.msg.set_content(content)
        self.msg['Subject'] = 'No Reply'
        self.msg['From'] = EMAIL

    def send(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL,PASS)

            smtp.send_message(self.msg)
