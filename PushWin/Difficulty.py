import random
class Difficulty:
    def __init__(self,size=10,index=5,select=5):         
        self.index=index
        self.size=size
        self.lisPush = tuple(range(size))
        self.select =select
        self.cupDifficulty()

    def factor(self,value):
        return value/ self.size

    def cupDifficulty(self):
        self.range_one=self.lisPush[:self.index]
        self.range_two=self.lisPush[self.index:]   
        self.size_one =len(self.range_one)
        self.size_two =len(self.range_two)

    def getDifficulty(self):                           
        if self.size_one ==self.size_two:
            return self.factor(1)                                                           
        return self.__difficulty() +self.factor(1)
    def _getDifficulty(self, select):                           
        self.select=select
        if self.size_one ==self.size_two:
            return self.factor(1)                                                           
        return self.__difficulty() + self.factor(1)
        
    def __difficulty(self):
        max_=max(self.size_one,self.size_two)                
        if self.select in self.range_one:                       
            return self.factor(self.size_two)
        else:                 
            return self.factor(self.size_one)
    
    def uot(self):
        self.getDifficulty()
        if self.index==5:
            return [(self.range_one,self.factor(1)),
            (self.range_two,self.factor(1))]        
        return [(self.range_one,self.factor(self.size_one)),
            (self.range_two,self.factor(self.size_two))]
    
        
     
        

if __name__== "__main__":
 a=Difficulty(10,7,8)
 print(
     a.uot()
 )