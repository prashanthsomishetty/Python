input=raw_input('enter the string: ')
n=len(input)
flag=0
for i in range (n):   
    inp=input[n-1-i]
    inp1=input[i]
    if inp==inp1:
        flag=0
    else:
       flag=1
if flag==0:
    print ('the given input is a palindorme')
else :
    print ('the given input is not a palindorme')