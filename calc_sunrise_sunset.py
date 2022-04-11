import datetime as dt
from pytz import timezone
from skyfield import almanac
from skyfield.api import S, E, wgs84, load

def calc_sunrise_sunset():
    # Figure out local midnight.
    zone = timezone('Pacific/Auckland')

    now = zone.localize(dt.datetime.now())
    # print('now',now)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    # print('midnight',midnight)
    next_midnight = midnight + dt.timedelta(days=1)
    # print('next_midnight',next_midnight)
    # print()


    ts = load.timescale()
    t0 = ts.from_datetime(midnight)
    t1 = ts.from_datetime(next_midnight)
    eph = load('de421.bsp')
    bluffton = wgs84.latlon(36.8509 * S, 174.7645 * E)


    t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))
    sunrise = str(t[0].astimezone(zone))[11:16]
    sunset = str(t[1].astimezone(zone))[11:16]
    # print()

    results = {}
    results['sunrise'] = sunrise
    results['sunset'] = sunset
    return results


if __name__ == '__main__':
    results = calc_sunrise_sunset()

    print(f"Sunrise is at: {results['sunrise']}")
    print(f"Sunset is at: {results['sunset']}")