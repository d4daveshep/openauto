import datetime as dt
from pytz import timezone
from skyfield import almanac
from skyfield.api import S, E, wgs84, load

# Figure out local midnight.
zone = timezone('Pacific/Auckland')

now = zone.localize(dt.datetime.now())
print('now',now)
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
print('midnight',midnight)
next_midnight = midnight + dt.timedelta(days=1)
print('next_midnight',next_midnight)
print()


ts = load.timescale()
t0 = ts.from_datetime(midnight)
t1 = ts.from_datetime(next_midnight)
eph = load('de421.bsp')
bluffton = wgs84.latlon(36.8509 * S, 174.7645 * E)

# f = almanac.risings_and_settings(eph, eph['Sun'], bluffton)
# t, y = almanac.find_discrete(t0, t1, f)
#
# for ti, yi in zip(t, y):
#     print(str(ti.astimezone(zone))[:16], 'Rise' if yi else 'Set')
#
# print()

t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))
print(str(t[0].astimezone(zone))[:16])
print(str(t[1].astimezone(zone))[:16])
print()


# f = almanac.dark_twilight_day(eph, bluffton)
# times, events = almanac.find_discrete(t0, t1, f)
#
# previous_e = f(t0).item()
# for t, e in zip(times, events):
#     tstr = str(t.astimezone(zone))[:16]
#     if previous_e < e:
#         print(tstr, ' ', almanac.TWILIGHTS[e], 'starts')
#     else:
#         print(tstr, ' ', almanac.TWILIGHTS[previous_e], 'ends')
#     previous_e = e
print('Done')