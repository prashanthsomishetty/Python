inp = raw_input ('enter the number of series: ')
num=int(inp)
a=1
b=1
c=0
if num==0:
    print 'nothing'
if num==1:
    print a
if num==2:
    print a
    print b
for i in range (num-2):
    
    if a==1 and b==1:
      print a
      print b
    c=a+b
    a=b
    b=c
    print c
    