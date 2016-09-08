#-*- encoding:utf-8 -*-
#python设计模式 迭代模式 单例模式 工厂模式

#单例模式
# class SingleClass:
#     def __init__(self,x=0):
#         self.x = x
# sc = SingleClass()
# 
# def tcs():
#     print(sc.x)
#     sc.x=10
#     print(sc.x)
#     
# def tcs2():
#     print(sc.x)
#     sc.x=5
#     print(sc.x)
#     
# if __name__ == '__main__':
#     tcs()
#     tcs2()

# class Singleton:
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls, '_sgl'):
#             cls._sgl = super().__new__(cls,*args,**kwargs)
#         return cls._sgl
#     
# if __name__ == '__main__':
#     sa = Singleton()
#     sb = Singleton()
#     print(id(sa))
#     print(id(sb))

#工厂模式
# class Ab:
#     a = 3
# class Ac:
#     a = 0
# class MyFactory:
#     def getInstance(self,ins):
#         return ins()
# if __name__ == '__main__':
#     mf = MyFactory()
#     print(type(mf.getInstance(Ab)))
#     print(type(mf.getInstance(Ac)))

#策略模式
#类作为参数传递
# class Moveable:
#     def move(self):
#         print("Move...")
# class Moveonfeet(Moveable):
#     def move(self):
#         print("Move on feet.")
# class Moveonwheel(Moveable):
#     def move(self):
#         print("Move on wheel.")
# class Moveobj:
#     def set_move(self,moveable):
#         self.moveable = moveable()
#     def move(self):
#         self.moveable.move()
# #不用继承Moveable也行
# class Test:
#     def move(self):
#         print("I'm fly.")
# if __name__ == '__main__':
#     m = Moveobj()
#     m.set_move(Moveable)
#     m.move()
#     m.set_move(Moveonfeet)
#     m.move()
#     m.set_move(Moveonwheel)
#     m.move()
#     m.set_move(Test)
#     m.move()
    
#函数作为传递参数
# def movea():
#     print("move a...")
# def moveb():
#     print("move b...")   
# class Moveobj:
#     def set_move(self,moveable):
#         self.moveable = moveable
#     def move(self):
#         self.moveable()
# if __name__ =='__main__':
#     m = Moveobj()
#     m.set_move(movea)
#     m.move()
#     m.set_move(moveb)
#     m.move()
    
#装饰模式
# class BeDeco:
#     def be_edit_fun(self):
#         print('Source fun.')
#     def be_keep_fun(self):
#         print('Keep fun.')
# class Decorater:
#     def __init__(self,dec):
#         self._dec = dec()
#     def be_edit_fun(self):
#         print('start...')
#         self._dec.be_edit_fun()
#     def be_keep_fun(self):
#         self._dec.be_keep_fun()
# if __name__ == '__main__':
#     dec = BeDeco()
#     dec.be_edit_fun()
#     dec.be_keep_fun()
#     dcr = Decorater(BeDeco)
#     dcr.be_edit_fun()
#     dcr.be_keep_fun()

# class Water:
#     def __init__(self):
#         self.name = 'water'
#     def show(self):
#         print(self.name)
# class Deco:
#     def show(self):
#         print(self.name)
# class Sugar(Deco):
#     def __init__(self,water):
#         self.name='sugar'
#         self.water=water
#     def show(self):
#         print(self.name)
#         print(self.water().name)
# class Salt(Deco):
#     def __init__(self,water):
#         self.name='salt'
#         self.water=water
#     def show(self):
#         print(self.name)
#         print(self.water().name)
# if __name__ == '__main__':
#     su = Sugar(Water)
#     su.show()
#     sa = Salt(Water)
#     sa.show()

#使用装饰器
def Deco(a_class):
    class NewClass:
        def __init__(self,age,color):
            self.color = color
            self.wrapped = a_class(age)
        def display(self):
            print(self.color)
            print(self.wrapped.age)
    return NewClass
@Deco
class Cat():
    def __init__(self,age):
        self.age = age
    def display(self):
        print(self.age)
if __name__ == '__main__':
    c = Cat(12,'black')
    c.display()
            
            