import sys
import os

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
try:
    from email.MIMEBase import MIMEBase # python2
except:
    from email.mime.base import MIMEBase # python3

def send_email(
    recipients,
    subject,
    text,
    sender,
    password,
    attachments=[]
):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(text))

    for file in attachments: # get all attachments
        filename = os.path.basename(file)
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename="{0}".format(filename))
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sender, password)
    mailServer.sendmail(sender, recipients, msg.as_string())
    mailServer.close()