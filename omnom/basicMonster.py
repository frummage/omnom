#!/usr/bin/env python

import pygame
import basicSprite
import random
import config


isEvil = False


class Monster(basicSprite.Sprite):

	def __init__(self, centerPoint, image, scared_image=None, evil_image=None):
		basicSprite.Sprite.__init__(self, centerPoint, image)
		global isEvil
		#if test == 1:
		isEvil = False
		self.original_rect = pygame.Rect(self.rect)
		#test = 0
		self.normal_image = image
		self.evil_image = evil_image
		if scared_image is not None:
			self.scared_image = scared_image
		else:
			self.scared_image = image
		self.scared = False
		self.direction = random.randint(1, 4)
		if config.boss == 1:
			self.dist = config.player_speed+4
			self.moves = random.randint(10, 60)
		else:
			self.dist = config.enemy_speed
			self.moves = random.randint(60, 120)
		self.moveCount = 0

	def update(self, block_group):
		xMove, yMove = 0, 0
		if self.direction == 1:
			xMove = -self.dist
		elif self.direction == 2:
			yMove = -self.dist
		elif self.direction == 3:
			xMove = self.dist
		elif self.direction == 4:
			yMove = self.dist

		self.rect.move_ip(xMove, yMove)
		self.moveCount += 1
		if pygame.sprite.spritecollideany(self, block_group):
			self.rect.move_ip(-xMove, -yMove)
			self.direction = random.randint(1, 4)
		elif self.moves == self.moveCount:
			self.direction = random.randint(1, 4)
			self.moves = random.randint(100, 200)
			self.moveCount = 0

	def SetScared(self, scared):
		if self.image == self.evil_image:
			return
		else:
			if self.scared != scared:
				self.scared = scared
				if scared:
					self.image = self.scared_image
				else:
					self.image = self.normal_image

	def Eaten(self):
		self.rect = self.original_rect
		self.scared = False
		self.image = self.evil_image
		global isEvil
		isEvil = True
