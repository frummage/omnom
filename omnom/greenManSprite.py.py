#!/usr/bin/env python

import logging
import pygame
import pygame.locals

import basicSprite


_moduleLogger = logging.getLogger(__name__)


SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START + 1
PLAYER_EATEN = SUPER_STATE_OVER + 1


class greenMan(basicSprite.Sprite):
	def __init__(self, centerPoint, image):
		basicSprite.Sprite.__init__(self, centerPoint, image)
		self.pellets = 0
		self.x_dist = 8
		self.y_dist = 8
		self.xMove = 0
		self.yMove = 0
		self.superState = False

	def MoveKeyDown(self, key):
		if (key == pygame.locals.K_RIGHT):
			self.xMove += self.x_dist
		elif (key == pygame.locals.K_LEFT):
			self.xMove += -self.x_dist
		elif (key == pygame.locals.K_UP):
			self.yMove += -self.y_dist
		elif (key == pygame.locals.K_DOWN):
			self.yMove += self.y_dist

	def MoveKeyUp(self, key):
		if (key == pygame.locals.K_RIGHT):
			self.xMove += -self.x_dist
		elif (key == pygame.locals.K_LEFT):
			self.xMove += self.x_dist
		elif (key == pygame.locals.K_UP):
			self.yMove += self.y_dist
		elif (key == pygame.locals.K_DOWN):
			self.yMove += -self.y_dist

	def update(self, block_group, pellet_group, super_pellet_group, monster_group):
		if (self.xMove==0)and(self.yMove==0):
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
			elif (len(pygame.sprite.spritecollide(self, super_pellet_group, True))>0):
				self.superState = True
				pygame.event.post(pygame.event.Event(SUPER_STATE_START, {}))
				pygame.time.set_timer(SUPER_STATE_OVER, 0)
				pygame.time.set_timer(SUPER_STATE_OVER, 8000)

	def MonsterCollide(self, lstMonsters):
		if(len(lstMonsters)<=0):
			return
		for monster in lstMonsters:
			if (monster.scared):
				monster.Eaten()
			else:
				pygame.event.post(pygame.event.Event(PLAYER_EATEN, {}))
