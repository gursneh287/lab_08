# 4(1)
r = int(input("enter the number of rows:-"))
c = int(input("enter the number of columns:-"))
m1=[]
m2=[]
sum_m=[]

# for matrix 1
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m1.append(l)

# for matrix 2
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m2.append(l)

for i in range(r):
    l=[]
    for j in range(c):
        sum = m1[i][j]+m2[i][j]
        l.append(sum)
    sum_m.append(l)

print("matrix 1")
for i in m1:
    print(i)
print()
print("matrix 2")
for i in m2:
    print(i)
print()
print("sum of matrix 1 and matrix 2")
for i in sum_m:
    print(i)


# 4(2)
r1 = int(input("enter the number of rows for mat1:-"))
c1 = int(input("enter the number of columns for mat1:-"))
r2 = int(input("enter the number of rows for mat2:-"))
c2 = int(input("enter the number of columns for mat2:-"))
m1 = []
m2 = []
if c1 == r2:
    # for matrix 1
    for i in range(r1):
        l=[]
    for j in range(c1):
        v=int(input("Enter the number:-"))
        l.append(v)
    m1.append(l)

    # for matrix 2
    for i in range(r):
        l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m2.append(l)