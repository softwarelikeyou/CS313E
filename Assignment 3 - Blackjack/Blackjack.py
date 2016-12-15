import random

class Card:
    suit = ''
    pip = ''

    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return self.pip + self.suit
    
class Deck:
    cardList = []

    def __init__(self):
        for suit in ['C', 'D', 'H', 'S']:
            for i in range(2, 11):
                self.cardList.append(Card(suit, str(i)))
            for face in ['J', 'Q', 'K', 'A']:
                self.cardList.append(Card(suit, face))

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        string = '  '
        counter = 0
        for i in range(len(self.cardList)):
            string += ('{:<4}'.format(str(self.cardList[i])))
            counter += 1
            if (counter == 13):
                string += ('\n')
                string += ('  ')
                counter = 0
        return string
    
    def shuffle(self):
        random.shuffle(self.cardList)

    def dealOne(self, player):
        card = self.cardList.pop(0)
        player.addCard(card)
        #print('Card dealt: ' + str(card), end='\n')
        
class Player:
    name = ''
    hand = []
    handTotal = 0
    hasAce = False

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        string = self.name + ' hand: '
        for i in range(len(self.hand)):
            ## fix when len != 2
            string += ('{:<4}'.format(str(self.hand[i])))
        string += ' for a total of ' + str(self.handTotal)
        return string
    
    def addCard(self, card):
        if card.pip == 'J' or card.pip == 'Q' or card.pip == 'K':
            self.handTotal += 10
        elif card.pip == 'A': 
            if self.handTotal <= 10:
                self.handTotal += 11
                self.hasAce = True
            else:
                self.handTotal += 1
        else:
            self.handTotal += int(card.pip)
        self.hand.append(card)

    def swapAce(self, value):
        self.handTotal = 0
        for card in self.hand:
            if card.pip == 'J' or card.pip == 'Q' or card.pip == 'K':
                self.handTotal += 10
            elif card.pip == 'A':
                self.handTotal += value
            else:
                self.handTotal += int(card.pip)

    def faceUp(self):
        return self.hand[1]

    def lastCard(self):
        return self.hand[-1]
    
def showHands(you, dealer):
    print('Dealer shows ' + str(dealer.faceUp()) +  ' faceup', end='\n')
    print('You show ' + str(you.faceUp()) + ' faceup', end='\n')

def yourTurn(cardDeck, dealer, you):
    print('You go first.', end='\n')
    print(end='\n')
    if you.hasAce == True:
        print('Assuming 11 points for an ace you were dealt for now.', end='\n')
    print(you)
    while True:
        try:
            choice = int(input('1 (hit) or 2 (stay)? '))
            if choice > 2:
                continue
            # logic is here
            if choice == 1:
                cardDeck.dealOne(you)
                print('Card dealt:' + str(you.lastCard()))
                if you.handTotal > 21 and you.hasAce == True:
                    print('Over 21.  switching an ace from 11 points to 1.')
                    you.swapAce(1)
                    print('New total:' + str(you.handTotal))
                    print()
                    continue
                elif you.handTotal > 21:
                    break
                elif you.handTotal == 21:
                    print(str(you.handTotal) + '!')
                    break
                else:
                    continue
            elif choice == 2:
                break
        except ValueError:
            continue
        
def dealerTurn(cardDeck, dealer, you):
    while dealer.handTotal < 21:
        if dealer.handTotal < you.handTotal:
            if dealer.hasAce == True:
                print('Assuming 11 points for an ace I was dealt for now.')
            cardDeck.dealOne(dealer)
            print('Dealer hits:' + str(dealer.lastCard()))
            print('New total:' + str(dealer.handTotal))
            print()
            if dealer.handTotal > 21 and dealer.hasAce == True:
                print('Over 21.  switching an ace from 11 points to 1.')
                dealer.swapAce(1)
                print('New total:' + str(dealer.handTotal))
                print()
            continue
        else:
            break

def gameOver(dealer, you):
    print(end='\n')
    print('Game over.')
    print('Final hands:')
    print(dealer)
    print(you)
    
def main():
    cardDeck = Deck()
    print('Initial deck:', end='\n')
    print(cardDeck)
    random.seed(50)
    cardDeck.shuffle()
    print('Shuffled deck:', end='\n')
    print(cardDeck)
    
    dealer = Player('Dealer')
    you = Player('Your')
    cardDeck.dealOne(you)
    cardDeck.dealOne(dealer)
    cardDeck.dealOne(you)
    cardDeck.dealOne(dealer)
    
    print(you)
    print()
    print(dealer)
    print()
    print('Deck after dealing two cards each:', end='\n')
    print(cardDeck)
    print()

    showHands(you, dealer)
    print()

    yourTurn(cardDeck, dealer, you)
    print()
    if you.handTotal > 21:
        print('You have ' + str(you.handTotal) + '. You bust! Dealer wins.')
    else:
        print()
        print('Dealer\'s turn')
        print(you)
        print(dealer)
        print()
        dealerTurn(cardDeck, dealer, you)
        if dealer.handTotal > 21:
            print('Dealer has ' + str(dealer.handTotal) + '.Dealer busts! You win.')
        else:
            print('Dealer wins.')
            
    gameOver(dealer, you)

main()
