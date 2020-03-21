import random
from Profit import Profit
class Push:
    def __init__(self,size=10,index=5):         
         self.profit = Profit(index=10)

    def Play(self):
        playing = True
        index = random.randint(0,9)
        self.profit.index=index
        casa =0
        clientes=0
        count =0
        while count<100:
            bit=random.randint(1,15)
            num=random.randint(0,9)
            select = random.randint(0,9)
            if random.random()>0.7:
                select=num
            if random.randint(0,9)>5:
                index = random.randint(0,9)
            if num==select:
                clientes+=self.profit.getProfit(select,bit)
            else:
                casa+=bit
            count +=1
        print(casa,int(clientes),casa >int(clientes))
            
                
            
            


if __name__== "__main__":
    a=Push()
    a.Play()