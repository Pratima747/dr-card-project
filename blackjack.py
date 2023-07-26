# Names: Nikki, Vivian, Nicoly, Pratima, Austin
# Date: 7/26/23

# Import statements
from card import Card

# Program your game here!
# Blackjack
def black_jack():
    deck = Card.new_deck()
    random.shuffle(deck)
    player_card=
# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    black_jack()


class Player():
    def __init__ (self, name, hand, score=0):
        self.name = name 
        self.hand = hand
        self.score = score
       

class Computer(Player):
    def move(self,pile):
        # TODO: Generate a best possible move
        return None
    
class Human(Player):
    def move(self,pile):
        # TODO: Take in a user's input
        return None
    