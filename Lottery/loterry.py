from TicketGenerator import TicketGenerator as Tickes
import random

class Lottery:
    def __init__(self,seed=18,size=6,maxTickes=10,all=False):        
        self.maxTickes=maxTickes
        self.tickes =Tickes(seed=seed,size=size,maxTickes=maxTickes,all=all).tickes      
        self.seller=[]
        self.sell()
    
    def randomTicket(self):
        [test] =random.sample(self.tickes,1)
        return test
    
    def sell(self):
        num = random.randint(3,self.maxTickes)
        for _ in  range(num):
            self.seller.append(self.randomTicket())
    def Winner(self):
        winner=self.randomTicket()
        if winner in self.seller:
            print("hay ganador")
        else:
            print("nadie gano")


    
    
    
        

if __name__== "__main__":
    a=Lottery()
    print(       
        a.Winner()
    )
