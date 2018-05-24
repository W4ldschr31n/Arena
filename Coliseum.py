from .Corpse import Corpse

class Coliseum():
	def __init__(self):
		self.fighters = []
		self.corpses = []

	def startFight(self,fighters):
		self.fighters = fighters

	def updateFighters(self):
		for i, f in enumerate(self.fighters):
			if not f.isAlive():
				self.corpses.append(Corpse(self.fighters.pop(i)))

	def clean(self):
		self.fighters = []
		self.corpses = []
