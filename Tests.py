from FightManager import FightManager
from CharacterController import CharacterController
from Character import Character
from Corpse import Corpse
from Arena import Arena
from items.Item import HealingPotion
from items.Weapon import Weapon
from items.Armor import Armor
from Inventory import Inventory
import unittest

class CharacterTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('Dummy', 100, 10, 5, Inventory([]))

	def testIsAlive(self):
		self.assertTrue(self.dummy.isAlive())
		self.dummy.hp = 0
		self.assertFalse(self.dummy.isAlive())

	def testAttack(self):
		self.assertEqual(self.dummy.attack(), 10)

	def testProtect(self):
		self.assertEqual(self.dummy.protect(10), 5)

	def testPickUpConsummable(self):
		potion = HealingPotion()
		self.dummy.pickup(potion)
		self.assertIn(potion, self.dummy.inventory.items)

	def testPickUpWeapon(self):
		sword = Weapon('Sword', '1hsw', 2)
		self.dummy.pickup(sword)
		self.assertEqual(self.dummy.equipment.weapon, sword)

class CharacterControllerTest(unittest.TestCase):

	def setUp(self):
		self.charController = CharacterController()
		self.dummy = Character('Dummy', 100, 10, 0, Inventory([HealingPotion('normal')]))
		self.dummy2 = Character('Dummy', 5, 0, 5)

	def testMakeAttack(self):
		self.charController.makeAttack(self.dummy, self.dummy2)
		self.assertFalse(self.dummy2.isAlive())

	def testMakeUse(self):
		self.dummy2.hp = 1
		self.charController.makeUse(self.dummy, self.dummy.inventory.items[0], self.dummy2)
		self.assertEqual(self.dummy2.hp, self.dummy2.maxHp)
		self.assertFalse(self.dummy.inventory.items)

class CorpseTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('dummy', 1, 0, 0, Inventory([HealingPotion()]))
		self.corpse = Corpse(self.dummy)

	def testCreationItems(self):
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
		dummy = Character('dummy', 20, 0, 0, Inventory([HealingPotion('normal')]))
		dummy.hp = 5
		charController = CharacterController()
		charController.makeUse(dummy, dummy.inventory.items[0], dummy)
		self.assertEqual(dummy.hp, 15)
		self.assertFalse(dummy.inventory.items)
		dummy.pickup(self.potion)
		charController.makeUse(dummy, dummy.inventory.items[0], dummy)
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
		self.dummy.hp = 0
		self.arena.updateFighters()
		self.arena.clean()
		self.assertFalse(self.arena.fighters)
		self.assertFalse(self.arena.corpses)

		
