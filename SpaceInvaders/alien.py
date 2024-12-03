import pygame
import random as r
from bullets import Bullet

class AlienBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (165,55,253), (5,5),5)
        self.rect = self.image.get_rect(midbottom =(x,y))
    
    def update(self, ship_object):
        pygame.sprite.spritecollide(self, ship_object, True) # true = destroy other object
        self.rect.y += 10
        if self.rect.y == 810:
            self.kill()




class Alien(pygame.sprite.Sprite): # inherits from the sprites group

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._green_alien = pygame.image.load("/Users/danyelleridley/Documents/Learning/pygame/SpaceInvaders/assets/GreenAlien.png")
        self._red_alien = pygame.image.load("/Users/danyelleridley/Documents/Learning/pygame/SpaceInvaders/assets/RedAlien.png")
        self._yellow_alien = pygame.image.load("/Users/danyelleridley/Documents/Learning/pygame/SpaceInvaders/assets/YellowAlien.png")
        # creating randomization of aliens
        self._spawnable_aliens =[self._green_alien, self._red_alien, self._yellow_alien]
        self.image = self._spawnable_aliens[r.randint(0,2)]
        self.rect = self.image.get_rect(center=(20,20))
        self._going_right = True
    

    def shoot_alien_bullet(self):
        can_shoot = r.randint(1,5)
        if can_shoot == 2:
            alien_bullet = AlienBullet(self.rect.x, self.rect.y)
            return alien_bullet
        pass

    def update(self):
        if self._going_right == True:
            self.rect.x += 5
            if self.rect.x == 760:
                self.rect.y += 50
                self._going_right = False
        else:
            self.rect.x -= 5
            if self.rect.x == 10:
                self._going_right = True
                self.rect.y += 50

