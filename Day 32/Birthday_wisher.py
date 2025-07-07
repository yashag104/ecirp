
import pandas
import datetime as dt
import smtplib
import random

my_mail = "yashagra104@gmail.com"
password = "jbxj dhgt cbgu webt"

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {}
for (index, row) in birthdays.iterrows():
    day = row['day']
    month = row['month']
    mail = row['email']
    name = row['name']

    if name not in birthdays_dict:
        birthdays_dict[name] = []
    birthdays_dict[name].append({
        'day': day,
        'month': month,
        'mail': mail
    })

letters = []
with open("letter_1.txt", 'r') as letter:
    letters.append(letter.read())

with open("letter_2.txt", 'r') as letter:
    letters.append(letter.read())

with open("letter_3.txt", 'r') as letter:
    letters.append(letter.read())
birthday_letter = random.choice(letters)

now = dt.datetime.now()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    for name, birthday_data in birthdays_dict.items():
        for data in birthday_data:
            mail = data['mail']
            day = data['day']
            month = data['month']
            if now.day == day and now.month == month:
                connection.sendmail(
                    from_addr=my_mail,
                    to_addrs=mail,
                    msg=f"Subject: Happy Birthday!!!\n\n{birthday_letter.replace('[NAME]', name)}")
