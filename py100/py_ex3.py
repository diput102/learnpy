# if a num add 100 can be sqrt,
#and it add 100 add 168 also can be sqrt ,
#find it and print
m=int(input('input range'))
def xxx(n):
    for x in range(1,n):
        if (n/x==x):
            return n
def add100add168(n):
    m=n+100
    if (xxx(m)):
        k=m+168
        if(xxx(k)):
            return n
def main():
    print(list(filter(add100add168,range(0,m))))

if __name__=='__main__':
    main()
