import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
         self.deck = [Card(suit,rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total} chips')
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Player stands, Dealer goes')
            playing = False

        else:
            print('Sorry, I did not understand, please enter h or s ')
            continue

        break

def show_some(player, dealer):
    print(f'Dealer Hand: {dealer.cards[1]}')
    print('Player Hand:', *player.cards)
    


def show_all(player, dealer):
    print('Dealer Hand:', *dealer.cards)
    print('Value of Dealer hand is:', dealer.value)
    print('Player Hand:', *player.cards)
    print('Value of Player hand is:', player.value)

def player_bust(player, dealer, chips):

    print('Bust Player!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    
    print('Player Wins!')
    chips.win_bet()


def dealer_bust(player, dealer, chips):

    print('Player Wins! Bust Dealer!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):

    print('Dealer Wins!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie')

# Game start

while True:

    print('Welcome to BlackJack')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print(f'Player total chips: {player_chips.total}')

    new_game = input('Would you like to play an other game? y or n')

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print('Thank you for playing')
        break














