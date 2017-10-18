#斐波那契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
#递归
def fib2(n):
    if n==1 or n==2:
        return 1
    return fib2(n-1)+fib2(n-2)
#最简单最python（reduce（lambda 常用
from functools import reduce
l=[0,1]
for i in range(10):
    l.append(reduce(lambda x,y:x+y,l[-1:-3:-1]))
print(l)

#我的答案
m=[]
a,b=0,1
for i in range(0,10):
    a,b=b,a+b
    m.append(b)
print(m)
