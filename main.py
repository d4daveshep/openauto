import argparse
from pathlib import Path

import get_sunrise_set
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


if __name__ == '__main__':
    args = parse_args()

    results = get_sunrise_set.get_sunrise_sunset()
    if results['status_code'] == 200:
        update_config.update_config(args.configfile, results)
    else:
        SystemExit(f"Couldn't get times from web page.  Status code = {results['status_code']:d}")
