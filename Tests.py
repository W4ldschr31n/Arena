from FightManager import FightManager
from Character import Character
from Corpse import Corpse
import unittest
from Arena import Arena
from Item import HealingPotion

class CharacterTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('Dummy', 100, 10, 0, [])

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

	def testPickUp(self):
		potion = HealingPotion()
		self.dummy.pickup(potion)
		self.assertIn(potion, self.dummy.belt)

class CorpseTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('dummy', 0, 0, [HealingPotion()])
		self.corpse = Corpse(self.dummy)

	def testCreationBelt(self):
		self.assertEqual(self.corpse.name, self.dummy.name)
		self.assertTrue(self.corpse.items)

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
		dummy = Character('dummy', 20, 15, 0, [HealingPotion('normal')])
		dummy.attack(dummy)
		dummy.use(dummy.belt[0], dummy)
		self.assertEqual(dummy.hp, 15)
		self.assertFalse(dummy.belt)
		dummy.pickup(self.potion)
		dummy.use(dummy.belt[0], dummy)
		self.assertEqual(dummy.hp, 20)

class ArenaTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('Dummy')
		self.dummy2 = Character('Dummy2')
		self.arena = Arena()
		self.fighters = [self.dummy, self.dummy2]

	def testUpdateFighters(self):
		self.arena.startFight(self.fighters)
		self.assertEqual(len(self.arena.fighters), len(self.fighters))
		self.dummy.hp = 0
		self.arena.updateFighters()
		self.assertEqual(len(self.arena.fighters), 1)
		self.assertEqual(len(self.arena.corpses), 1)

	def testClean(self):
		self.arena.startFight(self.fighters)
		self.dummy.hp =0
		self.arena.updateFighters()
		self.arena.clean()
		self.assertFalse(self.arena.fighters)
		self.assertFalse(self.arena.corpses)

		
