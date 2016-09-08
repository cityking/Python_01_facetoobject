#-*- encoding:utf-8 -*-
class washer(object):
    
    def __init__(self,water=10,scour=2):
        self._water=water
        self.scour=scour
 
    @property
    def water(self):
        return self._water
    
       
   
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
if __name__ == '__main__':
    w = washer()
    w.start_wash()
    print(w.water)
    print(w._water)
    w.water=100
    print(w.water)
    print(w._water)      
        
        
        