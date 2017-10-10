#!/usr/bin/env.python3
#-*- coding:utf-8 -*-
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
def triangles():
    I1=[1]
    I2=[1,1]
    while 1:
        yield I1
        I1=I2
        I2=[I1[i]+I1[i+1] for i in range(len(I1)-1)]
        I2.insert(0,1)
        I2.append(1)
def yanghui(max):
    A=[1]
    B=[1,1]
    n=0
    while n<max:
        yield A
        A=B
        B=[A[i]+A[i+1] for i in range(len(A)-1)]
        B.insert(0,1)
        B.append(1)
        n=n+1
def triangles2(max):
    L=[]
    result=[]
    n=0
    while n<max:
        L=result
        result=[]

        for i,v in enumerate(L):
            if i>=1:
                result.append(L[i]+L[i-1])
            else:
                result.append(1)
        result.append(1)
        yield result
        n=n+1
    
    
