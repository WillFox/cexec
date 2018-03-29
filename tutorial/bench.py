import time
t = time.time()
for x in xrange(0, 100000):
    a = x ** 10000
print time.time() - t
