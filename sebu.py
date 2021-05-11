import datetime
import csv

def pay_calculator():

    ## outputting the title of the system
    print("Hourly Calculator\n")

    ## take input for the date started in a string format yyyy-mm-dd
    date_started = str(input('Please input the date started. Format yyyy-mm-dd : '))

    ## take input for the time started in a string format hh:mm
    ## split ':' from the time started to get a list of two items
    time_started = input('specify time (24 hrs)started in HH:MM format: ').split(":")

    ## take input for the date ended in a string format yyyy-mm-dd
    date_ended = str(input('Please input the date ended. Format yyyy-mm-dd: '))

    ## take input for the time ended in a string format hh:mm
    ## split ':' from the time ended to get a list of two items
    time_ended = input('specify time (24 hrs) ended in HH:MM format: ').split(":")

    
    ## join ':' to time started and time ended
    ## this reverts the splitted time to correct format hh:mm
    ts = (":").join(time_started)
    te = (":").join(time_ended)
      

    ## calculations

    ## convert the string list [hh, mm] into int data type
    ## do it for both time_started and time ended
    ## assign both to time_s and time_e variables respectively
    time_s = [int(i) for i in time_started ]

    time_e = [int(i) for i in time_ended]

    ## convert hours of both list (ended and started) into minutes
    ## this is done by accessing zero index of each list
    ## multiply it by 60 and add it to the corresponding minute
    ## do for both respectively
    ## initial list [hh, mm] now becomes list [mm, mm]
    a = 60*time_s[0] + time_s[1]
    b = 60*time_e[0] + time_e[1]
    
    
    ## difference in time (ended - started)
    ans = b - a

    ## the actual hours worked
    actual_hours = ans / 60

    ## initialize the hourly pay variable with 5 dollars
    hourly_pay = 5

    ## check if diff is positiive then calculate for the money earned
    ## else print error
    if ans > 0:
        val = ans/60
        money_earned = val* hourly_pay

        print("the hourly money earned: GH$", money_earned, "cedis")

        print("the hours worked: ", actual_hours, 'hours')
        
        ## header and data of the csv file
        header = ['Date Started', 'Time Started', 'Date Ended', 'Time Ended', 'Amount Earned', 'Hours Worked']
        data = [date_started , ts, date_ended, te, money_earned, actual_hours]
        
        ## write to the csv file
        with open('C:/Users/Big-Max/Desktop/P/SEBU/money.csv', 'w', newline='',encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

            f.close()
                  
    else:
        print("hours cannot be less than zero")


## calling the function to execute
pay_calculator()

    
