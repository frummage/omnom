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
		self.pelletcount = 164
		config.mariomode = 1
		config.paper = 0

	def getLayout(self):
		if config.players == 1:
			P = 0
			B = 9
		else:
			P = 7
			B = 1
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
			[1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, B, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],\
			[1, 0, 0, 0, 1, 0, 1, 0, 5, 0, 1, 0, 1, 0, 1, 0, 5, 0, 1, 0, 1, 0, 0, 0, 1],\
			[1, 1, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0, 3, 0, 1, 0, P, 0, 1, 1, 1],\
			[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],\
			[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],\
			[1, 0, 1, 3, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 3, 1, 0, 1],\
			[1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, B, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],\
			[1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],\
			[1, 1, 1, 1, 0, 0, 1, 0, 3, 1, 0, 0, 1, 0, 0, 1, 3, 0, 1, 0, 0, 1, 1, 1, 1],\
			[1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],\
			[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],\
			[1, 5, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, B, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 1],\
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

	def getSprites(self):
		block, rect = load_image('marioBlock.png')
		pellet, rect = load_image('coin.png',-1)
		greenMan, rect = load_image('mario.png',-1)
		monster_01, rect = load_image('goomba.png',-1)
		monster_scared_01, rect = load_image('goombaScared.png',-1)
		monster_evil_01, rect = load_image('goombaEvil.png',-1)
		purpleMan, rect = load_image('luigi.png',-1)
		super_pellet, rect = load_image('mushroom.png',-1)
		return [pellet,block,greenMan,monster_01,monster_scared_01,super_pellet,monster_evil_01,purpleMan]

