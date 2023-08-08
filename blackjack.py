# Names: Nikki, Vivian, Nicoly, Pratima, Austin
# Date: 7/26/23

# Import statements
from card import Card
game_over= False
# Blackjack
def black_jack():
    deck = Card.new_deck()
    player_hand= [deck.pop(), deck.pop()]
    dealer_hand= [deck.pop(), deck.pop()]


    def  hand_value(hand):
        sum=0
        for card in hand:
            sum= sum + card.value
            return sum 
   
    print(player_hand)
# Ask user if they want to add a card
    Add_card =input("yes or no")
    # if Add_card =="yes":
    #     mycard= player_card .appenddeck.pop()
    if hand_value(player_hand)>21:
        print("you")


    while Add_card =="yes":
        player_hand.append(deck.pop())
        print(player_hand)
        Add_card =input("yes or no")

    

    if hand_value(player_hand)>hand_value(dealer_hand):
        if hand_value(player_hand)<= 21:
            print("You won")
        else: 
            print("You lost")
    if hand_value(player_hand)< hand_value(dealer_hand):
        if hand_value(dealer_hand)<= 21:
            print("You lost")
        else:
            print("You won")
    if  hand_value(player_hand)== hand_value(dealer_hand):
       print("Tie")

 # check who won or lost 


# Code that runs when script is called from terminal
# ex: python my_card_game.py




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
    
   #game over
black_jack()