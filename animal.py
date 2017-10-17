class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('dog is running')
class Cat(Animal):
    def run(self):
        print('cat is running')
    
dog=Dog()
cat=Cat()

a=list()
b=Animal()
c=Dog()

def run_twice(am):
    am.run()
    am.run()
    
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
#动态语言的鸭子类型       
class Duck(object):
    def run(self):
        print('Duck is running most slowly...')
