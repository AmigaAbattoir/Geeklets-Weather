#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

with open('/private/tmp/forecast.io_weather.json', 'r') as json_file:
    data = json.load(json_file)

realTemp = round(data["currently"]["temperature"],1)
feelsLikeTemp = round(data["currently"]["apparentTemperature"],1)

strSummary=str(data["currently"]["summary"])
strTemp=str(round(data["currently"]["apparentTemperature"],1))
if(abs(realTemp-feelsLikeTemp)>5):
	print 'Feels like ' + strTemp + '°F'
