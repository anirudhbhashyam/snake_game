import pygame

from dataclasses import dataclass, field

import numpy as np

from typing import ClassVar

from window import Window

@dataclass
class Food:
    item: pygame.Rect = field(
        init = False
    )
    
    RENDER_Q: ClassVar[bool] = field(
        default = False
    )
    
    def __post_init__(self):
        x, y = self.__generate_food_pos()
        self.item = pygame.Rect(x, y, 20, 20)
    
    def draw(self, surface: pygame.Surface): 
        self.RENDER_Q = True if not self.RENDER_Q else self.RENDER_Q
        pygame.draw.rect(surface, (255, 0, 0), self.item)
       
    def update(self, surface: pygame.Surface):
        if not self.RENDER_Q:
            self.item.x, self.item.y = self.__generate_food_pos()
        self.draw(surface)
        
    @staticmethod    
    def __generate_food_pos() -> tuple[int, int]:
        return (
            np.random.default_rng().integers(0, Window.width - 20),
            np.random.default_rng().integers(0, Window.height - 20)
        )