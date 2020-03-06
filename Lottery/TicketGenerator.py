from itertools import permutations
from Ticket import Ticket
import  random

class TicketGenerator:
    def __init__(self,maxTickes=5,seed=24,size=4, all=False):
        self.seed=seed
        self.size=size
        self.maxTickes=maxTickes
        self.tickes=[]
        self.all=all
        self.Generator()    
    

    def Generator(self):        
        shuffle = list(range(1,self.seed))
        random.shuffle(shuffle)
        raw=permutations(shuffle,self.size)             
        if self.all:
            self.tickes=list(raw)
            return

        rawTickes=[next(raw) for _ in range(self.maxTickes)]
        self.tickes=[Ticket(value=v)for v in rawTickes]        

if __name__== "__main__":
    a=TicketGenerator()    
    print(
        a.tickes
    )
    
    