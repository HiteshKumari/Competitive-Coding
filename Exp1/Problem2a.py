import sys
import random
 
MAX = 400000
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in xrange(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in xrange(i * i, MAX + 1, i):
            prime[j] = False
 
def ok(x):
    return x > 1 and not prime[x]
 
input = sys.stdin.readline
t = int(input())
 
for _ in xrange(t):
    n = int(input())
    if n <= 4:
        print -1
        continue
 
    a = range(1, n + 1)
    while True:
        random.shuffle(a)
        good = True
        for i in xrange(n - 1):
            if not ok(a[i] + a[i + 1]):
                good = False
                break
        if good:
            print " ".join(map(str, a))
            break