import pygame
import sys

class Button:
    
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def render(self, surface: pygame.Surface) -> None:
        # check if rect/surface collides w/ another button's space
        if self._check_collide(surface.get_rect()): 
            print("Unable to render buttons. Collision detected.")
            pygame.quit()
            sys.exit()
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
            
            
    def event_inc_dec(self,surface):
        event_action = False
        
        pos = pygame.mouse.get_pos()
        
        # check mouseover & click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False and pygame.MOUSEBUTTONDOWN:
                self.clicked = True
                event_action = True
                pygame.event.wait(1000)
                
        if pygame.mouse.get_pressed()[0] == 0 and pygame.MOUSEBUTTONUP:
            self.clicked = False
            
        # re draw button
        self.render(self.image)
        
        return event_action
        
        
            
            
    def _check_collide(self, other: pygame.Rect) -> bool:
        pass
        # collision = False
        
        # # do not overlap
        # if self.rect.clip(other) == 0:
        #     return collision
        # else:
        #     collision = True
        #     return collision
            