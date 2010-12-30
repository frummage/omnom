#!/usr/bin/env python

from __future__ import with_statement
from __future__ import division

import os
import simplejson
import logging
import pygame

import config
import helpers


_moduleLogger = logging.getLogger(__name__)


class LevelLoader(object):

	PELLET = 0
	BLOCK = 1
	GREENMAN = 2
	MONSTER = 3
	SCARED_MONSTER = 4
	SUPER_PELLET = 5
	EVIL_MONSTER = 6
	PURPLEMAN = 7
	EMPTY = 9
	GREENMAN_CLOSED = 20
	PURPLEMAN_CLOSED = 21

	_SYMBOL_TO_VALUE = {
		"#": BLOCK,
		"G": GREENMAN,
		"P": PURPLEMAN,
		".": PELLET,
		"M": MONSTER,
		"*": SUPER_PELLET,
		" ": EMPTY,
	}

	def __init__(self, dataFolder, levelFile):
		self._dataFolder = dataFolder
		self._pelletCount = 0

		with open(levelFile) as f:
			self._level = simplejson.load(f)

		self._block, _ = helpers.load_image(self._get_image_name("block"))
		self._pellet, _ = helpers.load_image(self._get_image_name("pellet"))
		self._greenMan, _ = helpers.load_image(self._get_image_name("greenMan"))
		self._greenManClosed, _ = helpers.load_image(self._get_image_name("greenManClosed"))
		self._monster_01, _ = helpers.load_image(self._get_image_name("monster_01"))
		self._monster_scared_01, _ = helpers.load_image(self._get_image_name("monster_scared_01"))
		self._monster_evil_01, _ = helpers.load_image(self._get_image_name("monster_evil_01"))
		self._purpleMan, _ = helpers.load_image(self._get_image_name("purpleMan"))
		self._purpleManClosed, _ = helpers.load_image(self._get_image_name("purpleManClosed"))
		self._superPellet, _ = helpers.load_image(self._get_image_name("super_pellet"))
		self._images = {
			self.BLOCK: self._block,
			self.GREENMAN: self._greenMan,
			self.GREENMAN_CLOSED: self._greenManClosed,
			self.PELLET: self._pellet,
			self.MONSTER: self._monster_01,
			self.SCARED_MONSTER: self._monster_scared_01,
			self.EVIL_MONSTER: self._monster_evil_01,
			self.PURPLEMAN: self._purpleMan,
			self.PURPLEMAN_CLOSED: self._purpleManClosed,
			self.SUPER_PELLET: self._superPellet,
		}
		self._biteSound = pygame.mixer.Sound(self._get_sound_name("bite"))
		self._superSound = pygame.mixer.Sound(self._get_sound_name("super"))
		self._killSound = pygame.mixer.Sound(self._get_sound_name("kill"))

	@property
	def sprites(self):
		return self._images

	@property
	def backgroundColor(self):
		return self._level["background"]

	@property
	def biteSound(self):
		return self._biteSound

	@property
	def superSound(self):
		return self._superSound

	@property
	def killSound(self):
		return self._killSound

	def getLayout(self):
		layout =  self._translate_layout(self._level["layout"])
		self._pelletCount = sum(
			sum(
				1
				for c in row
				if c in [self.PELLET, self.SUPER_PELLET]
			)
			for row in layout
		)
		return layout

	def _get_image_name(self, i):
		return os.path.join(self._dataFolder, "images", self._level["image"][i])

	def _get_sound_name(self, i):
		return os.path.join(self._dataFolder, "sounds", self._level["sound"][i])

	def _translate_layout(self, m):
		return [self._translate_row(r) for r in m]

	def _translate_row(self, row):
		return [self._translate_spot(c) for c in row]

	def _translate_spot(self, spot):
		p = self._SYMBOL_TO_VALUE[spot]
		if p == self.PURPLEMAN and config.players == 1:
			p = self.PELLET
		return p
