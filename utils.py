from datetime import datetime as dt
from datetime import date

def now(fmt = "%H:%M:%S"):
    return dt.now().strftime(fmt)

def today(fmt = "%d/%m/%Y"):
    return date.today().strftime(fmt)