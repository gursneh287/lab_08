# 5(1)
l= list(str(x) for x in input('enter strings: ').split())
sub_str = input('enter substring: ')
count=0
for i in range(len(l)):
    if sub_str in l[i]:
        count=count+1
print(count)

# 5(2)
l1= list(int(x) for x in input('enter integers: ').split())
l2=[]
for i in l1:
    if i<=0:
        i = 0
        l2.append(i)
    else:
        i = i**2
        l2.append(i)
print(l2)

# 5(3)
l3 = list(int(x) for x in input('enter integers: ').split())
l4 = []
for i in l3:
    if 10<=i<=20:
        i = i**2
        l4.append(i)
    else:
        l4.append(i)
print(l4)

# 5(4)
l5 = list(str(x) for x in input('enter strings: ').split())
l6=[]
for i in l5:
    if i[0].islower()==True:
        i = i.upper()
        l6.append(i)
    else:
        l6.append(i)
print(l6)

