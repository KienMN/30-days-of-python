import datetime

today = datetime.date.today()
date_text = '{today.day}/{today.month}/{today.year}'.format(today = today)

print(date_text)