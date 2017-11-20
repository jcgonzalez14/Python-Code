#  File: Blackjack.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/17/16
#  Date Last Modified: 9/23/16

import random

class Card:

    def __init__(self,pip,suit):
        self.pip = pip
        self.suit = suit
        self.value = 0
        self.ace = "no"

    def values(self):
        if self.pip == "K" or self.pip == "Q" or self.pip == "J":
            self.value = 10
        elif self.pip == "A":
            self.value = 11
        else:
            self.value = (int(self.pip))
        
    def __str__(self):
        return(str(self.pip) + str(self.suit))
   
class Deck:
    
    def __init__(self):
        self.cardList = []
        suits = ["C","D","H","S"]
        pips = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for i in suits:
            for j in pips:
                cards = Card(j,i)
                if j == "A":
                    cards.ace = "yes"
                cards.values()
                self.cardList.append(cards)

    def shuffle(self):
        random.shuffle(self.cardList)   

    def __str__(self):
        string = ""
        count = 0
        while count < (len(self.cardList) - 3):
            for card in self.cardList:
                string += "{:<4}".format(str(card))
                if count == 12 or count == 25 or count == 38:
                    string += "\n"
                count += 1
            return(str(string))
        
    def dealOne(self, listy, i=0):
        listy.append(self.cardList.pop(i))
        return listy

class Player:

    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def cal_value(self):
        self.handTotal = 0
        for i in self.hand:
            self.handTotal = i.value + self.handTotal
        return self.handTotal           

    def __str__(self):
        new = []
        for card in self.hand:
            new.append(str(card))
        for i in self.hand:
            self.handTotal = i.value + self.handTotal
        return ' '.join(new)
    
def main():

    print("Let's play a game of blackjack. Ready?")
    print()

    julio = True
    while julio:
        deck1 = Deck()
        print("Initial deck:")
        print(deck1)
        print()

        deck1.shuffle()

        dealer = Player()
        opponent = Player()

        cardy = deck1.dealOne(opponent.hand)
        deck1.dealOne(dealer.hand)
        deck1.dealOne(opponent.hand)
        deck1.dealOne(dealer.hand)

        dealer.cal_value()
        opponent.cal_value()
            
        dummy = opponent.handTotal
        mummy = dealer.handTotal

        ready = 1
        if opponent.handTotal == 21:
            if opponent.handTotal == dealer.handTotal:
                print("You have a blackjack!", opponent)
                print("Dealer has blackjack too!", dealer)
                print("Dealer wins!")
                ready = 3
            else:
                print("You hold", opponent,"for a total of", opponent.handTotal)
                print("While dealer holds", dealer)
                print("Blackjack! You win")
                ready = 3
        else:
            print("Dealer shows", dealer.hand[1],"faceup")
            print("You show", opponent.hand[1], "faceup")
            print()
            print("You go first")
            print("You hold", opponent,"for a total of", opponent.handTotal)
            
            ready = eval(input('1 (hit) or 2 (stay)? '))

        aces = 0
        while ready == 1:
            print()
            print("Your current Hand Total is",dummy)
            cardy = deck1.dealOne(opponent.hand)
            for i in range(len(opponent.hand)):
                if opponent.hand[i].ace == "yes":
                    aces = aces + 1
                    opponent.hand[i].ace == "no"
            print("Card dealt: ",cardy[-1])
            dummy = dummy + cardy[-1].value
            if dummy < 21:
                print("Your new Hand Total is",dummy)
                ready = eval(input('1 (hit) or 2 (stay)? '))
            elif dummy == 21:
                print("21! My turn....")
                ready = 2
            else:
                if aces > 0:
                    print("Over 21. Switching an Ace from 11 points to 1.")
                    aces = aces - 1
                    dummy = dummy - 10
                    print("Your current hand is", dummy)
                    ready = eval(input('1 (hit) or 2 (stay)? '))
                else:
                    print("Over 21! You lose!")
                    ready = 3
                    
        print()
        joto = 1
        if ready ==2:
            print("Dealer's turn")
            print("Your hand:", opponent,"for a total of", dummy)
            print("Dealer's hand:", dealer, "for a total of", mummy)
            if mummy > dummy:
                print("Dealer has better hand! You lose")
                joto = 2
            elif mummy == dummy:
                print("Dealer has equal hand! You lose")
                joto = 2
            else:
                joto = 1
        elif ready == 3:
            joto = 2


        baces = 0 
        while joto == 1:
            puto = deck1.dealOne(dealer.hand)
            for j in range(len(dealer.hand)):
                if dealer.hand[j].ace == "yes":
                    baces = baces + 1
                    dealer.hand[j].ace = "no"
            print("Dealer hits: ",puto[-1])
            mummy = mummy + puto[-1].value
            print("Dealer's new total:", mummy)
            print()
            if mummy > 21:
                if baces > 0:
                    print("Over 21. Switching an Ace from 11 points to 1.")
                    baces = baces - 1
                    mummy = mummy - 10
                    print("Dealer's current hand is", mummy)
                    print()
                else:
                    print("Dealer is over 21! You win!")
                    joto = 2
            elif mummy == 21 or mummy == dummy:
                print("Dealer wins!")
                joto = 2
            elif mummy > dummy and mummy <=21:
                print("Dealer wins!")
                joto = 2

        print()
        print("Game over.")
        print()
        print("Deck after dealing cards:")
        print(deck1)
        print()
        print ("Final hands:")
        print ("   Dealer:   ", dealer)
        print ("   Opponent: ", opponent)
        print()

        decision = input("Want to play again? (Type Yes or No)")
        if decision == "No":
            julio = False
    
main()

