import random

class deckOfCards:
    def __init__(self):
        self.cards = {"hearts":{
                        "ace":1,
                        "2":2, 
                        "3":3, 
                        "4":4, 
                        "5":5, 
                        "6":6, 
                        "7":7, 
                        "8":8, 
                        "9":9, 
                        "10":10, 
                        "jack": 11, 
                        "queen": 12, 
                        "king":13
                        },
                "diamonds":{
                        "ace":1,
                        "2":2, 
                        "3":3, 
                        "4":4, 
                        "5":5, 
                        "6":6, 
                        "7":7, 
                        "8":8, 
                        "9":9, 
                        "10":10, 
                        "jack": 11, 
                        "queen": 12, 
                        "king":13
                        },
                "clubs":{
                        "ace":1,
                        "2":2, 
                        "3":3, 
                        "4":4, 
                        "5":5, 
                        "6":6, 
                        "7":7, 
                        "8":8, 
                        "9":9, 
                        "10":10, 
                        "jack": 11, 
                        "queen": 12, 
                        "king":13
                        },
                "spades":{
                        "ace":1,
                        "2":2, 
                        "3":3, 
                        "4":4, 
                        "5":5, 
                        "6":6, 
                        "7":7, 
                        "8":8, 
                        "9":9, 
                        "10":10, 
                        "jack": 11, 
                        "queen": 12, 
                        "king":13
                        }
                    }
    def shuffle_cards(self):
        deck = []
        for suit in self.cards:
            for card_name in self.cards[suit]:
                deck.append((suit, card_name, self.cards[suit][card_name]))
        
        random.shuffle(deck)
        
        return deck

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def display(self):
        return self.queue
    
#-----actual game------#

deck = deckOfCards()
shuffled_deck = deck.shuffle_cards()
queue = Queue()

for card in shuffled_deck[1:6]:
    queue.enqueue(card)

player = deck.shuffle_cards()[0]

print("banker card:", queue.display())
print("Player card:", player)