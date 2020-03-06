from Deck import Deck
from Hand import Hand
from time import sleep

class Game:
    def __init__(self):
        pass

    def testPlay(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.player_hand.display()            
            print("Dealer's hand is:")
            self.dealer_hand.display()
            sleep(5)

if __name__== "__main__":
    play=Game()
    play.play()