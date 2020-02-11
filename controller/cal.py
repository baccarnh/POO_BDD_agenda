import calendar
from calendar import month
import time
import calendar
import locale
from datetime import datetime
def today():
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    print(f"Nous sommes le : {datetime.today().strftime('%A %d %B %Y')}")


def next_month():
    currentyear = datetime.now().year
    currentmonth = datetime.now().month
    if currentmonth<12:
        currentmonth+=1
    else:
        currentmonth=1
        currentyear+=1
    print(calendar.month(currentyear, currentmonth))

def last_month():
    currentyear = datetime.now().year
    currentmonth = datetime.now().month
    if currentmonth>1:
        currentmonth-=1
    else:
        currentmonth=12
        currentyear-=1
    print(calendar.month(currentyear, currentmonth))


