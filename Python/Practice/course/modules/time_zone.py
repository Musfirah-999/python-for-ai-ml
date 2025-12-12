import datetime
now_utc = datetime.datetime.now(datetime.timezone.utc)
print(f"Current UTC time: {now_utc}")


new_timezone = datetime.timezone(datetime.timedelta(hours=5))
new_est = datetime.datetime.now(new_timezone)
print(f"Time in EST: {new_est}")