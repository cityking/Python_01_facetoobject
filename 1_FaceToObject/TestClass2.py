#-*- encoding:utf-8 -*-

#1.静态方法和类方法
#1.1静态方法
#1.2类方法
class washer(object):
    #定义类属性
    company="Le Xi"
    #1.11定义静态方法
    @staticmethod
    def spins_ml(spins):
        #1.13静态方法只能访问类属性不能访问实例属性
        print("company:",washer.company)
        return spins*0.4
    
    #1.21定义类方法
    @classmethod
    def get_washer(cls,water,scour):
        #1.23类方法只能访问类属性不能访问实例属性
        print("company:",washer.company)
        return cls(water,cls.spins_ml(scour))
   
    def __init__(self,water=10,scour=2):
        self._water=water
        self.scour=scour
        self.year=2010
 
    @property
    def water(self):
        return self._water
    @property
    def total_year(self):
        return 2015-self.year
       
   
    @water.setter
    def water(self,water):
        self._water = water
           
         
    def set_water(self,water):
        self.water=water
    def set_scour(self,scour):
        self.scour=scour
           
    def add_water(self):
        print("add water",self.water)
    def add_scour(self):
        print("add scour",self.scour)
    def start_wash(self):
   
        self.add_water()
        self.add_scour()
        print("start wash ...")
# if __name__ == '__main__':
#     #1.12访问静态方法
#     print(washer.spins_ml(8))
#     w=washer(100,washer.spins_ml(8))
#     w.start_wash()
    #1.22访问类方法
#     w = washer.get_washer(100, 9)
#     w.start_wash()
#     
#2.类的继承和方法重载
class washerDry(washer):
    def dry(self):
        print("dry clothes...")
    #重载父类方法
    def start_wash(self):
        print("......")
        #使用super一定要指定其父类继承自object
        super(washerDry,self).start_wash()
        print("......")
        
if __name__ == '__main__':
    w = washerDry()
    w.start_wash()
    w.dry()
