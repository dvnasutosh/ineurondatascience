'''
                sudh
        sudh            sudh
sudh            sudh            sudh
        sudh            sudh
                sudh
'''

'''
                                sudh
                                
                        sudh            sudh

                sudh            sudh            sudh
        
        sudh            sudh            sudh            sudh

sudh            sudh            sudh            sudh            sudh

        sudh            sudh            sudh            sudh
                
                sudh            sudh            sudh
                        
                        sudh            sudh
                                
                                sudh
'''




a:str=str(input("Enter string: "))
len=a.__len__()

line:int=int(input("Enter no. of lines: "))

for i in range(line):
        print(((' '*len)+(' '*2))*(line-1-i), end='')
        print( ( a+((' '*len)+(' '*4)))*(i+1))
        print()

        
    
for i in range(line-2,-1,-1):
        print(((' '*len)+(' '*2))*(line-1-i), end='')
        print( ( a+((' '*len)+(' '*4)))*(i+1))
        print()
        
    
    

# def diamond(val:str,l:int):
#     if type(val)!=str:
         
    
#     type(l)!=int:
        
