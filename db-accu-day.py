import redis
r=redis.Redis()

count={}

for dato in r.keys('*-LOV-*'):
    day=dato.split('-')[4]
    if not count.has_key(day):
        count[day]=1
    else:
        count[day]=count[day]+1

for day in sorted(count,key=count.__getitem__, reverse=True):
    print int(day),count[day]
