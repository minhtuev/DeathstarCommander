import pygame
from pygame.locals import *
from pygame.key import *
import random
import sys
class painter():
    screen=0
    background=0
    Model = {}
    render=pygame.sprite.Group()
    def __init__(self,screenWidth,screenHeight):
        WindowFlags = pygame.FULLSCREEN #for fullscreen
        ScreenRectangle = Rect(0, 0, screenWidth, screenHeight)       # the screen resolution
        render=pygame.sprite.Group()
        # initialise pygame
        pygame.init()

        # Create a new window
        self.screen = pygame.display.set_mode(ScreenRectangle.size, WindowFlags)

        pygame.display.set_caption('DeathStar Commander')

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        for i in range(0, 500):
            x = random.randint(0, ScreenRectangle.width-1)
            y = random.randint(0, ScreenRectangle.height-1)
            pygame.draw.circle(self.background, (255,255,255), (x,y), 0)
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        pygame.mixer.music.load("imperial_march.mp3")
#        pygame.mixer.music.play(-1,0.0)
        pygame.key.set_repeat(10,10)
        pass

    def Paint(self,Array):
        for p in Array:
            Id = p[1]
            x = p[2]
            y = p[3]
            if p[0] == "planet":
                if p[1] in self.Model:
                    self.render.clear(self.screen, self.background)
                    self.screen.blit(self.Model[p[1]],[x,y])
                    self.render.update()           
                    self.render.draw(self.screen)
                else:
                    self.render.clear(self.screen, self.background)
                    FileName = random.randint(1,13)
                    Id = pygame.image.load(str(FileName)+".bmp").convert()
                    Id.set_colorkey((0,0,0))
                    Id = pygame.transform.scale(Id,(p[4],p[4]))
                    x = x + int(p[4])/2
                    y = y - int(p[4])/2
                    self.screen.blit(Id,[x,y])
                    self.render.update()                     
                    self.render.draw(self.screen)
                    self.render.draw(self.background)
                    self.Model[p[1]] = Id
            elif p[0] == "DeathStar":
                init = 1
                if init == 1:
                    self.render.clear(self.screen, self.background)
                    Player = pygame.image.load("DeathStar.bmp").convert()
                    Player = pygame.transform.scale(Player, (60, 60))
                    Player.set_colorkey((255,255,255))
                    x = x - 30
                    y = y - 30
                    self.screen.blit(Player,[x,y])
                    self.render.update()                     
                    self.render.draw(self.screen)
                    self.render.draw(self.background)
                    init = 0
                else:
                    self.render.clear(self.screen, self.background)
                    Player.pygame.rect.move_ip(x,y)
                    self.render.update()           
                    self.render.draw(self.screen)
            elif p[0] == "Collision":
                if p[1] in self.Model:
                    self.render.clear(self.screen, self.background)
                    self.screen.blit(self.Model[p[1]],[x,y])
                    self.render.update()           
                    self.render.draw(self.screen)
                else:
                    self.render.clear(self.screen, self.background)
                    Id = pygame.image.load("Collision.bmp").convert()
                    Id = pygame.transform.scale(Id,(p[4],p[4]))
                    Id.set_colorkey((255,255,255))
                    x = x - int(p[4])/2
                    y = y - int(p[4])/2
                    self.screen.blit(Id,[x,y])
                    self.render.update()                     
                    self.render.draw(self.screen)
                    self.render.draw(self.background)
                    self.Model[p[1]] = Id
        pygame.display.update()

    def ClearBackground(self):
        self.screen.blit(self.background, (0,0))
        #pygame.display.update()

    def CheckCollision(self,size):
        pygame.sprite.collide_circle
        
        
        
        
