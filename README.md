This project is based on the code from KM6LYW
I wanted to send my weather data from WeatherUnderGround API to APRS via DireWolf
The code and process assume you are comfortable with modifying files in Linux/Debian
You will need to get an API key for your Weather Underground PWS (https://www.wunderground.com/member/api-keys)

Place both aprs-send-weather.sh and weather.py into /usr/local/bin (setting file permissions "chmod 777 filename"

Changes need to be customized code/scripts for your station

In weather.py
  Change Location to your station's location
  In the URL, update the stationId and APIKey (test by going to the URL in a web browser)

  Test using the command 'python weather.py'

In aprs-send-weather.sh
  Update the USER and PASS with your APRS station's username and password (https://apps.magicbug.co.uk/passcode/ to generate a password for your station)

  Test by using the command './aprs-send-weather.sh'

Once everything works, add aprs-send-weather.sh to your cron so it runs on a schedule.
  crontab -e
  0 * * * * /usr/local/bin/aprs-send-weather.sh
