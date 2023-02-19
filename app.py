import pygame, sys
from button import Button


class CounterApp:
    ''' Counter app using pygame, creating a GUI '''
    
    def __init__(self) -> None:
        self.count = 0
        self.fps = 60
        self.objects = list()
        self.fps_clock = pygame.time.Clock()
        self.width, self.height = 1366, 768 # screen resolution
        
        
        pygame.init()
        
        # we assign a pygame surface to variable screen
        self.screen = pygame.display.set_mode((self.width, self.height), vsync=1)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.font = pygame.font.SysFont('Arial', 40)
        pygame.display.set_caption("Counter App")
        
        self.bg_color = (100,100,100)
        
    def run_app(self) -> None:
        while True:
            # event handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.main_menu()
            self._update_screen()
            self.fps_clock.tick(self.fps)
            
    def main_menu(self):
        DEFAULT_IMAGE_SIZE = (200,200)
        dec_img = pygame.image.load('counter_pygame/images/left-arrow.png').convert_alpha()
        inc_img = pygame.image.load('counter_pygame/images/right-arrow.png').convert_alpha()
        
        dec_img = pygame.transform.scale(dec_img, (180,180))
        inc_img = pygame.transform.scale(inc_img, (DEFAULT_IMAGE_SIZE))

        dec_button = Button(425, 415, dec_img)
        inc_button = Button(725, 400, inc_img)
        self.screen.fill(self.bg_color)
        dec_button.render(self.screen)
        inc_button.render(self.screen)
        
        # event click -> increment or decrement counter
        if dec_button.event_inc_dec(self.screen):
            self.count -= 1
            print(self.count)
        elif inc_button.event_inc_dec(self.screen):
            self.count += 1
            print(self.count)
            
        self._draw_count()
            
    def _draw_count(self):
        font = pygame.font.SysFont(None, 72)
        img = font.render(str(self.count), True, (0, 0, 0))
        self.screen.blit(img, (650, 300))
        
    def _update_screen(self) -> None:
        pygame.display.flip()
                            
if __name__=="__main__":
    app = CounterApp()
    app.run_app()
        