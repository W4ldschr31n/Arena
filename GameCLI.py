from FightManager import FightManager
from Character import Character
from Arena import Arena
import time

def main():
	player = Character(input('What is your name, slave?\n'), 15)
	orc = Character('Foul orc')
	troll = Character('Fetid troll')
	arena = Arena()
	fight = FightManager(arena, [troll, player], player)
	
	wageFight(fight)

	corpses = fight.arena.corpses

	if fight.hasPlayer():
		print('You survived another fight.')
		#Loot
	elif len(fight.arena.fighters)>0:
		winner = fight.arena.fighters.pop(0)
		print('%s won the fight !'%winner.name)
	else:
		print('Draw ! All fighters lost their lives, the crowd cheers to revive the most brutal.')
		#Continue if fought best
	if(player.isAlive()):
		lootCorpses(player, corpses)

	print(player)
	print(player.belt)
		
	print('End.')

def lootCorpses(player, corpses):
	print('Pick your loot : ')
	for i, c in enumerate(corpses):
		print('%d to loot %s'%(i+1, c))
	try:
		action = int(input())
	except:
		action = -1
	corpseChoice = player.loot(corpses[action-1]) if action>0 and action<=len(corpses) else -1
	for i, l in enumerate(corpseChoice):
		print('%d to loot %s'%(i+1, l))
	try:
		action = int(input())
	except:
		action = -1
	if action>0 and action<=len(corpseChoice):
		player.pickup(corpseChoice[action-1])

def wageFight(fight):
	player = fight.player
	while not fight.isOver():
		for f in fight.arena.fighters:
			print(f)
		
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
	
	def actionAttack():
		pass
	def actionItem():
		pass
	switchAction ={1:actionAttack, 2:actionItem}
	

	action = -1
	while(action not in switchAction):
		try:
			action = int(input('1 to attack\n2 to use item'))
		except:
			print('Please enter a valid action')
	for i, f in enumerate(fighters):
		print('%d to attack %s'%(i+1, f.name))
	try:
		action = int(input())
	except:
		action = -1
	target = fighters[action-1] if action>0 and action<=len(fighters) else player
	if target is not player:
		player.attack(target)
		print('You attack %s !'%target.name)
	else:
		print('You scratch your head.')
		
if __name__ == '__main__':
    main()

