#! /usr/bin/env python

import os
import logging
import pygame


_moduleLogger = logging.getLogger(__name__)


def load_image(name, colorkey=None):
	fullname = os.path.join('data', 'images')
	fullname = os.path.join(fullname, name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		_moduleLogger.exception("Cannot load image "+fullname)
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, pygame.locals.RLEACCEL)
	return image, image.get_rect()
