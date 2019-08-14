import datetime as dt
import time as tm


print(tm.time())
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dt.datetime.fromtimestamp(tm.time()))
print(dtnow.year,dtnow.month,dtnow.day)

delta = dt.timedelta(days=100)
print(delta)

today = dt.date.today()
print(today-delta)
print(today>today-delta)

print(['a','b','c']+[1,2,3])
print(type(lambda x: x+1))