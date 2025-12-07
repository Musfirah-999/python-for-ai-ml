import datetime

# now = datetime.datetime.now()
# formatted_now = now.strftime("%d %m %y   %Y- %H hour, %M min, %S sec")
# print(now)
# print(formatted_now)

# date_string = "2025-12-07  14:53:30"
# date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(date)
# print(type(date))


# now = datetime.datetime.now()
# five_days = datetime.timedelta(days=5)
# new_date = now+five_days
# print("Now:",now)
# print("New date after adding five days:",new_date)


# new_date = now- five_days
# print("New date after subracting five days:",new_date)


date1 = datetime.datetime(2005,10,14)
now = datetime.datetime.now()
diff = now - date1
print(f"My age is :{diff} ")
