n, m, a = [int(x) for x in input().split()]
 
h = n//a
v = m//a
c = h*v
rv = v if n%a else 0 
rh = h if m%a else 0 
iSec = 1 if m%a and n%a else 0 
c += rv + rh + iSec
print(c)
