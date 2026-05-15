import math 
​
def cockroach_speed(s):
    #1km = 100,000 cm
    #1hr = 3600 secs
    return math.floor(s*100000 / 3600)