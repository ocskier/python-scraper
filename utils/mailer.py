""" This is a module to email real estate local data"""
import smtplib
import ssl
import os
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 465
context = ssl.create_default_context()

def send_email():
    """This is a function to send the excel spreadsheet via email"""
    admin_user = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")
    sender = os.getenv("SENDER")
    receivers = os.getenv("RECEIVER")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Real Estate Scrape"
    message["From"] = admin_user
    message["To"] = receivers

    filename = os.path.join("sheet.xlsx")
    attachment = open(os.path.join("sheet.xlsx"), 'rb')
    xlsx = MIMEBase('application','vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    xlsx.set_payload(attachment.read())

    encode_base64(xlsx)
    xlsx.add_header('Content-Dispolsition', 'attachment', filename=filename)
    message.attach(xlsx)

    text = ''

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',PORT,context=context) as server:
            server.login(admin_user,password)
            server.sendmail(admin_user, receivers, message.as_string())
            print("Successfully sent email")
    except smtplib.SMTPException as _e:
        print(_e)
