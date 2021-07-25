# openauto
Update openauto config file with sunrise and sunset times

This set of python files is designed to be installed on the OpenAutoPro 
raspberry pi in my car.  

## How it works
`anacron` needs to be installed via apt-get.  Anacron will ensure that things
get run once daily, weekly, monthly etc.

So `anacron` will run the `main.py` script once a day (trying every hour)

`main.py` needs the location of the config file which is at
`/home/pi/.openauto/config/openauto_system.ini`

`main.py` first calls `get_sunrise_sunset.py` to scrape sunset and sunrise times
Auckland from https://www.sunrise-and-sunset.com/en/sun/new-zealand/auckland

Then `main.py` calls `update_config_file.py` to load the config file,
update the sunset and sunrise times in the `[DayNight]` section and 
save the file.

The `openauto_system.ini` file needs to have CamelCase retained and have
no whitespace between key and value.  E.g. `Sunrise=07:30`.
Specific overrides were needed to ensure the file was written in the correct
format

## Logging
If running on Linux (i.e. RaspberryPi) then basic logging to `rsyslog` service is
configured.  If running Windows (i.e. to test) then logging is to `System.out` and `System.err`

See instructions at https://pimylifeup.com/raspberry-pi-syslog-server/ to set up 
service to receive log messages


## TO DO:
I could try make this location aware for when we're way out of 
Auckland)

