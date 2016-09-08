#-*- encoding:utf-8 -*-
#定义类
# class TestClass:
#     """
#             添加类说明 紧跟类名后面 用三引号包围
#     """
#     #定义方法和属性
#     def pr(self):
#         #属性
#         self.height=20
#         print(self.height)
#     pass
#实例化类
#调用__new__方法创建实例 __new__方法自动从Object继承
#调用__init__方法对其进行初始化 __init__方法在类中定义
# tc=TestClass
# tc().pr()

#查看类说明
# 类名.__doc__
# help(类名)

#实例属性 类属性
# class TestClass:
#     #定义类属性
#     cssa="class_attri"
#     def __init__(self):
#         #定义类的实例属性
#         self.a = 0
#         self.b = 20
#     def info(self):
#         print("a:",self.a,"b:",self.b,"cssa:",TestClass.cssa)
# if __name__=='__main__':
#     tc = TestClass()
#     tc.info()
    
    #在外部定义实例属性
#     tc.color = 'red'
#     print(tc.color)


#私有属性__ab
# class A:
#     
#     def __init__(self):
#         self.__ab = 20
#     def info(self):
#         print("self.__ab:",self.__ab)
# a = A()
# a.info()

#特殊属性
# print(a.__doc__)
# print(a.__name__)
# print(A.__dict__)
# print(a.__module__)
# print(A.__base__)
    


# #添加方法
# class washer():
#     #构造方法
#     def __init__(self,water=10,scour=2):
#         self.water=water
#         self.scour=scour
#         
#     def set_water(self,water):
#         self.water=water
#     def set_scour(self,scour):
#         self.scour=scour
#         
#     def add_water(self):
#         print("add water",self.water)
#     def add_scour(self):
#         print("add scour",self.scour)
#     def start_wash(self):
#         #类内部方法的相互调用
#         self.add_water()
#         self.add_scour()
#         print("start wash ...")
# if __name__ == '__main__':
#     w = washer()
# #     w.set_water(20)
# #     w.set_scour(4)
#     w.start_wash()
#     wb = washer(100,10)
#     wb.start_wash()
#     
# #深入类的属性
# #以对象名.属性名访问优先引用类的实例属性 以类名.属性名只能访问类属性
# class A:
#     a=0
#     def __init__(self):
#         self.a=10
#         self.b=100
# if __name__ == '__main__':
#     a=A()
#     print(a.a)
#     print(A.a)
#     
#反射 用字符串的形式操作类的属性/方法
#主要工具函数 hasattr(对象名,属性名) 检测是否有此属性
#setattr(对象名,属性名,值) 设置属性的值
#getattr(对象名,属性名) 获取属性的值
# aa=A()
# print(hasattr(aa, 'a'))
# print(hasattr(aa, 'cc'))
# print(aa.a)
# setattr(aa, 'a', 50)
# x=getattr(aa, 'a')
# print(x)

#属性包装
# class washer(object):
#   
#     def __init__(self,water=10,scour=2):
#         self._water=water
#         self.scour=scour
#         self.year=2010
#           
#     #可读 @property
#     @property
#     def water(self):
#         return self._water
#     @property
#     def total_year(self):
#         return 2015-self.year
#       
#     #注意类一定要指定继承object才能起作用
#     @water.setter
#     def water(self,water):
#         self._water = water
#           
#         
#     def set_water(self,water):
#         self.water=water
#     def set_scour(self,scour):
#         self.scour=scour
#           
#     def add_water(self):
#         print("add water",self.water)
#     def add_scour(self):
#         print("add scour",self.scour)
#     def start_wash(self):
#   
#         self.add_water()
#         self.add_scour()
#         print("start wash ...")
# if __name__ == '__main__':
#     w = washer()
#     print(w.water)
#     w.water=100
#     print(w._water)
#     print(w.total_year)



# #描述符
class NonNeg:
    def __init__(self,default=0):
        self.default=default
    def __get__(self,instance,owner):
        return self.default
    def __set__(self,instance,val):
        self.default=val
    def __delete__(self,instance):
        pass
class Movie():
    rating=NonNeg(20)
    score=NonNeg(30)
if __name__ == '__main__':
    m = Movie()
    print(m.rating)
    print(m.score)

#__call__
# class Tst():
#     def __call__(self):
#         print("hello")
# t = Tst()
# t()
        

