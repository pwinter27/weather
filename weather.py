#!/usr/bin/python
from pprint import pprint
import requests
import sys
import json 
import weatherapikey

def weatherCity(city,country="US"):
    print "Using country ", country
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="+city+","+country+"&units=imperial&appid="+weatherapikey.apikey())
    datalist = r.json()['list']  
    for x in datalist[0:20]: 
        print x['dt_txt'] + ' - ' + str(x['main']['temp']) +' ('+ x['weather'][0]['main']+")"


def printUsage():
    print "usage: ./weather.py cityname"

if __name__ == "__main__":
    if(len(sys.argv) < 2 or len(sys.argv) > 3 ):
        printUsage()
        exit()

    city = sys.argv[1]
    if len(sys.argv) > 2:
        weatherCity(city,sys.arg[2])
    else: 
        weatherCity(city)

