n = int(input('number of elements in list: '))
l1=[]
for i in range(n):
    a = int(input('enter a number: '))
    l1.append(a)

# 1(1)
sum = 0
for num in l1:
    sum=sum+num
    i+=1
print(sum)

# 1(2)
product=1
for j in l1:
    product=product*j
    i+=1
print(product)

# 1(3)
max = l1[0]
for k in l1[0:]:
    if k>l1[0]:
        max = k
print(max)