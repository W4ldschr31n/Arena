from FightManager import FightManager
from Character import Character
import unittest
from Item import HealingPotion

class CharacterTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('Dummy', 100, 10, 0)

	def testTakeDamages(self):
		self.dummy.takeDamages(25)
		self.assertEqual(self.dummy.hp, 75)
		self.dummy.toughness = 10
		self.dummy.takeDamages(25)
		self.assertEqual(self.dummy.hp, 60)

	def testIsAlive(self):
		self.assertTrue(self.dummy.isAlive())
		self.dummy.hp = 0
		self.assertFalse(self.dummy.isAlive())

	def testAttack(self):
		dummy2 = Character('Dummy2', 10, 0, 0)
		self.dummy.attack(dummy2)
		self.assertFalse(dummy2.isAlive())

class HealingPotionTest(unittest.TestCase):

	def setUp(self):
		self.potion = HealingPotion('normal')

	def testUpgrade(self):
		self.potion.upgrade()
		self.assertEqual(self.potion.quality, 'greater')
		self.assertEqual(self.potion.heal, HealingPotion.healParams['greater'])

		self.potion.upgrade()
		self.assertEqual(self.potion.quality, 'greater')
		self.assertEqual(self.potion.heal, HealingPotion.healParams['greater'])

	def testUse(self):
		dummy = Character('dummy', 20, 15, 0, HealingPotion('normal'))
		dummy.attack(dummy)
		dummy.use(dummy.belt[0], dummy)
		self.assertEqual(dummy.hp, 15)
		self.assertNotIn(self.potion, dummy.belt)
		dummy.use(self.potion, dummy)
		self.assertEqual(dummy.hp, 20)
		
