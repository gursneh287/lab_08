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
    for i in range(r2):
        l=[]
    for j in range(c2):
        v=int(input("Enter the number:-"))
        l.append(v)
    m2.append(l)
