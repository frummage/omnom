#! /usr/bin/env python

import logging
import pygame
import pygame.locals


_moduleLogger = logging.getLogger(__name__)


def load_image(name, colorkey=None):
	try:
		image = pygame.image.load(name)
	except pygame.error, message:
		_moduleLogger.exception("Cannot load image "+name)
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, pygame.locals.RLEACCEL)
	return image, image.get_rect()
