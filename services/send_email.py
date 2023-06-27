import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

SENDGRID_API_KEY = "your_sendgrid_api_key_here"

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)


def send_email(to_email, subject, email_text):
    from_email = Email("noreply@example.com")
    to_email = To(to_email)
    content = Content("text/plain", email_text)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
