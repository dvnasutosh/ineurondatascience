def isHappy(num,b:list=[]):
    digsq=0
    for i in range(len(str(num))):
        digsq += int( str(num)[i] )  ** (2)
    
    if digsq==1:
        b=num=digsq=None
        b=[]
        del b
        del num
        del digsq
        
        return True
    elif digsq in b:
        b=num=digsq=None
        b=[]
        del b
        del num
        del digsq

        return False
    else:
        b.append(digsq)
        ret=isHappy(digsq,b)
        b=num=digsq=None
        b=[]
        del b
        del num
        del digsq
        
        return ret
    del b
# x=[i for i in range(100) if isHappy(i)]
# 1 7 10 13 19 23 28 31 32 44 49 68 70 79 82 86 91 94 97 100 
x=[]
dec=False
for j in range(100):
    dec=isHappy(j,b=[])
    if dec:
        x.append(j)

print(x)

'''

'''
