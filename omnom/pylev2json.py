#!/usr/bin/env python

from __future__ import with_statement
from __future__ import division

import simplejson
import logging

import levelloader
import config


_moduleLogger = logging.getLogger(__name__)


_VALUE_TO_SYMBOL = dict(
	(v, s)
	for (s, v) in levelloader.LevelLoader._SYMBOL_TO_VALUE.iteritems()
)


def pylevel_to_json(moduleName, jsonname):
	config.player = 2 # be sure to get multi-player
	level0XX = __import__(moduleName)
	layout = level0XX.level().getLayout()
	for r in xrange(len(layout)):
		for c in xrange(len(layout[r])):
			layout[r][c] = _VALUE_TO_SYMBOL[layout[r][c]]
		layout[r] = "".join(layout[r])
	level = {
		"layout": layout,
		"image": {
			"block": "blueTileBlock.png",
			"pellet": "pellet.png",
			"greenMan": "charOpenRight.png",
			"monstor_01": "monster.png",
			"monstor_scared_01": "monsterScared.png",
			"monstor_evil_01": "monsterEvil.png",
			"purpleMan": "purpleOpenRight.png",
			"super_pellet": "superPellet.png",
		},
	}
	with open(jsonname, "w") as f:
		simplejson.dump(level, f, indent=4)


if __name__ == "__main__":
	import sys
	pylevel_to_json(sys.argv[1], sys.argv[2])
