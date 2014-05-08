import urllib2
import json
from datetime import *
import sys
import string
#from datetime import date

weatherDict = {}


def getLoc(loc):
	location = '';
	if loc == 'phl':
		location = "Philadelphia, PA"
	elif loc == "sj":
		location = "San Jose, CA"
	elif loc == "psj":
		location = "Port St Joe, FL"
	elif loc == "cc":
		location = "Cooper City, FL"
	elif loc == 'ny':
		location = "New York, NY"
	elif loc == "mn":
		location = "Minneapolis, MN"
	elif loc == "ast":
		location = "Austin, TX"
	elif loc == "pr":
		location = "The Caribbean"
	return location

def daterange(startDate, endDate):
	for n in range(int ((endDate - startDate).days)):
		yield startDate + timedelta(n)

def getWeatherBetweenTwoDates(date1, date2, loc, info):
	for singleDate in daterange(date1, date2):
		#print singleDate.strftime("%Y%m%d")
		getWeatherData(singleDate.strftime("%m/%d/%Y"), loc, info)



def getWeatherData(date, loc, info):	
	location = getLoc(loc)
	# json_string = f.read()
	# parsed_json = json.loads(json_string)
	# dailySum = parsed_json['history']['dailysummary'][0]
	weatherDict[date] = {'Location': location, 'Story': info}

	print "Date: " + date + " Location: " + loc
	#temp_f = parsed_json['current_observation']['temp_f']
	#print "mean temp :" + meanTemp
	#print "min temp :" + minTemp
	#print "max temp :" + maxTemp
	#print "humidity :" + maxHumidity
	#f.close()

if __name__ == '__main__':
    #topicFile = sys.argv[1]
    getWeatherBetweenTwoDates(date(2012,5,31), date(2012,7,5), "ny", "Interning at NBCUniversal in NYC for the summer")
    getWeatherBetweenTwoDates(date(2012,7,9), date(2012,8,12), "ny", "Interning at NBCUniversal in NYC for the summer")
    getWeatherBetweenTwoDates(date(2012,10,20), date(2012,10,22), "ny", "Visited an old friend over Fall Break")
    getWeatherBetweenTwoDates(date(2013,5,18), date(2013,5,31), "sj", "Was interning at Google/Youtube in San Jose / Mountain View for the summer")
    getWeatherBetweenTwoDates(date(2013,6,4), date(2013,8,17), "sj", "Was interning at Google/Youtube in San Jose / Mountain View for the summer")
    getWeatherBetweenTwoDates(date(2013,10,15), date(2013,10,16), "sj", "Came back to the Bay Area for a few days for a job interview and visit a friend at Standford")
    getWeatherBetweenTwoDates(date(2013,3,3), date(2013,3,10), "psj", "Spring break with friends from Theta Tau, the professional engineering fraternity I am a part of. Basically was a week of celebrating my birthday")
    getWeatherBetweenTwoDates(date(2013,3,13), date(2013,3,17), "psj", "Spring break with my family")
    getWeatherBetweenTwoDates(date(2013,10,2), date(2013,10,6), "mn", "Went to the Grace Hooper Conference for Women in Computing.  Saw friends from this past summer and networked a lot")
    getWeatherBetweenTwoDates(date(2013,11,14), date(2013,11,17), "ast", "Came to Austin for a job interview, spent most of the time with one of my good friends who lives in Austin.  Had to leave for the Philly Half marathon the next day")
    getWeatherBetweenTwoDates(date(2013,12,22), date(2013,12,30), "pr", "Family vacation for Winter Break.  We went on a cruise in the caribbean to Puerto Rico, St. Kitts, St. Thomas, Curacao, and Aruba")
    getWeatherBetweenTwoDates(date(2012,5,1), date(2012,5,31), "cc", "Was home after completing sophomore year of college before going up to NYC for my internship")
    getWeatherBetweenTwoDates(date(2012,8,13), date(2012,8,30), "cc", "Home for a bit before starting junior year of college")
    getWeatherBetweenTwoDates(date(2012,11,21), date(2012,11,26), "cc", "Traveled home for thanksgiving with the family")
    getWeatherBetweenTwoDates(date(2012,12,19), date(2013,1,6), "cc", "Home for winter break. Didnt really do much")
    getWeatherBetweenTwoDates(date(2013,5,9), date(2013,5,18), "cc", "Home for a week before starting my internship in California")
    getWeatherBetweenTwoDates(date(2013,6,1), date(2013,6,4), "cc", "Came home for a few days for my brother high school graduation")
    getWeatherBetweenTwoDates(date(2013,8,18), date(2013,8,26), "cc", "Home for a week between finishing my internship at Google and starting Senior year of college")
    getWeatherBetweenTwoDates(date(2013,12,30), date(2014,1,12), "cc", "Home for the second half of winter break")
    getWeatherBetweenTwoDates(date(2014,3,8), date(2014,3,13), "cc", "Spent some of spring break home Senior year")
    getWeatherBetweenTwoDates(date(2012,7,6), date(2012,7,9), "phl", "Briefly came to Philly to do the Color Run")
    getWeatherBetweenTwoDates(date(2012,8,30), date(2012,10,20), "phl", "Start of junior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2012,10,23), date(2012,11,21), "phl", "Junior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2012,11,26), date(2012,12,20), "phl", "Junior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2013,1,6), date(2013,3,3), "phl", "Junior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2013,3,10), date(2013,5,9), "phl", "Junior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2013,8,26), date(2013,10,2), "phl", "Senior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2013,10,18), date(2013,11,14), "phl", "Senior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2013,11,17), date(2013,12,22), "phl", "Senior year of college at University of Pennsylvania")
    getWeatherBetweenTwoDates(date(2014,1,12), date(2014,3,9), "phl", "Senior year of college at University of Pennsylvania.  It was a particularly cold winter")
    getWeatherBetweenTwoDates(date(2014,3,17), date(2014,4,30), "phl", "Senior year of college at University of Pennsylvania")
    # saved = sys.stdout
    # f = file('storyData.json', 'wb')
    # sys.stdout = f
    # print json.dumps(weatherDict)
    # sys.stdout = saved
    # f.close()

    with open('storyData.json', 'w') as outfile:
        json.dump(weatherDict, outfile)

    #print sorted(location)


    #getWeatherData(20140421, 'Philly')