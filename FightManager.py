import random

class FightManager():
	def __init__(self, arena, fighters, player=None):
		self.arena = arena
		self.arena.startFight(fighters)
		self.player = player

	def isOver(self):
		return len(self.arena.fighters)<=1

	def hasPlayer(self):
		return self.player is not None and self.player in self.arena.fighters

	def playNPCTurns(self):
		npcs = [f for f in filter(lambda x:x is not self.player, self.arena.fighters)]
		for f in npcs:
			target = random.choice(self.arena.fighters)
			if target is f:
				pass
				print('%s scratches his head.'%f.name)
			else:
				f.attack(target)
				print('%s attacks %s !'%(f.name, target.name))
			
	def update(self):
		self.arena.updateFighters()
