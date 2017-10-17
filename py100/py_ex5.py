from functools import reduce
a=int(input('请输入整数'))
b=int(input('请输入整数'))
c=int(input('请输入整数'))
print(sorted([a,b,c]))

#标答
a=[]
for i in range(0,3):
    m=int(input('整数'))
    a.append(m)
a.sort()
print(a)

