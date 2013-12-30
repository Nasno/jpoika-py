# ceil( sqrt( x + 1 ) )
# from math import *
a = [2]


def is_prime(x):
    global a
    if x > 1:
        for y in range(0, len(a)):
            if (float(x)/a[y]) % 1 == 0:
                return False
        else:
            return True
    else:
        return False

for i in range(2, 100000):
    if is_prime(i):
        a.append(i)
        print("Prime Number: "+str(i))
else:
    print("Number of Primes: "+str(len(a)))
