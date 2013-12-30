from math import *
def is_prime(x):
    if(x>1):
        for i in range(2,ceil(sqrt(x+1))):
            if ((float(x)/i)%1==0):
                return False
        else:
            return True
    else:
        return False

for x in range(2,100):
	if (is_prime(x)):
		print("Prime Number: "+str(x))
