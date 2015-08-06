import redis
r=redis.Redis()

count={}

for key in r.keys('*-LOV-*'):
    dept=r.hget(key,"dept")
    if not count.has_key(dept):
        count[dept]=1
    else:
        count[dept]=count[dept]+1

for dept in sorted(count,key=count.__getitem__, reverse=True):
    print dept,count[dept]
