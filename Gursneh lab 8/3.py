l = list(int(x) for x in input('enter elements of list:').split())
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)