import datetime as dt

current_date_time=dt.datetime.now() #getting current date and time from system
print(current_date_time)

current_hour=current_date_time.hour #getting current hour from current date time

print(current_hour)
if current_hour<12:
    print('Good Morning')
elif current_hour<17:
    print('Good afternoon')
else:
    print('Good evening')
    
