from skyfield import api

ts = api.load.timescale()
eph = api.load('de421.bsp')

print('Done')