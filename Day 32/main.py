import smtplib
import random
import datetime as dt


with open("quotes.txt", 'r') as file:
    quotes = file.readlines()
now = dt.datetime.now()
second_password = "rejn tzlg syte jcqh"
my_mail = "mr.yashagraindia@gmail.com"
APP_PASSWORD = "jbxj dhgt cbgu webt"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=second_password)
    if now.weekday() == 0:
        connection.sendmail(from_addr=my_mail,
                            to_addrs="it.damoh@gmail.com",
                            msg=f"Subject: Monday Quote\n\n{random.choice(quotes)}"
                            )

