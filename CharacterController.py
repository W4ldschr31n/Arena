class CharacterController():

	def __init__(self):
		pass

	def makeAttack(self, character, target):
		dmg = character.attack()
		dmg = target.protect(dmg)
		target.hp -= dmg

	def makeUse(self, character, item, target):
		assert item in character.belt, "You don't have that item"
		isDepleted = item.use(target)
		if isDepleted:
			character.belt.remove(item)
		
