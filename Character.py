from Item import HealingPotion

class Character():

	def __init__(self, name, hp=10, strength=5, toughness=1, belt = [HealingPotion()], armor=None, weapon=None):
		self.name = name
		self.maxHp = hp
		self.hp = hp
		self.strength = strength
		self.toughness = toughness
		self.armor = armor
		self.weapon = weapon
		self.belt = belt


	def attack(self, other):
		dmg = self.strength
		if self.weapon:
			dmg = dmg + self.weapon.getDamages()
		other.takeDamages(dmg)

	def takeDamages(self, dmg):
		if self.armor:
			dmg = self.armor.protect(dmg)
		dmg = dmg - self.toughness
		self.hp = self.hp - dmg

	def pickup(self, item):
		def default():
			self.belt.append(item)
		def w():
			self.weapon = item
		def a():
			self.armor = item
		switch = {
			'Weapon':w,
			'Armor':a,
			}
		switch.get(type(item), default)()

	def use(self, item, target):
		item.use(target)

	def isAlive(self):
		return self.hp > 0 

	def loot(self, corpse):
		return corpse.items

	def __str__(self):
		return self.name + (' is alive with %s HP'%self.hp if self.isAlive() else ' is dead ')\
			+ ', carrying ' + (str(self.armor) if self.armor else 'no armor')\
			+ ' and wielding ' + (str(self.weapon) if self.weapon else 'no weapon') + '.'


