
def build(x,y):
    return lambda:x*x+y*y
print(build(2,3)())

def build(x,y):
    return x*x+y*y
print(build(2,3))
#use lambda simple the last code
def count():
    fs=[]
    def f(n):
        return lambda:n*n
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
