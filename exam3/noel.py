
#!/usr/bin/python3
import calendar
import os
import datetime
import sys
from datetime import timedelta
from datetime import datetime

def noel(date):
    date = sys.argv[1]
    date = datetime.strptime(date, "%d-%m-%Y")
    d =  date - datetime.today()
    text = str(d.days) + ' days before christmas'  

    # create a plain text calendar

    year  = date.year
    month = date.month
    # calendar of month
    cd = calendar.month(year, month)
    res = text + "\n" + cd
    return res




if __name__ == '__main__':
    date = sys.argv[1]
    print(noel( str(date)) )