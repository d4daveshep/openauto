# read the  config file
import configparser

config_file = "z:/phones/android auto/openauto_system.ini"
config = configparser.ConfigParser()
config.read(config_file)

sunrise = config["DayNight"]["SunriseTime"]
sunset = config["DayNight"]["SunsetTime"]
print(f"Sunrise time = {sunrise}")
print(f"Sunset time = {sunset}")

new_sunrise = "7:25"
new_sunset = "17:29"

config["DayNight"]["SunriseTime"] = new_sunrise
config["DayNight"]["SunsetTime"] = new_sunset

print(f"Sunrise time = {new_sunrise}")
print(f"Sunset time = {new_sunset}")

with open(config_file, 'w') as ini_file:
    config.write(ini_file)
