import redis
r=redis.Redis()

count={}

for dato in r.keys('*-LOV-*'):
    month=dato.split('-')[3]
    if not count.has_key(month):
        count[month]=1
    else:
        count[month]=count[month]+1

for month in sorted(count,key=count.__getitem__, reverse=True):
    print int(month),count[month]
