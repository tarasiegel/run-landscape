import sys
import json
import csv
from decimal import *
import unicodedata
import collections

distanceList = []

firstLine = []

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def getAvgTime(time, dist):
    timesInSeconds = []
    pieces = time.split(':')
    print pieces
    hrs =  float(pieces[0])
    mins = float(pieces[1])
    secs = float(pieces[2])
    timesInSeconds = hrs * 60 * 60
    timesInSeconds += mins * 60
    timesInSeconds += secs
    print timesInSeconds
    avg = round((float(timesInSeconds) / dist), 3)
    return avg

def getLength(dist):
	return float(dist)/1.61

def filterOutWords(jsonFile):
	obj = json.loads(open(jsonFile).read())
	obj = convert(obj)
	#print obj

	for date in obj.get('data'):
		newObj = date.get('metricSummary')
		row = []
		dist = getLength(newObj.get('distance'))
		row.append(getAvgTime(newObj.get('duration'), dist))
		row.append(dist)
		row.append(date.get('startTime')[0:10])
		distanceList.append(row)

def writeFile():
	with open('runningData2.csv', 'wb') as output:
		outputWriter = csv.writer(output)
		firstRow = []
		firstRow.append("Pace")
		firstRow.append("Distance")
		firstRow.append("Date")
		outputWriter.writerow(firstRow)	
		for entry in sorted(distanceList, key=lambda variable: variable[2]):
			outputWriter.writerow(entry)

if __name__ == '__main__':
    jsonFile = sys.argv[1]
    filterOutWords(jsonFile)
    writeFile()
