import random

from combat import Combat


class Character(Combat):
	attack_limit = 30
	experience = 0
	base_hit_points = 15
	dodge_limit = 15

	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'sword':
			roll += 1
		elif self.weapon == 'axe':
			roll += 4
		elif self.weapon == 'bow':
			roll += 3
		return roll > 4

	def get_weapon(self):
		weapon_choice = input("Choose Your Weapon ([S]word, [A]xe, [B]ow): ").lower()

		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return 'sword'
			elif weapon_choice == 'a':
				return 'axe'
			else:
				return 'bow'
		else:
			return self.get_weapon()

	def __init__(self, **kwargs):
		self.name = input("Name Your Character: ")
		self.weapon = self.get_weapon()
		self.hit_points = self.base_hit_points

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return '{}, HP: {}, EXP: {}'.format(self.name, self.hit_points, self.experience)

	def rest(self):
		if self.hit_points < self.base_hit_points:
			self.hit_points += 5

	def level_up(self):
		return self.experience >= 5
