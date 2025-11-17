import random

class deckOfCards:
    def shuffle_cards(self):
        cards = {"hearts":{
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
        
        deck = []
        for suit in cards:
            for card_name in cards[suit]:
                deck.append((suit, card_name, cards[suit][card_name]))
        
        random.shuffle(deck)
        
        return deck

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
