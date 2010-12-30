#!/usr/bin/env python

import levelBase
import config
from helpers import load_image

class level(levelBase.Level):
	def __init__(self):
		self.BLOCK = 1
		self.GREENMAN = 2
		self.PELLET = 0
		self.MONSTER = 3
		self.SCARED_MONSTER = 4
		self.EVIL_MONSTER = 6
		self.PURPLEMAN = 7
		self.SUPER_PELLET = 5
		self.pelletcount = 0
		config.paper = 0

	def getLayout(self):
		if config.players == 1:
			P = 9
		else:
			P = 7
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 5, 9, 9, 9, 9, 9, 9 , 9, 2, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 1], \
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 1, P, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 , 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], \
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

	def getSprites(self):
		block, rect = load_image('blackBlock.png')
		pellet, rect = load_image('no.png', -1)
		greenMan, rect = load_image('charOpenRight.png', -1)
		monster_01, rect = load_image('monster.png', -1)
		monster_scared_01, rect = load_image('monsterScared.png', -1)
		monster_evil_01, rect = load_image('monsterEvil.png', -1)
		purpleMan, rect = load_image('purpleOpenRight.png', -1)
		super_pellet, rect = load_image('yes.png', -1)
		return [pellet, block, greenMan, monster_01, monster_scared_01, super_pellet, monster_evil_01, purpleMan]

