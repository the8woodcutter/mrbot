# !/usr/bin/env python3.10

import random

class BlackJack():

	###	TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO ##
		### TODO: dealer shows one card :TODO
		### TODO: create functions for dealer play, bust and blackjack :TODO
		### TODO: make it so that player cards all REMAIN with their indexes :TODO
		### TODO: declare all variables globally as empty types, for reference on their intended types :TODO
		### TODO: consider a NEW naming scheme :TODO
	###	TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO ##

	scs = [] # spade cards
	hcs = [] # heart cards
	ccs = [] # club cards
	dcs = [] # diamond cards
	sfv = [] # spade face value
	hfv = [] # heart face value
	cfv = [] # club face value
	dfv = [] # diamond face value
	cs = [] # cards
	fvs = [] # face values
	fv = str() # face value
	c = str() # card
	r = int() # randint
	pc1 = [] # player card 1
	pc2 = [] # player card 2
	pc3 = [] # player card 3
	pc4 = [] # player card 4
	pc5 = [] # player card 5
	dc1 = [] # dealer card 1
	dc2 = [] # dealer card 2
	dc3 = [] # dealer card 3
	dc4 = [] # dealer card 4
	dc5 = [] # dealer card 5
	pcs = str() # player cards
	dcs = str() # dealer cards
	ph = int() # player hand
	dh = int() # dealer hand

	def give_card(self):
		spade = {"SA": "🂡", "S2": "🂢", "S3": "🂣", "S4": "🂤", "S5": "🂥", "S6": "🂦", "S7": "🂧", "S8": "🂨", "S9": "🂩", "S10": "🂪" ,"SJ": "🂫", "SQ": "🂭", "SK": "🂮"}
		heart = {"HA": "🂱", "H2": "🂲", "H3": "🂳", "H4": "🂴", "H5": "🂵", "H6": "🂶", "H7": "🂷", "H8": "🂸", "H9": "🂹", "H10": "🂺", "HJ": "🂻", "HQ": "🂽", "HK": "🂾"}
		club = {"CA": "🃑", "C2": "🃒", "C3": "🃓", "C4": "🃔", "C5": "🃕", "C6": "🃖", "C7": "🃗", "C8": "🃘", "C9": "🃙", "C10": "🃚" ,"CJ": "🃛", "CQ": "🃝", "CK": "🃞"}
		diamond = {"DA": "🃁", "D2": "🃂", "D3": "🃃", "D4": "🃄", "D5": "🃅", "D6": "🃆", "D7": "🃇", "D8": "🃈", "D9": "🃉", "D10": "🃊" ,"DJ": "🃋", "DQ": "🃍", "DK": "🃎"}
		# We can correlate the index numbers of these resulting lists with the index numbers of the next bit:
		scs = list(spade.values())
		hcs = list(heart.values())
		ccs = list(club.values())
		dcs = list(diamond.values())
		# The index numbers of these resulting lists can correlate with the index numbers of the above 4 lists:
		sfv = list(spade.keys())
		hfv = list(heart.keys())
		cfv = list(club.keys())
		dfv = list(diamond.keys())
		# To get an entire deck of cards and facevalues, with their indexes preserved, we append the lists:
		cs = list(scs + hcs + ccs + dcs)
		fvs = list(sfv + hfv + cfv + dfv)
		# A test to make sure we get the correct face_values from cards:
		r = random.randint(1,52) - 1
		c = cs[r]
		fv = fvs[r]
		return c, fv

	def hand_value(self, hand, hit):
		self.hand = hand
		face_cards = ["10","J","Q","K"]
		ace = "A"
		if ininstance(hand, list):
			for cd in hand:
				if ininstance(c, str):
					cd = cd[1:]
					if cd in face_cards:
						cd = 10
					elif cd == ace:
						cd = 11
					else:
						cd = int(cd)
					hand.append(cd)
			hand = sum(hand)
			return hand_value

	def start_deal(self):
		start = input("Deal a game of BlackJack?  (y/n)?")
		if start != "y":
			print("Cya!")
			exit()
		else:
			# each a list with two strings, card and face_value
			pc1 = self.give_card()
			dc1 = self.give_card()
			pc2 = self.give_card()
			dc2 = self.give_card()

			dh = self.hand_value(list(dc1[1], dc2[1]), 0)
			ph = self.hand_value(list(pc1[1], pc2[1]), 0)

			dcs = str(dc1[0] + " " + dc2[0])
			pcs = str(pc1[0] + " " + pc2[0])

			if int(ph) > 21:
				# bust()
				pass
			elif int(ph) == 21:
				# dealer()
				pass
			else:

		###	### TODO: dealer shows one card :TODO ###
		### TODO: dealer shows one card :TODO ### ###
		###	### TODO: dealer shows one card :TODO ###
		### TODO: dealer shows one card :TODO ### ###
		###	### TODO: dealer shows one card :TODO ###

				# execute delivery of cards
				print(f"Your cards are: {pcs} [value: {ph}]\r\n")
				self.hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand)

	def hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand):
		hit_or_stay = input("Hit or Stay?\r\n")
		hits = ["Hit", "hit", "h", "H", "Hit me", "hit me", "Hit me!", "Hit Me!", "Hit Me", "tap", "++", "y", "Y"]
		stays = ["Stay", "stay", "s", "hold", "Hold", "h", "H", "n", "N", "--"]
		
		if hit_or_stay in hits:
			player_card_3 = self.give_card()
			c = player_card_3[1:]
			face_cards = ["10","J","Q","K"]
			ace = "A"
			
			if c in face_cards:
				c = 10
			elif c == ace:
				c = 11
			else:
				c = player_card_3[1:]

			self.player_cards = player_cards
			player_cards = str(player_cards + " " + player_card_3[0])
			player_hand = int(player_hand + c)
			
			if player_hand == 21:
				# dealer()
				pass
			elif player_hand > 21:
				# bust()
				pass
			else:
				hit_or_stay(self, dealer_cards, player_cards, dealer_hand, player_hand)

		if hit_or_stay in stays:
			# dealer()
			pass

	def bust(self):
		pass

	def dealer():
		pass

	def blackjack(self, player_cards):
		pass


	# ♠ = cards.spade
	# ♥ = cards.heart
	# ♣ = cards.club
	# ♦ = cards.diamond