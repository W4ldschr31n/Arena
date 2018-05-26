class Service():
	def __init__(self, service_name=''):
		pass

class Shop():
	#TO DO
	def __init__(self, category, description, products):
		self.category = category
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
		def alchemist():
			return [Service('shop')]

		switch = {
			'inn':inn,
			'smith':smith,
			'alchemist':alchemist,
		}
		self.products = switch.get(self.category, default)()
