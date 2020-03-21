import random
from Difficulty import Difficulty
class Profit():
    def __init__(self,size=10,index=5):         
        self.index=index
        self.size=size
        self.lisPush = tuple(range(size))
        self.difficulty=Difficulty(index=index)  


    def getProfit(self,select,bet):
        nivel=self.difficulty._getDifficulty(select)
        profit=(nivel + 1) * float(bet) 
                
        return profit
    
        
if __name__== "__main__":
    a=Profit(index=3)

    print(
        a.getProfit(8,10)
    )
    pass