# Practicing inheritance with date functions
# Class will inherit properties from another class called date

from datetime import date
import time

FORMAT_DD_MM_YYYY = "dd.mm.yyyy"

class Date():
    def get_date(self):
        today = date.today()
        # format in order to get month abbreviation, day and year
        d2 = today.strftime("%b-%d-%Y")
        print("Today's date:", d2)

class Time(Date):
    now = datetime.now()

    def get_time(self):
        print("now =", now)

# Creating an instance from Date
dt = Date()
dt.get_date() # Accessing get_date method from Date
print("--------")

# Creating an instance from Time
tm = Time()
tm.get_time() # Accessing the get_time method from Time
tm.get_date() # Accesing the get_date method from the parent class Date