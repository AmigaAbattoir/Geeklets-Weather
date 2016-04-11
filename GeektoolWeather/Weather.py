#!/usr/bin/python
#
# Gets Forecast.io's data and saves it.
import json
import urllib
import shutil
import os

# Your forecast.io APIKEY
api = ""
# Location
latitude = ""
longitude = ""
# Which style of icons to use
whichStyle = "yahoo-weather"

# Make API call for data
json_data=urllib.urlopen("https://api.forecast.io/forecast/" + api + "/" + latitude + "," + longitude)
data=json.load(json_data)

# Write JSON file to temp, so we can use it again for other lines of text
with open('/private/tmp/forecast.io_weather.json', 'w') as outfile:
  json.dump(data, outfile)

# Get current time, sunrise and sunset to help determine which icons
intCurrentTime = int(data["currently"]["time"])
intSunrise = int(data["daily"]["data"][0]["sunriseTime"])
intSunset = int(data["daily"]["data"][0]["sunsetTime"])

timeOfDay = "d"
if(intCurrentTime<intSunrise or intCurrentTime>intSunset):
	timeOfDay = "n"

# Assume that 44 is the normal.
whichWeather = "44"

# Which style of icons to use
#whichStyle = "yahoo-weather"
whichStyle = "sketchy-weather-red"

strIcon = str(data["currently"]["icon"])

# Use Forecast.io's "icon" to determine the image
if(strIcon=="clear-day"):
	whichWeather = "32"
elif(strIcon=="clear-night"):
	whichWeather = "31"
elif(strIcon=="rain"):
	whichWeather = "11"
elif(strIcon=="snow"):
	whichWeather = "13"
elif(strIcon=="sleet"):
	whichWeather = "18"
elif(strIcon=="wind"):
	whichWeather = "24"
elif(strIcon=="fog"):
	whichWeather = "20"
elif(strIcon=="cloudy"):
	whichWeather = "26"
elif(strIcon=="partly-cloudy-day"):
	whichWeather = "30"
elif(strIcon=="partly-cloudy-night"):
	whichWeather = "29"

strCurrently = str(data["currently"]["summary"])

# However, if we have a summary that matches one of these, let's use it instead!
if(strCurrently =="Tornado"):
	whichWeather = "0"
elif(strCurrently =="Tropical Storm"):
	whichWeather = "1"
elif(strCurrently =="Hurricane"):
	whichWeather = "2"
elif(strCurrently =="Severe Thunderstorms"):
	whichWeather = "3"
elif(strCurrently =="Thunderstorms"):
	whichWeather = "4"
elif(strCurrently =="Mixed Rain and Snow"):
	whichWeather = "5"
elif(strCurrently =="Mixed Rain and Sleet"):
	whichWeather = "6"
elif(strCurrently =="Mixed Snow and Sleet"):
	whichWeather = "7"
elif(strCurrently =="Freezing Drizzle"):
	whichWeather = "8"
elif(strCurrently =="Drizzle"):
	whichWeather = "9"
elif(strCurrently =="Freezing Rain"):
	whichWeather = "10"
elif(strCurrently =="Showers"):
	whichWeather = "11"
elif(strCurrently =="Showers"):
	whichWeather = "12"
elif(strCurrently =="Snow Flurries"):
	whichWeather = "13"
elif(strCurrently =="Light Snow Showers"):
	whichWeather = "14"
elif(strCurrently =="Blowing Snow"):
	whichWeather = "15"
elif(strCurrently =="Snow"):
	whichWeather = "16"
elif(strCurrently =="Hail"):
	whichWeather = "17"
elif(strCurrently =="Sleet"):
	whichWeather = "18"
elif(strCurrently =="Dust"):
	whichWeather = "19"
elif(strCurrently =="Foggy" or strCurrently =="Fog"):
	whichWeather = "20"
elif(strCurrently =="Haze" or strCurrently =="Hazy"):
	whichWeather = "21"
elif(strCurrently =="Smoky"):
	whichWeather = "22"
elif(strCurrently =="Blustery"):
	whichWeather = "23"
elif(strCurrently =="Windy"):
	whichWeather = "24"
elif(strCurrently =="Cold"):
	whichWeather = "25"
elif(strCurrently =="Cloudy"):
	whichWeather = "26"
elif(strCurrently =="Mostly Cloudy" and timeOfDay=="n"):
	whichWeather = "27"
elif(strCurrently =="Mostly Cloudy" and timeOfDay=="d"):
	whichWeather = "28"
elif(strCurrently =="Partly Cloudy" and timeOfDay=="n"):
	whichWeather = "29"
elif(strCurrently =="Partly Cloudy" and timeOfDay=="d"):
	whichWeather = "30"
elif(strCurrently =="Clear" and timeOfDay=="n"):
	whichWeather = "31"
elif(strCurrently =="Sunny"):
	whichWeather = "32"
elif(strCurrently =="Fair" and timeOfDay=="n"):
	whichWeather = "33"
elif(strCurrently =="Fair" and timeOfDay=="d"):
	whichWeather = "34"
elif(strCurrently =="Mixed Rain and Hail"):
	whichWeather = "35"
elif(strCurrently =="Hot"):
	whichWeather = "36"
elif(strCurrently =="Isolated Thunderstrom"):
	whichWeather = "37"
elif(strCurrently =="Scattered Thunderstorms"):
	whichWeather = "38"
elif(strCurrently =="Scattered Thunderstorms"):
	whichWeather = "39"
elif(strCurrently =="Scattered Showers"):
	whichWeather = "40"
elif(strCurrently =="Heavy Snow"):
	whichWeather = "41"
elif(strCurrently =="Scattered Snow Showers"):
	whichWeather = "42"
elif(strCurrently =="Heavy Snow"):
	whichWeather = "43"
elif(strCurrently =="Partly Cloudy"):
	whichWeather = "44"
elif(strCurrently =="Thundershowers"):
	whichWeather = "45"
elif(strCurrently =="Snow Showers"):
	whichWeather = "46"
elif(strCurrently =="Isolated Thundershowers"):
	whichWeather = "47"
elif(strCurrently =="Something else"):
	whichWeather = "48"

# Copy image from location of GeekWeather icons to the temp.
shutil.copyfile(os.path.expanduser('~') + "/Library/Application Support/GeekWeatherImages/" + whichStyle + "/" + whichWeather + timeOfDay + ".png","/private/tmp/weather.png");
