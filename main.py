import datetime
import bday_messages  

today = datetime.date.today()

next_birthday = datetime.date(2024, 12, 19)

days_until_birthday = (next_birthday - today).days

if days_until_birthday == 0:
    print(random.choice(bday_messages.bday_messages()))
else:
    print('My next birthday is ' + str(days_until_birthday) + ' days away!')