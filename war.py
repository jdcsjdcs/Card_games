import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# create a card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# create a deck   
class Deck:
    
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    # remove on card from deck
    def deal_one(self):
        # remove one card from the list of all_cards
        return self.all_cards.pop()


# create a player
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == list:
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'



# Game setup
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()


# split the deck between players
for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

# start the game
round_num = 0
# check if someone losing
while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player One Wins!')
        game_on = False
        break
    
    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # while in war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 3:
                print('Player One unable to go to war')
                print('Player Two Wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print('Player Two unable to go to war')
                print('Player One Wins!')
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
