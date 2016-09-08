#-*- encoding:utf-8 -*-


# #元类 类的创建和管理者 所有类都是元类(type)的实例
# class empty(object):
#     pass
# print(type(empty))
# #通过type创建类
# def print_(c):
#     print(c)
# hello = type('hello',(object,),dict(helo=lambda lf:print_('hello')))
# hello().helo()
# print(isinstance(empty, type))



#类实例化过程 __new__ __init__
# class Custom(object):
#     def __init__(self):
#         self.a = 20
#         print("init method")
#         
#     def __new__(cls,*args,**kwargs):
#         print("new instance")
#         return object.__new__(cls,*args,**kwargs)
#         
# if __name__ == '__main__':
#     c = Custom()
#     print(c.a)


#自定义元类 对其创建的类进行预处理
# class MyMeta(type):
#     def __init__(self,name,bases,dicts):
#         print("init instance")
#     def __new__(cls,name,bases,dicts):
#         dicts['info']=lambda self:print("Djx.")
#         res = type.__new__(cls,name,bases,dicts)
#         res.company="ShangMei"
#         return res
#     
# class Custom(metaclass=MyMeta):
#     pass
# if __name__ == '__main__':
#     c = Custom()
#     c.info()
#     print(c.company)
#2.x定义元类
# class cus:
#     __metaclass__ = MyMeta
#     pass
#定义全局元类
# __metaclass__ = MyMeta


#构造序列
# class MySeq:
#     def __init__(self):
#         self.lseq=['I','II','III','IV']
#     def __len__(self):
#         return len(self.lseq)
#     def __getitem__(self,key):
#         if 0 <= key < 4:
#             return self.lseq[key]
# if __name__ == '__main__':
#     m = MySeq()
#     for i in range(4):
#         print(m[i])

#构造迭代器
class MyIter:
    def __init__(self,start,end):
        self.count = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < self.end:
            r = self.count
            self.count += 1
            return r
        else:
            raise StopIteration
if __name__ == '__main__':
    for i in MyIter(1,10):
        print(i)   
#构造可比较类
#构造可运算类       
