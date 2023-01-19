
import datetime as dt
import time


#Check for market open
def open_market():
    dayOfWeek = dt.date.today()
    todaysDate = dt.datetime.now()
    time_now = dt.datetime.now().time()
    market_open = dt.time(8,30,0)
    market_close = dt.time(14,59,0)

    market = True

    if dayOfWeek.weekday() < 5:
        if time_now > market_open and time_now < market_close:
            market = True
        else:
            print("### market is closed")

        return(market)
    else:
            print("### market is closed")
    return(market)
