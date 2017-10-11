def normalize(name):
    return name.capitalize()
#capitalize:首字母大写 后面小写

from functools import reduce
def prod(L):
    def xx(x,y):
        return x*y
    return reduce(xx,L)
#求积 例[3,4,5,6]

from functools import reduce
def str2float(s):
    L=s.split('.')
    def tran(L):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[L]
   
    return reduce(lambda x,y:x*10+y,map(tran,L[0]))+reduce(lambda x,y:x*10+y,map(tran,L[1]))/1000
#把字符串'123.456'转换成浮点数123.456
#lambda 简化代码，为了减少单行函数的定义而存在的
