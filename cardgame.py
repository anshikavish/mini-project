from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    def __init__(self):
        print("create new order deck")
        self.allcards=[(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)
    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    def add(self,added_cards):
        self.cards.extend(added_cards)
    def remove(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card=self.hand.remove()
        print("{} had places:{}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def stil_cards(self):
        return len(self.hand.cards)!=0
print("Welcome to War, let's begin...")
d=Deck()
d.shuffle()
half1,half2=d.split_in_half()

comp=Player("conputer", Hand(half1))
name=input("your name")
user=Player(name, Hand(half2))

total_round=0
war_count=0
while user.stil_cards() and comp.stil_cards():
    total_round+=1
    print("new round")
    print("current standings")
    print(user.name+"has count"+str(len(user.hand.cards)))
    print(comp.name+"has count"+str(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    table_card=[]
    c_card=comp.play_card()
    p_card=user.play_card()
    table_card.append(c_card)
    table_card.append(p_card)
    if c_card[1]==p_card[1]:
        war_count+=1
        print("war")
        table_card.extend(user.remove_war())
        table_card.extend(comp.remove_war())
        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            user.hand.add(table_card)
        else:
            comp.hand.add(table_card)
    else:
        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            user.hand.add(table_card)
        else:
            comp.hand.add(table_card)
print("game over,number of rounds:"+str(total_round))
print("a war happen"+str(war_count)+"times")

print("does comp has cards")
print(str(comp.stil_cards()))
print("does player has cards")
print(str(user.stil_cards()))
