import sys

from character import Character
from monster import Troll
from monster import Goblin
from monster import Orc
from monster import Jabberwocky
from monster import Golem
from monster import Dragon


class Game:
	def setup(self):
		self.player = Character()
		self.monsters = [
			Goblin(),
			Troll(),
			Orc(),
			Golem(),
			Jabberwocky(),
			Dragon()]
		self.monster = self.get_next_monster()

	def get_next_monster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None

	def monster_turn(self):
		print("~~~~~~~~~~~~~~VERSUS~~~~~~~~~~~~~~")
		print("{}, HP: {}, EXP: {}".format(self.monster, self.monster.hit_points, self.monster.experience))
		print('='*35 + "\n")
		print("{} has challenged you to combat!".format(self.monster))
		print("The monster lets loose a deafening battlecry: {}!".format(self.monster.sound.upper()))

		if self.monster.attack():
			print("{} is attacking!".format(self.monster))

			if input("Do you want to dodge? [Y/n] ").lower() == 'y':
				if self.player.dodge():
					print("You dodged the attack!")
				else:
					print("You failed to dodge. {} hit you with their {}!".format(self.monster, self.monster.weapon))
					self.player.hit_points -= self.monster.attack
			else:
				print("{} hit you with their {}".format(self.monster, self.monster.weapon))
				self.player.hit_points -= self.monster.attack()
		else:
			print("The monster didn't attack...")

	def player_turn(self):
		player_choice = input("Do you want to [A]ttack, [R]est or [Q]uit? ").lower()

		if player_choice == 'a':
			print("You attack {}!".format(self.monster))

			if self.player.attack():
				if self.monster.dodge():
					print("{} dodged your attack!".format(self.monster))
				else:
					if self.player.level_up():
						self.monster.hit_points -= 2
					else:
						self.monster.hit_points -= 1

					print("You hit {} with your {}!".format(self.monster, self.player.weapon))

			else:
				print("Your attack missed!")
		elif player_choice == 'r':
			self.player.rest()
		elif player_choice == 'q':
			print("Thanks for playing!\nGoodbye!")
			sys.exit()
		else:
			self.player_turn()

	def cleanup(self):
		if self.monster.hit_points <= 0:
			self.player.experience += self.monster.experience
			self.monster = self.get_next_monster()
			print("You beat the monster, but look out! Here comes the next one!")


	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters):
			print("\n" + '='*35)
			print(self.player)
			self.monster_turn()
			print('-'*35)
			self.player_turn()
			self.cleanup()
			print('\n'+'='*35)

		if self.player.hit_points:
			print("Congratulations! You have defeated all the monsters in your path. You WIN!")
		elif self.monster or self.monsters:
			print("AUGH! The monsters proved too strong to overcome. You LOSE!")
		sys.exit()

Game()
