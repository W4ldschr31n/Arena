from FightManager import FightManager
from CharacterController import CharacterController
from Character import Character
from Equipment import Equipment
from items.Weapon import Weapon
from items.Armor import Armor
from Arena import Arena
import time
import sys

charController = CharacterController()

def readAction(string=''):
	try:
		action = int(input(string))
	except KeyboardInterrupt:
		print('Exiting...')
		sys.exit()
	except:
		action = -1
	return action

def main():
	player = Character(input('What is your name, slave?\n'), 15)
	orc = Character('Foul orc')
	troll = Character('Fetid troll')
	knight = Character('Knight', 10, 5, 1, None, Equipment(Weapon('Sword','1hsw',2), Armor('Shiny armor', 1)))
	arena = Arena()
	fight = FightManager(arena, [player, orc, troll, knight], player)

	print('You enter the arena.')
	print(knight.equipment.weapon)
	
	wageFight(fight)

	corpses = fight.arena.corpses

	if fight.hasPlayer():
		print('You survived another fight.')
		#Loot and continue
		lootCorpses(player, corpses)
	elif len(fight.arena.fighters)>0:
		winner = fight.arena.fighters.pop(0)
		print('%s won the fight !'%winner.name)
	else:
		print('Draw ! All fighters lost their lives, the crowd cheers to revive the most brutal.')
		#Continue if fought best
		
	print(player)
	print(player.inventory.items)
		
	print('End.')

def lootCorpses(player, corpses):
	print('Pick your loot : ')
	for i, c in enumerate(corpses):
		print('%d to loot %s'%(i+1, c))
	action = readAction()
	corpseChoice = corpses[action-1].items if action>0 and action<=len(corpses) else -1
	if corpseChoice == -1:
		print("You don't loot.")
		return 1
	for i, l in enumerate(corpseChoice):
		print('%d to loot %s'%(i+1, l))
	action = readAction()
	if action>0 and action<=len(corpseChoice):
		player.pickup(corpseChoice[action-1])
	else:
		print("You don't loot")
		return 1
	return 0

def wageFight(fight):
	player = fight.player
	while not fight.isOver():
		print("="*60)
		for f in fight.arena.fighters:
			print(f)
		print("="*30)		
		#Player turn
		if fight.hasPlayer():
			playerTurn(player, fight)
		else:
			time.sleep(1)
		#Enemy turn
		fight.playNPCTurns()
		fight.update()

def playerTurn(player, fight):
	fighters = fight.arena.fighters
	endTurn = 0

	def default():
		print('You scratch your head')
		return 0
	
	def actionAttack():
		print('Choose someone to attack')
		for i, f in enumerate(fighters):
			print('%d to attack %s'%(i+1, f.name))
		action = readAction()
		if action>0 and action<=len(fighters):
			target = fighters[action-1]
		else:
			print('You scratch your head.')
			return 0
		if target is not player:
			charController.makeAttack(player,target)
			print('You attack %s !'%target.name)
		else:
			print('You hurt yourself.')
		return 1
			
	def actionItem():
		items = player.inventory.items
		if len(items)==0:
			print('No items in inventory')
			return 0
		print('Choose an item to use')
		for i, item in enumerate(items):
			print('%d to use %s : %s'%(i+1, item, item.desc()))
		action = readAction()
		if action>0 and action<=len(items):
			item = items[action-1]
			print('You use %s !'%item)
			charController.makeUse(player, items[action-1], player)
		else:
			print('You scratch your head.')
		for f in fight.arena.fighters:
			print(f)
		return 0
		
	switchAction ={1:actionAttack, 2:actionItem}

	while(endTurn==0):
		action = -1
		while(action not in switchAction):
			action = readAction('1 to attack\n2 to use an item\n')
			if action<0:
				for f in fight.arena.fighters:
					print(f)
		
			#Play the action
			endTurn = switchAction.get(action, default)()
		
if __name__ == '__main__':
	main()

