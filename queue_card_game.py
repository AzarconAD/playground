import random

class deckOfCards:
    def __init__(self):
        self.suits = ["hearts", "diamonds", "clubs", "spades"]
        self.card_names = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    def shuffle_cards(self):
        deck = [(suit, card_name, value) 
                for suit in self.suits 
                for card_name, value in zip(self.card_names, self.values)]
        
        random.shuffle(deck)
        return deck
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

class Banker(Queue):
    def hold(self):
        return self.display()
    
    def draw(self):
        if self.queue:
            drawn_card = self.dequeue()
            return drawn_card
        else:
            return None
        
    def has_cards(self):
        return len(self.queue) > 0

class Player:
    def __init__(self):
        self.cash = 0
    
    def cash_in(self, deposit):
        if deposit > 0:
            self.cash += deposit
            return self.cash
        else:
            print("Deposit must be positive")
            return self.cash
    
    def cash_out(self, amount):
        if amount > 0 and amount <= self.cash:
            self.cash -= amount
            return amount
        else:
            print("Insufficient funds or invalid amount")
            return 0
    
    def check_balance(self):
        return self.cash
    
#-----initialize game-----#
deck = deckOfCards()
shuffled_deck = deck.shuffle_cards()

banker = Banker()
player = Player()

#-----enqueueing 5 cards to the banker's queue (hold)-----#
for card in shuffled_deck[1:6]:
    banker.enqueue(card)

player_card = shuffled_deck[0]

#-----actual game-----#
print("Please deposit first before playing the game.")

amount = float(input("Amount: "))
balance = player.cash_in(amount)

# while player.check_balance() > 0:
print("Your balance:", balance)
print("Game is starting...")

print("Player's card:", player_card)

#-----betting system-----#
while True:
    try:
        min_bet = 10
        print("Minimum bet is 10.")
        bet = float(input("Your bet: "))
        
        if bet <= min_bet:
            print("Bet must be greater than or equal to the minimum bet.")
        elif bet > balance:
            print(f"Insufficient funds. You have {balance}.")
        else:
            break  # Valid bet, exit the loop
            
    except ValueError:
        print("Please enter a valid number.")

#     round_number = 1
#     while banker.has_cards():
#         drawn_card = banker.draw()
#         print(f"\nRound {round_number}: Banker draws {drawn_card}")
        
#         player_value = player_card[2]
#         banker_value = drawn_card[2]
        
#         if player_value > banker_value:
#             print("Player wins this round!")
#             balance = bet * 2
#         elif player_value < banker_value:
#             print("Banker wins this round!")
#             balance -= bet
#         else:
#             print("It's a tie this round!")

#         choice = input("Would you like to keep playing? (y/n): ")
#         if choice == "y":
#             round_number += 1
#         elif choice == "n":
#             break

#     print("\nGame over!")

# print("Balance:", player.check_balance())