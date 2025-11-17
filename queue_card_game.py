import random

def shuffle_cards():
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
