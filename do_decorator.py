
#装饰器：在代码运行期间动态增加功能的方式
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now1():
    print('2017-10-16')

#三层嵌套
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now2():
    print('三层嵌套')
    print(now2.__name__)


#三层嵌套:在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call')
        func()
        print('end call')
        return 
    return wrapper
@log
def now3():
    print('在函数调用的前后打印出\'begin call\'和\'end call\'的日志')


#使用默认值
import functools
import types 
def logger(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args, **kw)
        return wrapper
    if isinstance(text,types.FunctionType):        
        return decorator(text)
    else:        
        return decorator

@logger()
def f():
    pass
@logger('exector')
def f1():
    pass

