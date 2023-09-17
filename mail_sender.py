import smtplib
from parameters import *

my_email = EMAIL_ID
my_password = PASSWORD


def send_email(receiver, subject, content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{content}")
