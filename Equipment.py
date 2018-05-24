from .items.Weapon import Weapon
from .items.Armor import Armor

class Equipment():

	def __init__(self, weapon = None, armor = None):
		self.weapon = Weapon() if weapon is None else weapon
		self.armor = Armor() if armor is None else armor
