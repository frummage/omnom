#!/usr/bin/env python

import os, sys
import pygame
import level001
import level002
import level003
import level004
import level005
import level006
import level007
import level008
import level009
import level010
import level011
import level012
import level013
import level014
import level015
import continueScrn
import config
import basicSprite
from PyQt4 import QtGui, QtCore
import omnomgui
import greenManSprite
import purpleManSprite
import basicMonster


global levelselect
# Warn if soundrr or fonts are disabled
if not pygame.font:
	print 'Warning, fonts disabled'
if not pygame.mixer:
	print 'Warning, sound disabled'


BLOCK_SIZE = 32
fps = 30
clock = pygame.time.Clock()
levelselect = 0


class nomMain(object):

	def __init__(self , width=800, height=480):
		pygame.mixer.pre_init(44100, -16, 1, 256)
		pygame.init()
		pygame.mouse.set_visible(False)
		pygame.mixer.init()
		#global gameMusic
		#global gameSound
		#global player_speed
		#global enemy_speed
		#self.greenScore = 0
		#self.purpleScore = 0
		#if config.gameMusic == 1:
		#	pygame.mixer.music.load('data/sounds/music1.wav')
		#	pygame.mixer.music.play(-1, 0)
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.locals.FULLSCREEN)

	def MainLoop(self):
		global levelselect
		self.dead = 0
		if config.deathCount == 0:
			config.currentLvl = levelselect
			levelselect = 100
			config.deathCount = 3
			self.dead = 1
			self.ShowScores()
			nomMain().MainLoop()
		self.LoadSprites();
		#pygame.key.set_repeat(500, 30)
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		if config.paper == 1:
			self.background.fill((180, 180, 180))
			self.screen.fill((180, 180, 180))
		else:
			self.background.fill((0, 0, 0))
		self.block_sprites.draw(self.screen)
		self.block_sprites.draw(self.background)
		pygame.display.flip()
		#if config.gameMusic == 1:
		#	if levelselect == 7:
		#		pygame.mixer.music.stop()
		#		pygame.mixer.music.load('data/sounds/mario.wav')
		#		pygame.mixer.music.play(-1, 0)
		if  config.mariomode == 1:
			biteSound = pygame.mixer.Sound('data/sounds/coin.wav')
			superSound = pygame.mixer.Sound('data/sounds/mushroom.wav')
			killSound = pygame.mixer.Sound('data/sounds/kick.wav')
		else:
			biteSound = pygame.mixer.Sound('data/sounds/bite.wav')
			superSound = pygame.mixer.Sound('data/sounds/super.wav')
			killSound = pygame.mixer.Sound('data/sounds/kill.wav')
		while 1:
			if levelselect == 100:
				if self.greenMan.pellets == 1:
					pygame.quit()
					loadGui = sys.executable
					os.execl(loadGui, loadGui, * sys.argv)
				elif self.greenMan.supers == 1:
					levelselect = config.currentLvl
					config.greenScore = 0
					config.purpleScore = 0
					config.greenHits = 0
					config.purpleHits = 0
					config.greenScore = 0
					config.purpleScore = 0
					config.deathCount = 3
					pygame.quit()
					nomMain().MainLoop()
			tick_time = clock.tick(fps)
			#pygame.display.set_caption("Omnom. FPS: %.2f" % (clock.get_fps()))
			#2 player here
			if config.players == 2:
				while self.greenMan.pellets+self.purpleMan.pellets == self.total:
					config.greenScore = config.greenScore+self.greenMan.pellets
					config.purpleScore = config.purpleScore+self.purpleMan.pellets
					#config.greenHits = config.greenHits+self.greenMan.hits
					#config.purpleHits = config.purpleHits+self.purpleMan.hits
					levelselect = levelselect+1
					if levelselect == 16:
						#levelselect = 1
						#speedBoost = 2
						#config.enemy_speed = config.player_speed
						self.ShowScores()
						loadGui = sys.executable
						os.execl(loadGui, loadGui, * sys.argv)
					else:
						#pygame.quit()
						self.ShowScores()
						nomMain().MainLoop()
			else:
				#while self.greenMan.pellets == self.level1.pelletcount:
				while self.greenMan.pellets == self.total:
					config.greenScore = config.greenScore+self.greenMan.pellets
					levelselect = levelselect+1
					if levelselect == 16:
						#pygame.quit()
						#levelselect = 1
						#speedBoost = 2
						#config.enemy_speed = config.player_speed
						self.ShowScores()
						#nomMain().MainLoop()
						loadGui = sys.executable
						os.execl(loadGui, loadGui, * sys.argv)
					else:
						#pygame.quit()
						self.ShowScores()
						nomMain().MainLoop()
			self.greenMan_sprites.clear(self.screen, self.background)
			if config.players == 2:
				self.purpleMan_sprites.clear(self.screen, self.background)
			self.monster_sprites.clear(self.screen, self.background)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.locals.KEYDOWN:
					if ((event.key == pygame.locals.K_RIGHT)
					or (event.key == pygame.locals.K_LEFT)
					or (event.key == pygame.locals.K_UP)
					or (event.key == pygame.locals.K_DOWN)):
						self.greenMan.MoveKeyDown(event.key)
					if ((event.key == pygame.locals.K_x)
					or (event.key == pygame.locals.K_a)
					or (event.key == pygame.locals.K_s)
					or (event.key == pygame.locals.K_z)):
						if config.players == 2:
							self.purpleMan.MoveKeyDown(event.key)
					if event.key == pygame.locals.K_p:
						pygame.image.save(self.screen, '/home/user/MyDocs/omnom/screenshot.png')
					if event.key == pygame.locals.K_BACKSPACE:
						pygame.quit()
						loadGui = sys.executable
						os.execl(loadGui, loadGui, * sys.argv)
					if event.key == pygame.locals.K_SPACE:
						pygame.quit()
						nomMain().MainLoop()
				elif event.type == pygame.locals.KEYUP:
					if ((event.key == pygame.locals.K_RIGHT)
					or (event.key == pygame.locals.K_LEFT)
					or (event.key == pygame.locals.K_UP)
					or (event.key == pygame.locals.K_DOWN)):
						self.greenMan.MoveKeyUp(event.key)
					if ((event.key == pygame.locals.K_x)
					or (event.key == pygame.locals.K_a)
					or (event.key == pygame.locals.K_s)
					or (event.key == pygame.locals.K_z)):
						if config.players == 2:
							self.purpleMan.MoveKeyUp(event.key)
				elif event.type == pygame.locals.SUPER_STATE_OVER:
					self.greenMan.superState = False
					if config.players == 2:
						self.purpleMan.superState = False
					pygame.time.set_timer(pygame.locals.SUPER_STATE_OVER, 0)
					for monster in self.monster_sprites.sprites():
						monster.SetScared(False)
				elif event.type == pygame.locals.SUPER_STATE_START:
					for monster in self.monster_sprites.sprites():
						monster.SetScared(True)
				elif event.type == pygame.locals.PLAYER_EATEN:
					if config.players == 2:
						if ((self.greenMan.lives < 1)
						and (self.purpleMan.lives < 1)):
							self.greenMan.lives = config.lives
							self.purpleMan.lives = config.lives
							config.deathCount = config.deathCount-1
							pygame.quit()
							nomMain().MainLoop()
					else:
						if self.greenMan.lives < 1:
							self.greenMan.lives = config.lives
							config.deathCount = config.deathCount-1
							pygame.quit()
							nomMain().MainLoop()
				#elif event.type == BITE:
				#	biteSound.play(loops=0, maxtime=0, fade_ms=0)
				#elif event.type == KILL:
				#	killSound.play(loops=0, maxtime=0, fade_ms=0)
				#elif event.type == SUPER:
				#	superSound.play(loops=0, maxtime=0, fade_ms=0)
			self.greenMan_sprites.update(self.block_sprites, self.pellet_sprites, self.super_pellet_sprites, self.monster_sprites)
			if config.players == 2:
				self.purpleMan_sprites.update(self.block_sprites, self.pellet_sprites, self.super_pellet_sprites, self.monster_sprites)
			self.monster_sprites.update(self.block_sprites)
			#lstCols = pygame.sprite.spritecollide(self.greenMan, self.pellet_sprites, True)
			#self.greenMan.pellets = self.greenMan.pellets + len(lstCols)
			textpos = 0
			self.screen.blit(self.background, (0, 0))
			if pygame.font:
				font = pygame.font.Font(None, 36)
				if config.players == 2:
					if levelselect == 100:
						text = font.render("Continue?", 1, (255, 255, 255))
					else:
						text = font.render("Green %s		Lives %s		  Level %s		   Purple %s " % (self.greenMan.pellets, config.deathCount, levelselect, self.purpleMan.pellets), 1, (255, 255, 255))
				else:
					if levelselect == 100:
						text = font.render("Continue?", 1, (255, 255, 255))
					else:
						text = font.render("Pellets %s	  Lives %s	   Level %s" % (self.greenMan.pellets, config.deathCount, levelselect), 1, (255, 255, 255))
				textpos = text.get_rect(centerx=self.background.get_width()/2)
				self.screen.blit(text, textpos)
				#pnumber = str(self.greenMan.pellets)
				#tnumber = str(self.level1.pelletcount)
				#text2 = font.render('pnumber tnumber', 1, (255, 0, 0))
				#self.screen.blit(text2, text2.get_rect(centery=self.background.get_height()/2))
			reclist = [textpos]
			reclist += self.pellet_sprites.draw(self.screen)
			reclist += self.super_pellet_sprites.draw(self.screen)
			reclist += self.greenMan_sprites.draw(self.screen)
			if config.players == 2:
				reclist += self.purpleMan_sprites.draw(self.screen)
			reclist += self.monster_sprites.draw(self.screen)
			pygame.display.update(reclist)
			#self.greenMan_sprites.draw(self.screen)
			#self.pellet_sprites.draw(self.screen)
			#pygame.display.flip()

	def ShowScores(self):
		#pygame.init()
		#pygame.mouse.set_visible(False)
		screen = pygame.display.set_mode((800, 480), pygame.locals.FULLSCREEN)
		background = pygame.Surface(screen.get_size())
		if config.players == 2:
			background = pygame.image.load(os.path.join('data/images', '2pbg.png'))
		else:
			background = pygame.image.load(os.path.join('data/images', '1pbg.png'))
		font = pygame.font.Font(None, 36)
		if config.players == 2:
			text = font.render("Green								Purple", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery-100
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("Pellets", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery-40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("Hits", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("Score", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery+40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		if config.players == 2:
			text = font.render("%s" % (config.greenScore), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx-150
			textpos.centery = background.get_rect().centery-40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("%s" % (config.purpleScore), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx+150
			textpos.centery = background.get_rect().centery-40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		else:
			text = font.render("Pellets: %s" % (config.greenScore), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery-40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		pygame.time.wait(1000)
		config.greenHitsTotal = config.greenHitsTotal+config.greenHits
		config.purpleHitsTotal = config.purpleHitsTotal+config.purpleHits
		if config.players == 2:
			text = font.render("%s" % (config.greenHitsTotal), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx-150
			textpos.centery = background.get_rect().centery
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("%s" % (config.purpleHitsTotal), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx+150
			textpos.centery = background.get_rect().centery
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		else:
			text = font.render("Hits: %s" % (config.greenHitsTotal), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		pygame.time.wait(1000)
		greenDeduction = config.greenHitsTotal*10
		purpleDeduction = config.purpleHitsTotal*10
		config.greenPoints = (config.greenScore+greenDeduction)*10
		config.purplePoints = (config.purpleScore+purpleDeduction)*10
		if config.players == 2:
			text = font.render("%s" % (config.greenPoints), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx-150
			textpos.centery = background.get_rect().centery+40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			text = font.render("%s" % (config.purplePoints), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx+150
			textpos.centery = background.get_rect().centery+40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()

		else:
			text = font.render("Score: %s" % (config.greenPoints), 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery+40
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
		if self.dead == 1:
			pygame.time.wait(5000)
			text = font.render("G A M E   O V E R", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery+80
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			pygame.time.wait(5000)
		if levelselect == 16:
			pygame.time.wait(5000)
			text = font.render("CONGRATULATIONS!", 1, (255, 255, 255))
			textpos = text.get_rect()
			textpos.centerx = background.get_rect().centerx
			textpos.centery = background.get_rect().centery+80
			background.blit(text, textpos)
			screen.blit(background, (0, 0))
			pygame.display.flip()
			pygame.time.wait(5000)
		pygame.time.wait(5000)
		self.dead = 0
		pygame.quit()

	def LoadSprites(self):
		global levelselect
		self.total = 0
		x_offset = (BLOCK_SIZE/2)
		y_offset = (BLOCK_SIZE/2)
		if levelselect == 1:
			self.level1 = level001.level()
		elif levelselect == 2:
			self.level1 = level002.level()
		elif levelselect == 3:
			self.level1 = level003.level()
		elif levelselect == 4:
			self.level1 = level004.level()
		elif levelselect == 5:
			self.level1 = level005.level()
		elif levelselect == 6:
			self.level1 = level006.level()
		elif levelselect == 7:
			self.level1 = level007.level()
		elif levelselect == 8:
			self.level1 = level008.level()
		elif levelselect == 9:
			self.level1 = level009.level()
		elif levelselect == 10:
			self.level1 = level010.level()
		elif levelselect == 11:
			self.level1 = level011.level()
		elif levelselect == 12:
			self.level1 = level012.level()
		elif levelselect == 13:
			self.level1 = level013.level()
		elif levelselect == 14:
			self.level1 = level014.level()
		elif levelselect == 15:
			self.level1 = level015.level()
		elif levelselect == 100:
			self.level1 = continueScrn.level()
		#level1 = level001.level()
		layout = self.level1.getLayout()
		img_list = self.level1.getSprites()
		self.pellet_sprites = pygame.sprite.RenderUpdates()
		self.super_pellet_sprites = pygame.sprite.RenderUpdates()
		self.block_sprites = pygame.sprite.RenderUpdates()
		self.monster_sprites = pygame.sprite.RenderUpdates()
		for y in xrange(len(layout)):
			for x in xrange(len(layout[y])):
				centerPoint = [(x*BLOCK_SIZE)+x_offset, (y*BLOCK_SIZE+y_offset)]
				if layout[y][x]==self.level1.BLOCK:
					block = basicSprite.Sprite(centerPoint, img_list[self.level1.BLOCK])
					self.block_sprites.add(block)
				elif layout[y][x]==self.level1.GREENMAN:
					# hmmm...
					self.greenMan = greenManSprite.greenMan(centerPoint, img_list[self.level1.GREENMAN]) # , img_list[level1.GREENMANLEFT] , img_list[level1.GREENMANRIGHT])
				elif layout[y][x]==self.level1.PELLET:
					pellet = basicSprite.Sprite(centerPoint, img_list[self.level1.PELLET])
					self.pellet_sprites.add(pellet)
					self.total = self.total+1
					#pygame.mixer.Sound('data/sounds/bite.wav')
				elif layout[y][x]==self.level1.MONSTER:
					monster = basicMonster.Monster(centerPoint, img_list[self.level1.MONSTER], img_list[self.level1.SCARED_MONSTER], img_list[self.level1.EVIL_MONSTER])
					self.monster_sprites.add(monster)
					#pellet = basicSprite.Sprite(centerPoint, img_list[level1.PELLET])
					#self.pellet_sprites.add(pellet)
				elif layout[y][x]==self.level1.SUPER_PELLET:
					super_pellet = basicSprite.Sprite(centerPoint, img_list[self.level1.SUPER_PELLET])
					self.super_pellet_sprites.add(super_pellet)
				if config.players == 2:
					if layout[y][x]==self.level1.PURPLEMAN:
						# hmmm...
						self.purpleMan = purpleManSprite.purpleMan(centerPoint, img_list[self.level1.PURPLEMAN])
		self.greenMan_sprites = pygame.sprite.RenderUpdates(self.greenMan)
		if config.players == 2:
			self.purpleMan_sprites = pygame.sprite.RenderUpdates(self.purpleMan)


class MyForm(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = omnomgui.Ui_GUI()
		self.ui.setupUi(self)
		#global gameMusic
		#global gameSound
		#global player_speed
		#global enemy_speed
		#gameMusic = 1
		#gameSound = 1
		#player_speed = 8
		#enemy_speed = 3
		self.setWindowTitle("OmNomNom")
		lvl1 = QtGui.QPixmap("/home/opt/python/omnom/data/images/lvl1.png")
		lvl2 = QtGui.QPixmap("/home/opt/python/omnom/data/images/lvl2.png")
		lvl3 = QtGui.QPixmap("/home/opt/python/omnom/data/images/lvl3.png")
		lvl4 = QtGui.QPixmap("/home/opt/python/omnom/data/images/lvl4.png")
		self.ui.lvl1Pic.setPixmap(lvl1)
		self.ui.lvl2Pic.setPixmap(lvl2)
		self.ui.lvl3Pic.setPixmap(lvl3)
		self.ui.lvl4Pic.setPixmap(lvl4)

		QtCore.QObject.connect(self.ui.lvl1Button, QtCore.SIGNAL('clicked()'), self.doLvl1)
		QtCore.QObject.connect(self.ui.lvl2Button, QtCore.SIGNAL('clicked()'), self.doLvl2)
		QtCore.QObject.connect(self.ui.lvl3Button, QtCore.SIGNAL('clicked()'), self.doLvl3)
		QtCore.QObject.connect(self.ui.lvl4Button, QtCore.SIGNAL('clicked()'), self.doLvl4)
		QtCore.QObject.connect(self.ui.configButton, QtCore.SIGNAL('clicked()'), self.doConfig)

	def doLvl1(self):
		global levelselect
		levelselect = 1
		nomMain().MainLoop()

	def doLvl2(self):
		global levelselect
		levelselect = 6
		nomMain().MainLoop()

	def doLvl3(self):
		global levelselect
		levelselect = 10
		nomMain().MainLoop()

	def doLvl4(self):
		global levelselect
		levelselect = 14
		nomMain().MainLoop()

	def doConfig(self):
		confwindow = setConfig(self)
		confwindow.show()


class setConfig(QtGui.QMainWindow):

	def __init__(self, *args):
		QtGui.QMainWindow.__init__(self, args)
		self.ui = omnomgui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("Config")

		QtCore.QObject.connect(self.ui.applyButton, QtCore.SIGNAL('clicked()'), self.doApply)

	def doApply(self):
		#global gameMusic
		#global gameSound
		#global player_speed
		#global enemy_speed
		config.gameMusic = 0
		config.gameSound = 0
		config.players = 1
		config.mariomode = 1
		if self.ui.musicBox.isChecked() == True:
			config.gameMusic = 1
		if self.ui.soundBox.isChecked() == True:
			config.gameSound = 1
		if self.ui.multiBox.isChecked() == True:
			config.players = 2
		config.player_speed = self.ui.playerSpeed.value()
		config.enemy_speed = self.ui.enemySpeed.value()
		config.lives = self.ui.playerLives.value()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
