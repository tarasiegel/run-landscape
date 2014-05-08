
import sys
import json
import csv
from decimal import *
import unicodedata


humidityList = []
minTempList = []
maxTempList = []
meanTempList = []
snowList = []
rainList = []
locationList = []

firstLine = []

def filterOutWords(jsonFile):
	obj = json.loads(open(jsonFile).read())
	for date in obj:
		for feature in obj[date]:
			row = []
			row.append(feature.encode('ascii','ignore'))
			if obj[date][feature].encode('ascii','ignore') == "T":
				row.append("0.0")
			else:
				row.append(obj[date][feature].encode('ascii','ignore'))
			row.append(date.encode('ascii','ignore'))
			if feature.encode('ascii','ignore') == "Humidity":
				humidityList.append(row)
			elif feature.encode('ascii','ignore') == "MinTemp":
				minTempList.append(row)
			elif feature.encode('ascii','ignore') == "MaxTemp":
				maxTempList.append(row)
			elif feature.encode('ascii','ignore') == "MeanTemp":
				meanTempList.append(row)
			elif feature.encode('ascii','ignore') == "Snow":
				snowList.append(row)
			elif feature.encode('ascii','ignore') == "Rain":
				rainList.append(row)
			elif feature.encode('ascii','ignore') == "Location":
				locationList.append(row)
	# with open('jsonFile') as f:
	# 	for

def writeFile():
	with open('weatherDataFinal5.csv', 'wb') as output:
		outputWriter = csv.writer(output)
		firstRow = []
		firstRow.append("key")
		firstRow.append("value")
		firstRow.append("date")
		outputWriter.writerow(firstRow)	
		for entry in sorted(humidityList, key=lambda variable: variable[2]):
			outputWriter.writerow(entry)
		for entry in sorted(minTempList, key=lambda variable: variable[2]):
			outputWriter.writerow(entry)
		for entry in sorted(maxTempList, key=lambda variable: variable[2]):
			outputWriter.writerow(entry)
		for entry in sorted(meanTempList, key=lambda variable: variable[2]):
			outputWriter.writerow(entry)


if __name__ == '__main__':
    jsonFile = sys.argv[1]
    filterOutWords(jsonFile)
    writeFile()