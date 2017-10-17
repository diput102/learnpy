#类和限制访问
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def name_print(self):
        print(self.__name)
    def grade_print(self):
        print('%s,%s'%(self.__name,self.__score))
    def get_grade(self):
        if self.__score>=90:
            print('a')
        elif self.__score>=60:
            print('B')
        else:
            print('c')
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
bart=Student('Bart smith',58)
