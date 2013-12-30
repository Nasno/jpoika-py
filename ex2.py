from math import sqrt
def is_prime(x):
    if(x>0):
        for y in range(2,int(sqrt(x))):
            if ((x/y)%1==0):
                return True
                break
        else:
            return False
    else:
        return False
