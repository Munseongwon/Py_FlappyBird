import pygame.sprite
import assets,configs
from layer import Layer
# GameOver Message Class
class GameOverMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite("gameover")
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH/2, configs.SCREEN_HEIGHT/2))
        super().__init__(*groups)