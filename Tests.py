from Arena.controllers.FightController import FightController
from Arena.controllers.CharacterController import CharacterController
from Arena.characters.Character import Character
from Arena.characters.Corpse import Corpse
from Arena.environments.Coliseum import Coliseum
from Arena.items.Item import HealingPotion
from Arena.items.Weapon import Weapon
from Arena.items.Armor import Armor
from Arena.items.Inventory import Inventory
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
		sword = Weapon('Sword', 2)
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

class ColiseumTest(unittest.TestCase):

	def setUp(self):
		self.dummy = Character('Dummy')
		self.dummy2 = Character('Dummy2')
		self.coliseum = Coliseum()
		self.fighters = [self.dummy, self.dummy2]

	def testUpdateFighters(self):
		self.coliseum.startFight(self.fighters)
		self.assertEqual(len(self.coliseum.fighters), len(self.fighters))
		self.dummy.hp = 0
		self.coliseum.updateFighters()
		self.assertEqual(len(self.coliseum.fighters), 1)
		self.assertEqual(len(self.coliseum.corpses), 1)

	def testClean(self):
		self.coliseum.startFight(self.fighters)
		self.dummy.hp = 0
		self.coliseum.updateFighters()
		self.coliseum.clean()
		self.assertFalse(self.coliseum.fighters)
		self.assertFalse(self.coliseum.corpses)
