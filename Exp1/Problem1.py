import math
 
t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    s = raw_input()
 
    def perms(x):
        d = {}
        for c in x:
            d[c] = d.get(c, 0) + 1
        r = math.factorial(len(x))
        for v in d.values():
            r //= math.factorial(v)
        return r
 
    best = 10**18
    ans = s
 
    for i in range(n):
        for j in range(n):
            x = list(s)
            x[i] = s[j]
            x = ''.join(x)
            p = perms(x)
            if p < best:
                best = p
                ans = x
 
    print ans
    