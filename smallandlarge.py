largest=None
Smallest=None
while True:
    inp=raw_input('enter a number ')
    if inp =='done': break
    try:
        num=int(inp)
    except:
        print "invalid input "
        continue
    if largest == None:
        largest=num
    elif num>largest:
        largest=num
    if Smallest == None:
        Smallest=num
    elif num<Smallest:
        Smallest=num
print 'largest is',num
print 'Smallest is',num
	   