from items.Item import HealingPotion
from Inventory import Inventory
from Equipment import Equipment

class Character():

	def __init__(self, name, hp=10, strength=5, toughness=1, inventory = None, equipment = None):
		self.name = name
		self.maxHp = hp
		self.hp = hp
		self.strength = strength
		self.toughness = toughness
		self.equipment = Equipment() if equipment is None else equipment
		self.inventory = Inventory([HealingPotion()]) if inventory is None else inventory

	def attack(self):
		#Bare-hands attack
		dmg = self.strength
		if self.equipment.weapon:
			dmg = dmg + self.equipment.weapon.getDamages()
		return dmg

	def protect(self, dmg):
		if self.equipment.armor:
			dmg = self.equipment.armor.protect(dmg)
		dmg = dmg - self.toughness
		return max(dmg, 0)

	def pickup(self, item):
		def default():
			self.inventory.addItem(item)
		def w():
			self.equipment.weapon = item
		def a():
			self.equipment.armor = item
		switch = {
			'Weapon':w,
			'Armor':a,
			}
		switch.get(type(item).__name__, default)()

	def isAlive(self):
		return self.hp > 0 

	def __str__(self):
		return self.name + (' is alive with %s HP'%self.hp if self.isAlive() else ' is dead ')\
			+ ', carrying ' + (str(self.equipment.armor) if self.equipment.armor else 'no armor')\
			+ ' and wielding ' + (str(self.equipment.weapon) if self.equipment.weapon else 'no weapon') + '.'


