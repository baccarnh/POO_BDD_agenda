import calendar
from calendar import month
import time
import calendar
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
currentyear = datetime.now().year
currentmonth = datetime.now().month

print(calendar.month(currentyear, currentmonth))