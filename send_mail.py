import smtplib
from email.mime.text import MIMEText

def send_email(customer, dealer , rating , comments):
    port = 2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login = 'ecaa12f7b78b43'
    password = 'e4d989832dc22a'
    message = (f"<h3>New Feedback Submission<h3/><ul>"
               f"<li>Customer : {customer}<li/>"
               f"<li>Dealer: {dealer}<li/>"
               f"<li>Rating : {rating}<li/>"
               f"<li>Comments : {comments}<li/><ul/>")
    sender_email = "mail1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())