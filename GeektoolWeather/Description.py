#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

with open('/private/tmp/forecast.io_weather.json', 'r') as json_file:
    data = json.load(json_file)

strSummary=str(data["currently"]["summary"])
strTemp=str(round(data["currently"]["temperature"],1))

print strSummary + ', ' + strTemp + '°F'
