'''
q1: Print this:
                        sudh
                sudh    sudh    sudh
        sudh    sudh    sudh    sudh    sudh
sudh    sudh    sudh    sudh    sudh    sudh    sudh

            
'''


text=str(input("Enter Text: "))
l=len(text)


r = int(input("enter the number of lines: "))

j=1

result=""
for i in range(r):
    print(( ' ' * (l*2) )  *  (r-1-i), end='')

    print((text+(' '*l))*j)

    j+=2
print(result)

    

