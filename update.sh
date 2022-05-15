#!/bin/bash
DIR=/home/pi/python/update_sunrise_sunset
SCRIPT=main.py
CONFIG_FILE=/home/pi/.openauto/config/openauto_system.ini

cd $DIR
python3 $DIR/$SCRIPT $CONFIG_FILE
