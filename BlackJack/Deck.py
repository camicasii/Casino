import random
from Card import Card
#maso
class Deck:
    __suit=["Spades", "Clubs", "Hearts","Diamonds"]
    __number=["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self):
        self.cards = [Card(s, v) for s in self.__suit 
                        for v in self.__number]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
            

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

if __name__== "__main__":
    a= Deck()
    print(
len(a.cards),a.shuffle(),
a.deal().suit,
len(a.cards)
)