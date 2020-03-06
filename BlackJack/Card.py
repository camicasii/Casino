#conjunto de cartas
class Card:
    def __init__(self,suit,value):
        super().__init__()
        self.suit =suit
        self.value = value
    #reescribimos la salida al imprimir
    def __repr__(self):
        return " of ".join((self.value,self.suit))
