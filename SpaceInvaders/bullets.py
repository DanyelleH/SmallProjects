import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,0,0,255), (5,5), 5)
        self.rect = self.image.get_rect(midbottom=(x,y))
        self._shoot_sound = pygame.mixer.music.load("/Users/danyelleridley/Documents/Learning/pygame/SpaceInvaders/Sounds/shoot1.mp3")
        pygame.mixer.music.play()

    def update(self, alien_group): # takes in two sprite groups
        self.rect.y -= 20
        pygame.sprite.spritecollide(self, alien_group, True) # it deletes the OTHER sprite, not itself.
        if self.rect.y == -50:
            self.kill() # kill method kills that specifit sprite; preventing overloading " imaginary" sprites that cannot be seen.
            # use method to see if sprites have collided.

