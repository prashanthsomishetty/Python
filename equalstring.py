inp1= raw_input('enter the string 1: ')
inp2= raw_input('enter the string 2: ')
n=len(inp1)
m=len(inp2)
flag=0
if n==m:
    for i in range(n):
        p=inp1[i]
        s=inp2[i]
        if p==s:
            print ('the alpha is same',p,s)          
        else:
            print ('the given strings are not equal')
            flag=1
    if flag==1:
        print ('both the strings are not equal')
    else:
        print ('both the strings are equal')
else:
    print ('the given strings are not equal')