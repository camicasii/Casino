from Deck import Deck
from Hand import Hand
from time import sleep

class Game:
    def __init__(self):
        pass

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer
    
    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")
    
    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def first_hand(self):                
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        print("Your hand is:")
        self.player_hand.display()            
        print("Dealer's hand is:")
        self.dealer_hand.display()
        
    def second_hand(self,choice):    
        if choice in ['hit', 'h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        return True
        else:
            player_hand_value = self.player_hand.get_value()
            dealer_hand_value = self.dealer_hand.get_value()

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            if player_hand_value > dealer_hand_value:
                print("You Win!")
            elif player_hand_value == dealer_hand_value:
                print("Tie!")
            else:
                print("Dealer Wins!")
            return True                   


    
    def Play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            self.first_hand()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()              
                game_over = self.second_hand(choice)
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False
            
                
                

    
        

if __name__== "__main__":
    play=Game()
    play.Play()