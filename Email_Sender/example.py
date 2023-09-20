import smtplib
import datetime as dt
import random

my_email = "mazur.leonardo@outlook.com"
password = "jsukhnvfrezkwlib"

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 0:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        phrase = random.choice(data)
        with smtplib.SMTP("smtp.outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="leonardo.mazur@icloud.com",
                msg=f"Subject:Motivational Phrase\n\n{phrase}"
            )
else:
    print("Weekend")


