import argparse
import logging
import platform
import sys
from logging.handlers import SysLogHandler
from pathlib import Path

import calc_sunrise_sunset
# import get_sunrise_set
import update_config


def parse_args():
    # Parse the args
    parser = argparse.ArgumentParser(
        description='Update the OpenAutoPro config file sunrise and senset times')

    # define the argument to set the config file
    parser.add_argument("configfile", help="specify the full location of the config file")

    # parse the arguments and check the file exists
    args = parser.parse_args()

    if args.configfile:
        configfile = args.configfile

        if not Path(configfile).exists():
            raise SystemError("*** ERROR*** config file not found")

    return args


def initLogger():
    # copied from Example 5 at https://www.programcreek.com/python/example/3488/logging.handlers.SysLogHandler

    logger = logging.getLogger('UpdateSunTimes')
    logger.level = logging.DEBUG
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if platform.system() == 'Linux':
        logger.addHandler(SysLogHandler())

    if platform.system() == 'Windows':
        sh = logging.StreamHandler(sys.stderr)
        sh.setFormatter(formatter)
        logger.addHandler(sh)


if __name__ == '__main__':

    initLogger()
    logger = logging.getLogger('UpdateSunTimes')
    args = parse_args()

    # results = get_sunrise_set.get_sunrise_sunset()
    results = calc_sunrise_sunset.calc_todays_sunrise_sunset()
    if results['status_code'] == 200:
        update_config.update_config(args.configfile, results)
        logger.info(f"OAP UpdateSunTimes: Sunrise={results['sunrise']}, Sunset={results['sunset']}")
    else:
        logger.error(f"Couldn't update sun times.  Status code = {results['status_code']:d}")
        SystemExit()
