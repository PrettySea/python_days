# python 多态
class Base():
    def __init__(self):
        print("base")
        
    def func(self):
        print("base func")
        
        
class Son(Base):
    def __init__(self):
        Base.__init__(self)
        print("son")
        
    def func(self):
        print("son func")
        


class Test():
    def __init__(self, base: Base):
        self._monitor = base
        print("test")
        
    def func(self):
        self._monitor.func()
        
t = Test(Son())
t.func()
# base
# son
# test
# son func

t1 = Test(Base())
t1.func()
# base
# test
# base func
