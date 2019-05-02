import smtplib
import os
from email.message import EmailMessage
import logging

EMAIL=os.environ.get('CA_MAIL')
PASS = os.environ.get('CA_PASS')
logging.basicConfig(filename='./cleanApp/logs/all.log', level=logging.INFO)


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
            try:
                smtp.send_message(self.msg)
            except:
                logging.info('Error! no internet connectivity')
                print('Error! no internet connectivity')

