class Shop():
	#TO DO
	def __init__(self, type, description, products):
		self.type = type
		self.description = description
		self.products = products

	def generateStock(self):
		def default():
			return []
		def inn():
			return [Service('sleep')]

		def smith():
			return [Service('upgrade_armor'),
			Service('upgrade_weapon'),
			Service('craft_armor'),
			Service('craft_weapon'),]
			
		switch = {
			'inn',
			'smith',
			'alchemist',
		}
		self.products = switch.get(self.type, default)()
