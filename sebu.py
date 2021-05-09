import datetime
from dateutil import parser
from datetime import datetime

def pay_calculator():
    
    date_time_started = parser.parse(input('Please input the date and time started. Format yyyy-mm-dd HH:MM : \n '))
    date_time_ended = parser.parse(input('Please input the time started. Format HH:MM: \n '))
  

    # calculations

    duration_date =  date_time_ended - date_time_started

    if duration_date:
        money_earned = duration_date * 5
        print(f"money earend : {duration_date}")
        print(duration_date)
    else:
        print("duration less than 0 hence no income")


pay_calculator()

    
