#!/usr/bin/env python

import logging
import pygame

import helpers


_moduleLogger = logging.getLogger(__name__)


class Sprite(pygame.sprite.Sprite):
	def __init__(self, centerPoint, image):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = image.get_rect()
		self.rect.center = centerPoint


class pellet(pygame.sprite.Sprite):
	def __init__(self, top_left, image = None):
		pygame.sprite.Sprite.__init__(self)
		if image == None:
			self.image, self.rect = helpers.load_image('pellet.png', -1)
		else:
			self.image = image
			self.rect = image.get_rect()
		self.rect.topleft = top_left

