import numpy as np
np.set_printoptions(formatter={'float': '{:0.6f}'.format})

def geometric_progression(a,r,n):
    return a*np.power(r,np.arange(n))

def arithmetic_progression(a,d,n):
    return a+np.arange(n)*d


a_gp = 1
r = 1.000001
till_power = 3
n = till_power*1000000
a_ap = 0
d = 0.000001

GP = geometric_progression(a_gp,r,n)
AP = arithmetic_progression(a_ap,d,n)

# only works for a_ap = 0 and a_gp = 1

idx = np.random.randint(0,n,(2,))
n = np.max(np.append(np.append(idx,np.sum(idx)),n))+1

GP = geometric_progression(a_gp,r,n)
AP = arithmetic_progression(a_ap,d,n)
print("     GP","      AP")
print(np.array([GP,AP]).T)
print("Product of"," and ".join(['{:.7f}'.format(k) for k in GP[idx]]),"is",'{:.7f}'.format(np.product(GP[idx])))
print("Sum of"," and ".join(['{:.7f}'.format(k) for k in AP[idx]]),"is",'{:.7f}'.format(np.sum(AP[idx])))
print("Natural logarithm of",'{:.7f}'.format(np.product(GP[idx])),'is {:.7f}'.format(np.log(np.product(GP[idx]))))
