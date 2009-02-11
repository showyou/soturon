def toDate(date):
	import time,datetime
	dates = time.strptime(date,"%a %b %d %H:%M:%S +0000 %Y")
	dt = datetime.datetime(dates[0],dates[1],dates[2],dates[3],dates[4],dates[5],dates[6])+datetime.timedelta(hours=9)
	return dt

if __name__ == "__main__":
	import datetime
	date = "Sat Dec 22 01:07:16 +0000 2007"
	print toDate(date)
	print datetime.datetime.today()
	
