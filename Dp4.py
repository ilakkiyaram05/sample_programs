from datetime import datetime

date1 = datetime.strptime("06-06-2011", "%d-%m-%Y")

date2 = datetime.strptime("06-07-2011", "%d-%m-%Y")

months = (date2.year - date1.year) * 12 + (date2.month - date1.month)

if months == 1 and date1.day == date2.day:
    print("Exactly 1 month apart")

elif (date2 - date1).days < 30:
    print("Less than 1 month apart")

else:
    print("More than 1 month apart")
