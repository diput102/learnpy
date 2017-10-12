def is_odd(n):
    return n%2==1
#构造从3开始的奇数序列	
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
	
#筛选函数	
def _not_divisible(n):
    return lambda x:x%n>0
#生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter()
    while True:
	    n=next(it)
	    yield n
	    it=filter(_not_divisible(n),it)
#打印1000以内的素数
for n in primes():
    if n<1000:
	    print(n)
    else:
        break
#筛出回文数
def is_palindrome(n):
    def return_listnum(n):
        def int2num(n):
            while(n>0):
                s=n%10
                n=n//10
                yield s
        return list(int2num(n))
    if return_listnum(n)[::]==return_listnum(n)[::-1]:
        return n
def main():
    output=filter(is_palindrome(n),range(0,1000))
    print(list(output))
if __name__ == '__main__':
    main()

#筛出回文数(标答版）
def is_palindrome2(n):
    n_str=str(n)
    if n_str[::]==n_str[::-1]:
        return n

    
    

        


	
       
