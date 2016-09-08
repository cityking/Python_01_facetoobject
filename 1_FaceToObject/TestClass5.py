#-*- encoding:utf-8 -*-
#作业
class Side:
    def __init__(self,side):
        for i in range(0,6):
            if 1<=side[i]<=6:
                side[i] = side[i]
            else:
                side[i] = side[i]%6+1
        self.side = side
    def __set__(self,instance,value):
        for i in range(0,6):
            if 1<=value[i]<=6:
                self.side[i] = value[i]
            else:
                self.side[i] = value[i]%6+1
        
    def __get__(self,instance,owner):
        return self.side
    def __delete__(self,instance):
        pass
class Box:
    num = 0
    opened = False
    side = Side([1,52,63,14,57,14])
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
        self.__volume = self.length*self.width*self.height
        Box.num =Box.num+1
        self._color = "red"
        
        
    def getVolume(self):
        return self.__volume
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color = value
        
    def setColor(self,color):
        self._color = color
    def getColor(self):
        return self._color
    
    def openBox(self):
        if(Box.opened):
            print("the box has opened")
        else:
            print("open box...")
            Box.opened = True
    def closeBox(self):
        if(not Box.opened):
            print("the box has closed")
        else:
            print("close box...")
            Box.opened = False
    
    def show(self):
        print("length:",self.length)
        print("width:",self.width)
        print("height:",self.height)
        
        print("实例化了{}次".format(Box.num))
    def __call__(self):
        print(self.__volume)
        
if __name__ == '__main__':
    b1 = Box(2,4,6)
    b1()
    
    
class Saizi():
    
    def __init__(self,start,end):
        self.face = 'yellow'
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
            
    @staticmethod
    def get_num(color):
        if(color == 'red'):
            num = 1
        elif(color == 'black'):
            num = 2
        elif(color == 'yellow'):
            num = 3
        elif(color == 'white'):
            num = 4
        elif(color == 'blue'):
            num = 5
        elif(color == 'green'):
            num = 6
        else:
            num = 0
        return num
    @classmethod
    def gen_dice(cls,start,end):
        return Saizi(start,end)
    
if __name__ == '__main__':
   
    for i in Saizi(1,7):
        print(i)
              
    
    
