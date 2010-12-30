#!/usr/bin/env python

import pygame
import basicSprite
import config

import helpers


SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START + 1
PLAYER_EATEN = SUPER_STATE_OVER + 1
#BITE = pygame.USEREVENT + 1
#KILL = pygame.USEREVENT + 1
#SUPER = pygame.USEREVENT + 1

biteSound = None
superSound = None
killSound = None


class purpleMan(basicSprite.Sprite):

	def __init__(self, centerPoint, image):
		basicSprite.Sprite.__init__(self, centerPoint, image)
		#nom.gameMusic
		#nom.gameSound
		#nom.player_speed
		#nom.enemy_speed
		#centerPoint = self.image.get_center()
		config.purpleHits = 0
		self.openclosed = 1
		self.normal_image = self.image
		if config.mariomode == 1:
			self.closed, rect = helpers.load_image('luigiClosed.png', -1)
		elif config.paper == 1:
			self.closed, rect = helpers.load_image('purplePaperClosed.png', -1)
		else:
			self.closed, rect = helpers.load_image('purpleClosedRight.png', -1)
		self.rect.inflate_ip(-6, -6)
		self.original_rect = pygame.Rect(self.rect)
		#self.rect.center = (100, 160)
		self.lives = config.lives
		self.pellets = 0
		self.x_dist = config.player_speed
		self.y_dist = config.player_speed
		self.xMove = 0
		self.yMove = 0
		self.superState = False
		self.hdirect = 2
		self.vdirect = 0
		#self.charcenter = centerPoint
		#self.rect.inflate_ip(-6, -6)
		#pygame.mixer.init()
		global biteSound
		global superSound
		global killSound
		if  config.mariomode == 1:
			biteSound = pygame.mixer.Sound('data/sounds/coin.wav')
			superSound = pygame.mixer.Sound('data/sounds/mushroom.wav')
			killSound = pygame.mixer.Sound('data/sounds/kick.wav')
		else:
			biteSound = pygame.mixer.Sound('data/sounds/bite.wav')
			superSound = pygame.mixer.Sound('data/sounds/super.wav')
			killSound = pygame.mixer.Sound('data/sounds/kill.wav')

	def OpenAndClose(self):
		if self.openclosed == 1:
			self.current_rect = self.rect
			self.image = self.closed
			self.rect = self.current_rect
			self.openclosed = 2
		else:
			self.current_rect = self.rect
			self.image = self.normal_image
			self.rect = self.current_rect
			self.openclosed = 1
		if self.hdirect == 1:
			self.image = pygame.transform.flip(self.image, 1, 0)
		if self.vdirect == 2:
			if self.hdirect == 1:
				self.image = pygame.transform.rotate(self.image, -90)
			elif self.hdirect == 2:
				self.image = pygame.transform.rotate(self.image, 90)
		elif self.vdirect == 1:
			if self.hdirect == 1:
				self.image = pygame.transform.rotate(self.image, 90)
			if self.hdirect == 2:
				self.image = pygame.transform.rotate(self.image, -90)

	def MoveKeyDown(self, key):
		if (key == pygame.locals.K_x):
			self.xMove += self.x_dist
			if self.hdirect == 1:
				self.image = pygame.transform.flip(self.image, 1, 0)
				self.hdirect = 2
		elif (key == pygame.locals.K_a):
			self.xMove += -self.x_dist
			if self.hdirect == 2:
				self.image = pygame.transform.flip(self.image, 1, 0)
				self.hdirect = 1
		elif (key == pygame.locals.K_s):
			self.yMove += -self.y_dist
			if self.vdirect == 0:
				if self.hdirect == 2:
					self.image = pygame.transform.rotate(self.image, 90)
				if self.hdirect == 1:
					self.image = pygame.transform.rotate(self.image, -90)
			self.vdirect = 2
		elif (key == pygame.locals.K_z):
			self.yMove += self.y_dist
			if self.vdirect == 0:
				if self.hdirect == 2:
					self.image = pygame.transform.rotate(self.image, -90)
				if self.hdirect == 1:
					self.image = pygame.transform.rotate(self.image, 90)
			self.vdirect = 1

	def MoveKeyUp(self, key):
		control = 1
		if self.openclosed == 2:
			self.image = self.normal_image
			self.OpenAndClose()
		if (key == pygame.locals.K_x):
			self.xMove += -self.x_dist
		elif (key == pygame.locals.K_a):
			self.xMove += self.x_dist
		elif (key == pygame.locals.K_s):
			self.yMove += self.y_dist
			if self.hdirect == 2:
				self.image = pygame.transform.rotate(self.image, -90)
			if self.hdirect == 1:
				self.image = pygame.transform.rotate(self.image, 90)
			self.vdirect = 0
		elif (key == pygame.locals.K_z):
			self.yMove += -self.y_dist
			if self.hdirect == 2:
				self.image = pygame.transform.rotate(self.image, 90)
			if self.hdirect == 1:
				self.image = pygame.transform.rotate(self.image, -90)
			self.vdirect = 0

	def update(self, block_group, pellet_group, super_pellet_group, monster_group):
		if (self.xMove==0)and(self.yMove==0):
			lst_monsters = pygame.sprite.spritecollide(self, monster_group, False)
			if (len(lst_monsters)>0):
				self.MonsterCollide(lst_monsters)
			else:
				return
		self.rect.move_ip(self.xMove, self.yMove)
		if pygame.sprite.spritecollideany(self, block_group):
			self.rect.move_ip(-self.xMove, -self.yMove)
		lst_monsters = pygame.sprite.spritecollide(self, monster_group, False)
		if (len(lst_monsters)>0):
			self.MonsterCollide(lst_monsters)
		else:
			lstCols = pygame.sprite.spritecollide(self, pellet_group, True)
			if (len(lstCols)>0):
				self.pellets += len(lstCols)
				global biteSound
				global level1
				#Sound.stop()
				self.OpenAndClose()
				if config.gameSound == 1:
					#pygame.event.post(pygame.event.Event(BITE, {}))
					biteSound.play(loops=0, maxtime=0, fade_ms=0)
			elif (len(pygame.sprite.spritecollide(self, super_pellet_group, True))>0):
				self.superState = True
				if config.gameSound == 1:
					global superSound
					#Sound.stop()
					#pygame.event.post(pygame.event.Event(SUPER, {}))
					superSound.play(loops=0, maxtime=0, fade_ms=0)
				pygame.event.post(pygame.event.Event(SUPER_STATE_START, {}))
				pygame.time.set_timer(SUPER_STATE_OVER, 0)
				pygame.time.set_timer(SUPER_STATE_OVER, 8000)

	def MonsterCollide(self, lstMonsters):
		if(len(lstMonsters)<=0):
			return
		for monster in lstMonsters:
			global killSound
			if (monster.scared):
				monster.Eaten()
				config.purpleHits = config.purpleHits+1
				if config.gameSound == 1:
					#killSound.stop()
					#pygame.event.post(pygame.event.Event(KILL, {}))
					killSound.play(loops=0, maxtime=0, fade_ms=0)
			else:
				self.lives = self.lives-1
				if self.lives >= 1:
					self.rect = self.original_rect
				if config.players == 2:
					if self.lives == 0:
						self.rect = self.rect.move(-800, -800)
				if config.gameSound == 1:
					#killSound.stop()
					#pygame.event.post(pygame.event.Event(KILL, {}))
					killSound.play(loops=0, maxtime=0, fade_ms=0)
				pygame.event.post(pygame.event.Event(PLAYER_EATEN, {}))
