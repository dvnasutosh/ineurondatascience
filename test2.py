
# s=int(input('enter a number'))
from numpy import NaN


s=10

# 0 1 1 2 3 5 8 13

def fibonacci(n=10):
    out=[0,1]
    while(len(out)!=n):
        out.append(out[-1]+out[-2])
    return out
print(fibonacci(18))
