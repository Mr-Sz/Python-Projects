
'''
Card Game Called "War" in Terminal using Python.
Pygame Coded By Shahroz 'Sz' Khan.

'''
import random

#set global values for card game
suits=('Spades','Diamonds','Clubs','Hearts')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

#card class - suit,rank,Value
class Card():
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}\n'

#deck class - makes, holds, and shuffles a deck + removes one card
class Deck():
    
    def __init__(self):
        self.created_deck=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(rank,suit)
                self.created_deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.created_deck)

    def deal_one(self):
        return self.created_deck.pop()

#player class - makes player and his deck, adds/remove single/multiple cards to hand/deck
class Player():
    def __init__(self,name):
        self.name=name
        self.my_deck=[]
    
    def remove_card(self):
        return self.my_deck.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.my_deck.extend(new_cards) #for multiple cards
        else:
            self.my_deck.append(new_cards) #for single card

    def __str__(self):
        return f'\nPlayer {self.name} has {len(self.my_deck)} cards.'

#intro
print('\n---> Welcome To War Card Game By Sz <---\n')
print("\n***Rules are Simple, Card Values Have been Set, Ace being Highest and Number-2 card being Lowest\n***after cards being shuffled and dealt, players put forth their card from the top of their deck\n***and compare. The card worth more wins the rounds and takes both cards and places the cards below\n***his deck. If both played cards have same Value, War Condition is met and both players have to take-out\n***5 cards from the top of their decks and new cards are put forth by each player for that round\n***and compared. The game continues untill a player's hand is empty and game-over!\n")

#user-input
p1=input('\nPlayer 1, Enter your name: ')
p2=input('Player 2,: Enter you name: ')

#game-setup
rounds=0
player1=Player(p1)
player2=Player(p2)
fresh_deck=Deck() #makes a deck
fresh_deck.shuffle() #shuffles the deck
print("\n---> New Card Deck's Unpacked and Shuffled!")

for i in range(26):#deals each player a hand of half-deck saved in playerinstance.my_deck
    player1.add_cards(fresh_deck.deal_one())
    player2.add_cards(fresh_deck.deal_one())

print('\n---> CARDS DEALT!')

cond=True
while cond:
    if len(player1.my_deck)==0:
        print(f'\n---> Player {player2.name} Won The Game!')
        cond=False
        break
    
    if len(player2.my_deck)==0:
        print(f'\n---> Player {player1.name} Won The Game!')
        cond=False
        break

    rounds+=1
    print(f'\n\t----> Round {rounds}! <----')

    #game starts
    player1_cards=[]
    player1_cards.append(player1.remove_card())
    print(f'\n--> Player {player1.name} played {player1_cards[-1]}')
    player2_cards=[]
    player2_cards.append(player2.remove_card())
    print(f'--> Player {player2.name} played {player2_cards[-1]}\n')

    #always checks for war cond first
    while player1_cards[-1].value == player2_cards[-1].value:
        print('\n\t----> WAR! <----')
        print(f'\n---> Equal Value Cards Played: {player1_cards[-1].rank}')
        
        if (len(player1.my_deck) and len(player2.my_deck))>=6: #checking if players have enough cards to give or not
            print('\n---> 5 Cards Taken From Both Players\n')
            for i in range(5):
                player1_cards.append(player1.remove_card())
                player2_cards.append(player2.remove_card())
                
        elif len(player1.my_deck)<=5:
            print(f"\n---> Player {player1.name} can't draw 5 cards ")
            print(f"\n---> Player {player2.name} has won the game! <---\n")
            cond=False
            break
            
        elif len(player2.my_deck)<=5:
            print(f"\n---> Player {player2.name} can't draw 5 cards ")
            print(f"\n---> Player {player1.name} has won the game! <---\n")
            cond=False
            break

        #puts out new cards from top of deck for comparing if war cond is met
        player1_cards.append(player1.remove_card())
        print(f'\n--> Player {player1.name} played {player1_cards[-1]}')
        player2_cards.append(player2.remove_card()) 
        print(f'\n--> Player {player2.name} played {player2_cards[-1]}')
        
    #compare logic
    if player1_cards[-1].value > player2_cards[-1].value:
        player1.add_cards(player1_cards)
        player1.add_cards(player2_cards)
        print(f'\n---> Player {player1.name} won the round!\n')
        print(f'\t---> Current Holdings <---\n{player1}\n{player2}')
    
    elif player1_cards[-1].value < player2_cards[-1].value:
        player2.add_cards(player1_cards)
        player2.add_cards(player2_cards)
        print(f'\n---> Player {player2.name} won the round!\n')
        print(f'\t---> Current Holdings <---\n-> {player1}\n-> {player2}')

print('\n\t----> GAMEOVER! <----')
print('\n---> Thank You For Playing - WAR <---\n')