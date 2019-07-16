import random

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] 
key = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = key[rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"

class Deck:

	def __init__(self):
		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def show_cards(self):
		for num in self.deck:
			print(num)

	def shuffle(self):
		self.used_numbers = []
		self.shuffled_deck = []

		while len(self.shuffled_deck) < len(self.deck):

			rand = random.randint(0, len(self.deck)-1)

			if rand not in self.used_numbers:
				self.used_numbers.append(rand)

				self.shuffled_deck.append(self.deck[rand])

		self.deck = self.shuffled_deck

	def deal(self, who):
		self.who = who

		self.who.cards.append(self.deck.pop(0))

class Player:

	def __init__(self, name):
		self.cards = []
		self.name = name
		self.bank = 100
		self.total = 0
		self.ace_total = 0

	def win(self, bet):
		self.bank += bet

	def bet(self, bet):
		self.bank -= bet

	def show_cards(self):
		print(f"\n{self.name} is showing:")
		for card in self.cards:
			print(card)

	def total_value(self):
		self.total = 0
		self.ace_total = 0
		ace_count = 0
		for card in self.cards:
			self.total += card.value
			self.ace_total += card.value
			if card.value == 11:
				self.ace_total -= 10
				ace_count +=1

		#Need to adjust the total value when multiple aces come into play
		if ace_count > 1:
			self.total -= 10 * (ace_count-1)

		if self.total <=21 and self.total != self.ace_total:
			print(f"\nYou have a total of {self.total} or {self.ace_total}.")		
		else:
			print(f"\nYou have a total of {self.ace_total}.")

	def best_value(self):
		if self.total > 21:
			return self.ace_total
		else:
			return self.total			

	#Player can only double down after initial cards have been dealt
	#This should be used to set the value of the stand variable
	def doubledown(self):
		global player_bet

		if len(self.cards) == 2 and self.bank >= player_bet:
			deck.deal(player)
			player.show_cards()
			player.total_value()

			if player.best_value() <= 21:
				print("\n---------------HOUSE--TURN---------------")
				
			self.bank -= player_bet
			player_bet *= 2
			return True
		elif len(self.cards) == 2:
			print("\nSorry you don't have enough money in your bank to double down at this time.")
			print(f"You have ${self.bank} in your bank.")
			return False
		else:
			print("Sorry you can't double down at this time.")
			return False

	def __str__(self):
		return f"\n{self.name} has ${self.bank} in their bank."

class House:

	def __init__(self):
		self.cards = []
		self.total = 0
		self.ace_total = 0

	def show_initial(self):
		self.total = 0
		self.ace_total = 0
		for card in self.cards:
			self.total += card.value
			self.ace_total += card.value
			if card.value == 11:
				self.ace_total -= 10

		print(f"\nThe House is showing 1 facedown card and:")
		print(self.cards[0])
		print(f"\nHouse is showing a total of {self.cards[0].value}")

	def show_cards(self):
		print(f"\nThe House is showing:")
		for card in self.cards:
			print(card)

	def total_value(self):
		self.total = 0
		self.ace_total = 0
		ace_count = 0
		for card in self.cards:
			self.total += card.value
			self.ace_total += card.value
			if card.value == 11:
				self.ace_total -= 10
				ace_count +=1

		#Need to adjust the total value when multiple aces come into play
		if ace_count > 1:
			self.total -= 10 * (ace_count-1)

		if self.total <=21 and self.total != self.ace_total:
			print(f"\nHouse is showing a total of {self.total} or {self.ace_total}.")		
		else:
			print(f"\nHouse is showing a total of {self.ace_total}.")

	def best_value(self):
		if self.total > 21:
			return self.ace_total
		else:
			return self.total			


def player_play():
	stand = False
	decision = ''
	while player.best_value() < 21 and stand == False:
		decision = ''
		while decision not in ['HIT', 'STAND', 'DOUBLEDOWN']:
			decision = input("\nWould you like to 'Hit' or 'Stand'? ").upper().replace(" ", "")
			if decision	== "HIT":
				deck.deal(player)
				player.show_cards()
				player.total_value()
			elif decision == 'STAND':
				print("\n---------------HOUSE--TURN---------------")
				stand = True
			elif decision.replace(" ", "") == 'DOUBLEDOWN':
				stand = player.doubledown()
			else:
				print("Please enter either HIT or STAND!")

def house_play():
	house.show_cards()
	house.total_value()
	while house.best_value() < 17:
		print("\nHouse takes another card.")
		deck.deal(house)
		house.show_cards()
		house.total_value()

def play_again():
	play_again = ""
	while play_again not in ['NO', 'YES']:
		play_again = input("\nWould you like to keep playing? ").upper()
		if play_again == 'NO':
			print(f"\nYou are leaving the table with ${player.bank}")
			return False
		elif play_again == 'YES':
			return True
		else:
			print("Please enter either YES or NO!")

def get_player_bet():
	player_bet = 0
	while True:
		try:
			while player_bet < 10 or player_bet > player.bank:
				player_bet = int(input("\nHow much would you like to bet? "))

				if player_bet < 10:
					print("\nPlease enter at least the table minimum of $10.")
				elif player_bet > player.bank:
					print("\nYou don't have enough in your bank to place that bet.")
					print(f"\nYou have ${player.bank} in your bank.")

		except:
			print("\nPlease enter a valid whole number to bet!")
		else:
			break

	return player_bet


playing = True

name = input("\nHello and welcome to BlackJack. What is your name? ")

player = Player(name)
house = House()

print(f"\nWelcome {name}, you are starting with $100 and the minimum bet at this table is $10. Have fun and good luck!")
print("\nValid inputs are 'HIT', 'STAND' and 'DOUBLE DOWN'.")

while playing == True:

	#Player has run out of money so game ends
	if player.bank < 10:
		playing = False
		print("\nSorry you have run out of money. Better luck next time!")
	else:

		#Clear player and house cards after each game
		player.cards = []
		house.cards = []
			
		#Get the bet from the player
		player_bet = get_player_bet()

		#Remove player's bet from their bank
		player.bet(player_bet)

		#Generate deck, shuffle and deal cards
		print("\nShuffling and Dealing cards now...")

		deck = Deck()
		deck.shuffle()

		deck.deal(player)
		deck.deal(player)

		deck.deal(house)
		deck.deal(house)

		player.show_cards()
		player.total_value()

		house.show_initial()

		#Player has blackjack condition
		if player.total == 21 and house.best_value() != 21:
			print("\nCongratulations you have BlackJack!!")
			player.win(int(player_bet*2.5))
			playing = play_again()
		#Both House and Player have blackjack condition
		elif player.total == 21 and house.best_value() == 21:
			print("\nDealer also has 21 so it is a push.")
			player.win(player_bet)
			playing = play_again()
		else:

			if player.best_value() == 11:
				print("You may want to Double Down.")

			#Player takes their turn
			player_play()

			if player.ace_total > 21:
				print("\nYou have busted! House wins!")
				print(f"\nYou have ${player.bank}")
				playing = play_again()
			elif player.total == 21 or player.ace_total == 21:
				print("\nCongratulations you have 21. Let's see what the dealer has...")
				#House takes their turn. As long as house doesn't get 21 then player wins.
				house_play()
				if house.best_value() < 21 or house.best_value() > 21:
					print("\nYou win.")
					player.win(player_bet*2)
					print(f"\nYou have ${player.bank}")
					playing = play_again()
				elif house.best_value() == 21:
					print("\nIt's a push!")
					player.win(player_bet)
					print(f"\nYou have ${player.bank}")
					playing = play_again()
			else:

				#House takes their turn
				house_play()

				#Checking that the house has not busted and has met stand requirements of 17
				if 17 <= house.best_value() <= 21:

					#House win condition
					if house.best_value() > player.best_value():
						print("\nThe House wins!")
						print(f"\nYou have ${player.bank}")
						playing = play_again()

					#Player win condition
					elif house.best_value() < player.best_value():
						print("\nYou win.")
						player.win(player_bet*2)
						print(f"\nYou have ${player.bank}")
						playing = play_again()

					#Push condition
					else:
						print("\nIt's a push!")
						player.win(player_bet)
						print(f"\nYou have ${player.bank}")
						playing = play_again()

				#House busts condition
				elif house.best_value() > 21:
					print("\nHouse has busted! You win!!")
					player.win(player_bet*2)
					print(f"\nYou have ${player.bank}")
					playing = play_again()





























