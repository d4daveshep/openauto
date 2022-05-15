from datetime import datetime
from datetime import timedelta
from pytz import timezone
from skyfield import almanac
from skyfield.api import S, E, wgs84, load

import pytest


def test_calc_sunrise_set():
    test_date = datetime.strptime('2022-04-12 19:54:00', '%Y-%m-%d %H:%M:%S')
    print(test_date)

    results = calc_sunrise_sunset(test_date)
    assert results['sunrise'] == '06:43'
    assert results['sunset'] == '17:59'
    assert results['status_code'] == 200


def calc_todays_sunrise_sunset():
    results = calc_sunrise_sunset(datetime.now())
    return results

def calc_sunrise_sunset(my_date):
    zone = timezone('Pacific/Auckland')

    now = zone.localize(my_date)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    next_midnight = midnight + timedelta(days=1)

    ts = load.timescale()
    t0 = ts.from_datetime(midnight)
    t1 = ts.from_datetime(next_midnight)
    eph = load('/home/pi/python/update_sunrise_sunset/de421.bsp')
    bluffton = wgs84.latlon(36.8509 * S, 174.7645 * E)

    t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))
    sunrise = str(t[0].astimezone(zone))[11:16]
    sunset = str(t[1].astimezone(zone))[11:16]

    results = {}
    results['sunrise'] = sunrise
    results['sunset'] = sunset
    results['status_code'] = 200
    return results


if __name__ == '__main__':
    results = calc_sunrise_sunset(datetime.now())

    print(f"Sunrise is at: {results['sunrise']}")
    print(f"Sunset is at: {results['sunset']}")
