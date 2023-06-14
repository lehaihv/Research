from datetime import datetime
from geopy import geocoders
from tzwhere import tzwhere
from pytz import timezone

g = geocoders.GoogleV3()
tz = tzwhere.tzwhere()
locationList = ["Sackville, Canada", "Romania", "Mannheim, Germany", "New Delhi, India", "Trier, Germany", "Basel, Switzerland", "Bruxelles/Brussel, Belgium"]

for location in locationList:
	place, (lat, lng) = g.geocode(location)
	timeZoneStr = tz.tzNameAt(lat, lng)
	timeZoneObj = timezone(timeZoneStr)
	now_time = datetime.now(timezoneObj)
	print(now_time)
