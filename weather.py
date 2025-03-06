import requests
import json
import pprint
from datetime import datetime, timezone

Location = ("4105.46N/08120.14W")

T = datetime.now(timezone.utc)
Now = (T.strftime("%H"))
Now += (T.strftime("%M"))
Now += (T.strftime("%S"))

url = 'https://api.weather.com/v2/pws/observations/current?stationId=YOURSTATIONHERE&format=json&units=e&apiKey=YOURKEYHERE'
response = requests.get(url)
if response.status_code == 200:
	data = json.loads(response.text)
	wind_direction = data['observations'][0]['winddir']
	wind_speed = data['observations'][0]['imperial']['windSpeed']
	gust = data['observations'][0]['imperial']['windGust']
	temp = data['observations'][0]['imperial']['temp']
	rain_lastH = data['observations'][0]['imperial']['precipRate']
	rain_24 = ('000')
	rain_midnight = data['observations'][0]['imperial']['precipTotal']
	humidity = data['observations'][0]['humidity']
	pressure = data['observations'][0]['imperial']['pressure']

	rain_lastH = (rain_lastH * 100)
	rain_midnight = (rain_midnight * 100)
	pressure = (pressure * 33.8637526)
	pressure = round(pressure,1)

	wind_direction = f"{wind_direction:03}"
	wind_speed = f"{wind_speed:03}"
	gust = f"{gust:03}"
	temp = f"{temp:03}"
	rain_lastH = f"{rain_lastH:03}"
	rain_24 = f"{rain_24:03}"
	rain_midnight = f"{rain_midnight:03}"
	humidity = f"{humidity:02}"
	pressure = f"{pressure:04}"


	print(f"Wind Direction: {wind_direction}")
	print(f"Wind Speed: {wind_speed}")
	print(f"Gust: {gust}")
	print(f"Temp: {temp}")
	print(f"Rain Hour: {rain_lastH}")
	print(f"Rain 24: {rain_24}")
	print(f"Rain Midnight: {rain_midnight}")
	print(f"Humidity: {humidity}")
	print(f"Pressure: {pressure}")
	print(f"Time: {Now}")


	Packet = "/" + Now + "z"
	Packet += Location
	Packet += "_" + wind_direction
	Packet += "/...g" + gust
	Packet += "t" + temp
	Packet += "r" + rain_lastH
	Packet += "h" + humidity
	Packet += "b" + pressure

	print(f"Packet: {Packet}")	

	File = open("aprs.pkt", "w")
	File.write(Packet)
	File.close()

else:
	print(f"Error: {response.status_code}")
