from datetime import datetime
from pytz import timezone

fmt = "%H%M"

# Current time in London
now_london = datetime.now(timezone('UTC'))
london_time = int(now_london.strftime(fmt))

# Convert to US/Pacific time zone
now_portland = now_london.astimezone(timezone('US/Pacific'))
portland_time = int(now_portland.strftime(fmt))

# Convert to New York time zone
now_new_york = now_portland.astimezone(timezone('US/Eastern'))
new_york_time = int(now_new_york.strftime(fmt))

#Check New Yorks Office
if new_york_time >= 900 and new_york_time <= 2100:
    print "New York is open"
else:
    print "New York is closed"

#Check Londons Office
if london_time >= 900 and london_time <= 2100:
    print "London is open"
else:
    print "London is closed"

#Check Portlands Office
if portland_time >= 900 and portland_time <= 2100:
    print "Portland is open"
else:
    print "Portland is closed"
