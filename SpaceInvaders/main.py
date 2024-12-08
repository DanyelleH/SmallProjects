#game usually run as a huge "while" loop. 
import pygame
import sys
from spaceShip import SpaceShip
from bullets import Bullet
from alien import Alien
class Game:
    def __init__(self):
        #creation of the main window
        pygame.init() # init is initialization method
        self._display = pygame.display.set_mode((800,800)) #screen size
        self._clock = pygame.time.Clock()# actively tracks FPS
        self._channels = pygame.mixer.set_num_channels(2)
        self._background_music = pygame.mixer.Sound(file="SpaceInvaders/Sounds/retro-background-music.mp3")
        pygame.display.set_caption("Space Invaders") # allows changing of the test of the window
        pygame.mixer.Channel(0).play(self._background_music)

        #creation of a surface
        self._space_surface = pygame.Surface((900,800))

        #createSpaceShip
        self._space_ship = SpaceShip("/SpaceInvaders/assets/SpaceShip.png", 400,800)
        self._ship_sprite_group = pygame.sprite.GroupSingle()
        self._ship_sprite_group.add(self._space_ship)

        #create sprite groups
        self._all_bullet = pygame.sprite.Group()
        self._all_aliens = pygame.sprite.Group()
        self._all_alien_bullets = pygame.sprite.Group()

        #create timer for user events.
        self._alien_spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self._alien_spawn_event, 1000)

        self._alien_shoot_event = pygame.USEREVENT +1
        pygame.time.set_timer(self._alien_shoot_event,1000)
    def run(self):
        while True:
            #checks for events
            for event in pygame.event.get(): # to see when an event is happening
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN: # listn for event to track inpuy, and code an output.
                    current_ship_location = self._space_ship.get_position()
                    bullet_object = Bullet(current_ship_location[0] + 40, current_ship_location[1])
                    self._all_bullet.add(bullet_object)   

                if event.type == self._alien_spawn_event: # spawns a new alien every 1000 milliseconds.
                    alien_object = Alien()
                    self._all_aliens.add(alien_object)

                if event.type == self._alien_shoot_event:
                    alien_list = self._all_aliens.sprites()
                    for alien in alien_list:
                        alien_bullet_object = alien.shoot_alien_bullet()
                        if alien_bullet_object is not None:
                            self._all_alien_bullets.add(alien_bullet_object)
                        else:
                            pass
                    print(self._all_alien_bullets)
                            

                    
            #handling pressing keys
            keys = pygame.key.get_pressed()
            # ship_x, ship_y = self._space_ship.get_position()

            #Movement Logic
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self._space_ship.move("d")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self._space_ship.move("a")
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self._space_ship.move("w")
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self._space_ship.move("s")


            self._display.blit(self._space_surface, (0,0)) # blit essentially " draws" on the display
            self._space_surface.blit(pygame.image.load("/Users/danyelleridley/Documents/Learning/pygame/SpaceInvaders/assets/OuterSpace.png"),(0,0))# blit draws on the surface itself.
            self._space_surface.blit(self._space_ship.get_surface(), self._space_ship.get_position())
            self._all_bullet.draw(self._space_surface)
            self._all_bullet.update(self._all_aliens) # checks status of every instance in this group. compares positions.
            if self._all_alien_bullets is not None:
                self._all_alien_bullets.draw(self._space_surface)
                self._all_alien_bullets.update(self._ship_sprite_group)

            if pygame.sprite.spritecollide(self._space_ship, self._all_aliens, False):
                pygame.quit()
                sys.exit()


            #create aliens
            self._all_aliens.draw(self._space_surface)
            self._all_aliens.update()

            #updates window
            pygame.display.update()
            self._clock.tick(60) # timer set to 60 fps


my_game=Game()
my_game.run()