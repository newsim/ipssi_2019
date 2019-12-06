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
    return text



if __name__ == '__main__':
   print(noel(str(sys.argv[1])) )