
def mean(l): # creates 
    try:
        l=list(l)

        if(l.__len__()):
            raise   ZeroDivisionError    
    except Exception as e:
        return [0,e]
    
    return float(sum(l)/l.__len__())

