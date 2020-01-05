import sys 
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf 
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	stats=GameStats(ai_settings)
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#alien=Alien(ai_settings,screen)
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		#gf.update_aliens(ai_settings,ship,aliens)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		pygame.display.flip()
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()



