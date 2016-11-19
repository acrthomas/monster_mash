import random

from combat import Combat

COLORS = [
			'purple', 'blue', 'green', 'yellow', 'orange', 'emerald',
			'ruby', 'sapphire', 'red', 'pink', 'gold', 'silver', 'amethyst',
			'diamond', 'garnet', 'topaz', 'burgundy', 'maroon', 'crystal'
			]

class Monster(Combat):

	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

	def __init__(self, **kwargs):
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)
		self.sound
		self.weapon

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return "{} {}".format(self.color.title(),
							  self.__class__.__name__)

class Goblin(Monster):
	max_hit_points = 3
	max_experience = 2
	sound = 'squeak'
	weapon = 'dagger'

class Orc(Monster):
	min_hit_points = 5
	max_hit_points = 10
	max_experience = 10
	attack_limit = 14
	sound = 'groooar'
	weapon = 'cleaver'

class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 6
	min_experience = 2
	max_experience = 6
	attack_limit = 10
	sound = 'gruah'
	weapon = 'club'

class Jabberwocky(Monster):
	min_hit_points = 10
	max_hit_points = 20
	min_experience = 5
	max_experience = 15
	attack_limit = 19
	sound = 'jibber jabber'
	weapon = 'claws'

class Golem(Monster):
	min_hit_points = 7
	max_hit_points = 14
	min_experience = 4
	max_experience = 12
	attack_limit = 16
	sound = 'gruuuu'
	weapon = 'fists'

class Dragon(Monster):
	min_hit_points = 15
	max_hit_points = 30
	min_experience = 6
	max_experience = 18
	attack_limit = 22
	sound = 'brimstone, hellfire and damnation'
	weapon = 'firebreath'
