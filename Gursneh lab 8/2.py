l1 = list(int(x) for x in input('enter elements of list:').split())
l2=[]
while l1:
    a = min(l1)
    l2.append(a)
    l1.remove(a)
print(l2)