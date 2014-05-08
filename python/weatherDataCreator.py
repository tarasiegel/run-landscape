import urllib2
import json
from datetime import *
import sys
import string
#from datetime import date

weatherDict = {}
minTemp = {}
maxTemp = {}
rain = {}
snow = {}
maxHumidity = {}
location = {}


def getURL(date, loc):
	location = '';
	if loc == 'phl':
		location = "PA/Philadelphia"
	elif loc == "sj":
		location = "CA/San_Jose"
	elif loc == "psj":
		location = "FL/Port_St_Joe"
	elif loc == "cc":
		location = "FL/Cooper_City"
	elif loc == 'ny':
		location = "NY/New_York"
	elif loc == "mn":
		location = "MN/Minneapolis"
	elif loc == "ast":
		location = "TX/Austin"
	elif loc == "pr":
		location = "PR/San_Juan"
	return "http://api.wunderground.com/api/4071cf6e7fef262b/history_" + str(date) + "/q/" + str(location) + ".json"

def daterange(startDate, endDate):
	for n in range(int ((endDate - startDate).days)):
		yield startDate + timedelta(n)

def getWeatherBetweenTwoDates(date1, date2, loc):
	for singleDate in daterange(date1, date2):
		#print singleDate.strftime("%Y%m%d")
		getWeatherData(singleDate.strftime("%Y%m%d"), loc)



def getWeatherData(date, loc):	
	f = urllib2.urlopen(getURL(date,loc))
	json_string = f.read()
	parsed_json = json.loads(json_string)
	dailySum = parsed_json['history']['dailysummary'][0]
	weatherDict[date] = {'Location': loc, 'MeanTemp': dailySum['meantempi'], 'MinTemp': dailySum['mintempi'], 'MaxTemp': dailySum['maxtempi'], 'Rain': dailySum['precipm'], 'Snow': dailySum['snowfallm'], 'Humidity': dailySum['maxhumidity']}
	print "Date: " + date + " Location: " + loc
	#temp_f = parsed_json['current_observation']['temp_f']
	#print "mean temp :" + meanTemp
	#print "min temp :" + minTemp
	#print "max temp :" + maxTemp
	#print "humidity :" + maxHumidity
	f.close()

if __name__ == '__main__':
    #topicFile = sys.argv[1]
    getWeatherBetweenTwoDates(date(2012,5,31), date(2012,7,5), "ny")
    getWeatherBetweenTwoDates(date(2012,7,9), date(2012,8,12), "ny")
    getWeatherBetweenTwoDates(date(2012,10,20), date(2012,10,22), "ny")
    getWeatherBetweenTwoDates(date(2013,5,18), date(2013,5,31), "sj")
    getWeatherBetweenTwoDates(date(2013,6,4), date(2013,8,17), "sj")
    getWeatherBetweenTwoDates(date(2013,10,15), date(2013,10,16), "sj")
    getWeatherBetweenTwoDates(date(2013,3,3), date(2013,3,10), "psj")
    getWeatherBetweenTwoDates(date(2013,3,13), date(2013,3,17), "psj")
    getWeatherBetweenTwoDates(date(2013,10,2), date(2013,10,6), "mn")
    getWeatherBetweenTwoDates(date(2013,11,14), date(2013,11,17), "ast")
    getWeatherBetweenTwoDates(date(2013,12,22), date(2013,12,30), "pr")
    getWeatherBetweenTwoDates(date(2012,5,1), date(2012,5,31), "cc")
    getWeatherBetweenTwoDates(date(2012,8,13), date(2012,8,30), "cc")
    getWeatherBetweenTwoDates(date(2012,11,21), date(2012,11,26), "cc")
    getWeatherBetweenTwoDates(date(2012,12,19), date(2013,1,6), "cc")
    getWeatherBetweenTwoDates(date(2013,5,9), date(2013,5,18), "cc")
    getWeatherBetweenTwoDates(date(2013,6,1), date(2013,6,4), "cc")
    getWeatherBetweenTwoDates(date(2013,8,18), date(2013,8,26), "cc")
    getWeatherBetweenTwoDates(date(2013,12,30), date(2014,1,12), "cc")
    getWeatherBetweenTwoDates(date(2014,3,8), date(2014,3,13), "cc")
    getWeatherBetweenTwoDates(date(2012,7,6), date(2012,7,9), "phl")
    getWeatherBetweenTwoDates(date(2012,8,30), date(2012,10,20), "phl")
    getWeatherBetweenTwoDates(date(2012,10,23), date(2012,11,21), "phl")
    getWeatherBetweenTwoDates(date(2012,11,26), date(2012,12,20), "phl")
    getWeatherBetweenTwoDates(date(2013,1,6), date(2013,3,3), "phl")
    getWeatherBetweenTwoDates(date(2013,3,10), date(2013,5,9), "phl")
    getWeatherBetweenTwoDates(date(2013,8,26), date(2013,10,2), "phl")
    getWeatherBetweenTwoDates(date(2013,10,18), date(2013,11,14), "phl")
    getWeatherBetweenTwoDates(date(2013,11,17), date(2013,12,22), "phl")
    getWeatherBetweenTwoDates(date(2014,1,12), date(2014,3,9), "phl")
    getWeatherBetweenTwoDates(date(2014,4,22), date(2014,4,30), "phl")
    saved = sys.stdout
    f = file('weatherData.json', 'wb')
    sys.stdout = f
    print json.dumps(weatherDict)
    sys.stdout = saved
    f.close()

    #print sorted(location)


    #getWeatherData(20140421, 'Philly')