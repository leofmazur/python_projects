import smtplib
import datetime as dt
import pandas as pd
import random
import os

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

MY_EMAIL = "mazur.leonardo@outlook.com"
PASSWORD = "jsukhnvfrezkwlib"

data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")


if day == birthdays[0]["day"] and month == birthdays[0]["month"]:
    letter = random.choice(os.listdir("letter_templates/"))
    with open(f"letter_templates/{letter}", "rt") as data_file:
        data = data_file.read()
        data = data.replace("[NAME]", birthdays[0]["name"])

    with smtplib.SMTP("smtp.outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="leonardo.mazur@icloud.com",
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{data}")
