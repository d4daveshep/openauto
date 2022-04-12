# read the  config file
import configparser

class CaseConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

def update_config(config_filename, new_times):

    # read the config file
    config = CaseConfigParser()
    config.read(config_filename)
    # config.optionxform = str  # preserve case for letters

    # update the sunrise and sunset times
    config["DayNight"]["SunriseTime"] = new_times['sunrise']
    config["DayNight"]["SunsetTime"] = new_times['sunset']

    # write the updated config file
    with open(config_filename, 'w') as ini_file:
        config.write(ini_file,space_around_delimiters=False)
        # config.write(ini_file)


if __name__ == '__main__':
    # create some dummy test data
    results = {'status_code': 200, 'sunrise': '07:12', 'sunset': '17:34'}
    config_file = "openauto_system.ini"

    update_config(config_file, results)

    # sunrise = config["DayNight"]["SunriseTime"]
    # sunset = config["DayNight"]["SunsetTime"]
    # print(f"Sunrise time = {sunrise}")
    # print(f"Sunset time = {sunset}")
