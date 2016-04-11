#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os, datetime

with open('/private/tmp/forecast.io_weather.json', 'r') as json_file:
    data = json.load(json_file)

strSunrise = str(data["daily"]["data"][0]["sunriseTime"])
strSunset = str(data["daily"]["data"][0]["sunsetTime"])

strSunrise = str(datetime.datetime.fromtimestamp(int(strSunrise)).strftime('%H:%M:%S'))
strSunset = str(datetime.datetime.fromtimestamp(int(strSunset)).strftime('%H:%M:%S'))

print "Sunrise: " + strSunrise
print "Sunset: " + strSunset