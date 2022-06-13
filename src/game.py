import os
import sys

import pygame

from dataclasses import dataclass, field

sys.path.append(os.path.abspath("src"))

from window import Window
from snake import Snake
from food import Food
from assets import ASSETS

@dataclass
class Game:
    window: Window = field(
        default_factory = Window
    )
    
    assets: dict[str, pygame.image] = field(
        init = False
    )
    
    snake: Snake = field(
        default_factory = Snake
    )
    
    food: Food = field(
        default_factory = Food
    )
    
    score: int = field(
        default = 0
    )
    
    timer: pygame.time.Clock = field(
        default_factory = pygame.time.Clock
    )
    
    fps: int = field(
        default = 30
    )
    
    lost: bool = field(
        default = False
    )
    
    lost_count: int = field(
        default = 0
    )
    
    def __post_init__(self) -> None:
        pygame.init()
        self.assets = ASSETS
        self.background = pygame.transform.scale(self.assets["background"], (self.window.width, self.window.height))
        
    def run(self) -> None:
        running = True
        
        while running:
            self.timer.tick(self.fps)
            
            self.window.render_pixels(self.background, (0, 0))
            
            keys = pygame.key.get_pressed()
            
            hit_q = self.snake.update(self.window.screen, keys)
            
            if hit_q:
                self.lost = True
                self.lost_count += 1
                self.window.render_text(f"Lost!", (self.window.width / 2, self.window.height / 2), self.window.lost_font, True)
                
            if self.collision_q():
                self.food.RENDER_Q = False
                self.snake.EATEN = True
                self.score += 1
                
            self.food.update(self.window.screen)
        
            self.window.render_text(f"S C O R E: {self.score}", (10, 10), self.window.main_font)
            pygame.display.update()
            
            if self.lost:
                if self.lost_count > self.fps * 5:
                    run = False
                else:
                    continue
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
    def collision_q(self) -> bool:
        return self.food.item.colliderect(self.snake.body[0])
            
            
        
        