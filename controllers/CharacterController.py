class CharacterController():

	def __init__(self):
		pass

	def makeAttack(self, character, target):
		dmg = character.attack()
		dmg = target.protect(dmg)
		target.hp -= dmg

	def makeUse(self, character, item, target):
		assert item in character.inventory.items, "%s has no %s."%(character.name, item)
		isDepleted = item.use(target)
		if isDepleted:
			character.inventory.removeItem(item)
		
