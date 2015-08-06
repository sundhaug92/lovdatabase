import redis
r=redis.Redis()

count={}

for dato in r.keys('*-LOV-*'):
    year=dato.split('-')[2]
    if not count.has_key(year):
        count[year]=1
    else:
        count[year]=count[year]+1

for year in sorted(count,key=count.__getitem__, reverse=True):
    print int(year),count[year]
