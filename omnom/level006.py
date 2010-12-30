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
		self.pelletcount = 110
		config.mariomode = 0
		config.paper = 0

	def getLayout(self):
		if config.players == 1:
			P = 0
		else:
			P = 7
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
			[1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1 ,5, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1],\
			[1, 1, 1, 5, 0, 1, 1, 0, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 3, 1],\
			[1, 1, 1, 0, 0, 1, 2, 0, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],\
			[1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0 ,0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 1, 0, 1],\
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1 ,1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],\
			[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 ,0, 1, 1, 1, 1, 1, 0, 1, 1, P, 1, 0, 1],\
			[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 ,1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],\
			[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1 ,0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],\
			[1, 0, 1, 1, 0, 0, 0, 1, 5, 1, 1 ,0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],\
			[1, 0, 1, 1, 0, 1, 3, 1, 0, 1, 1 ,0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],\
			[1, 0, 0, 0, 0, 1, 3, 1, 0, 1, 1 ,0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],\
			[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0, 1, 1, 1, 1, 1, 5, 0, 0, 0, 0, 3, 1],\
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

	def getSprites(self):
		block, rect = load_image('swirlBlock.png')
		pellet, rect = load_image('pellet.png',-1)
		greenMan, rect = load_image('charOpenRight.png',-1)
		monster_01, rect = load_image('monster.png',-1)
		monster_scared_01, rect = load_image('monsterScared.png',-1)
		monster_evil_01, rect = load_image('monsterEvil.png',-1)
		purpleMan, rect = load_image('purpleOpenRight.png',-1)
		super_pellet, rect = load_image('superPellet.png',-1)
		return [pellet,block,greenMan,monster_01,monster_scared_01,super_pellet,monster_evil_01,purpleMan]

