# Names: Nikki, Vivian, Nicoly, Pratima, Austin
# Date: 7/26/23

# Import statements
from card import Card

# Blackjack
def black_jack():
    deck = Card.new_deck()
    mycard= [deck.pop(), deck.pop()]
    player_card= mycard
# Ask user if they want to add a card
    Add_card =input("yes or no")
    # if Add_card =="yes":
    #     mycard= player_card .appenddeck.pop()

    while Add_card =="yes":
        player_card.append(deck.pop())
        Add_card =input("yes or no")
 
 

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
    