from dataclasses import dataclass, field

from typing import ClassVar

import pygame 

from window import Window

@dataclass
class Snake:
    body: list = field(
        init = False, 
        default_factory = list
    )
    
    segment_width: int = field(
        default = 10
    )
    
    segment_height: int = field(
        default = 10
    )
    
    body_length: int = field(
        default = 6
    )
    
    width: float = field(
        default = 10.0
    )

    height: float = field(
        init = False
    )
    
    velocity: float = field(
        default = 5
    )
    
    EATEN: ClassVar[bool] = field(
        default = False
    )
    
    direction: str = field(
        default = "up"
    )

    def __post_init__(self): 
        x, y = 100, 100 
        self.body = [pygame.Rect(x, y + 4 * self.segment_height, self.segment_width, self.segment_height) 
                     for i in range(10, (self.body_length + 1) * self.segment_height, self.segment_height)]
        
        self.height = self.segment_height * self.body_length
        
    def update(self, surface:pygame.Surface, keys: dict) -> bool:
        if self.EATEN:
            self.body_length += 1
            self.body.append(pygame.Rect(self.body[-1].x, self.body[-1].y + 4 * self.segment_height, self.segment_width, self.segment_height))
            self.EATEN = False
        self.move(keys)
        self.draw(surface)
        return self.__hit_q()
        
    def draw(self, surface: pygame.Surface):
        for i, rect in enumerate(self.body):
            pygame.draw.rect(surface, (255, 255, 255), rect)
        pygame.draw.rect(surface, (0, 255, 0), self.body[0])
            
    def move(self, keys: list) -> None:
        if keys[pygame.K_UP]:
            self.direction = "up"
                
        if keys[pygame.K_DOWN]: 
            self.direction = "down"               
                
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
        
        if self.direction == "up" and self.body[0].y > 0:
            self.body[0].move_ip(0, -self.velocity)
            
        if self.direction == "down" and self.body[0].y + self.segment_height < Window.height:
            self.body[0].move_ip(0, self.velocity)
            
        if self.direction == "left" and self.body[0].x > 0:
            self.body[0].move_ip(-self.velocity, 0)
            
        if self.direction == "right" and self.body[0].x + self.segment_width < Window.width:
            self.body[0].move_ip(self.velocity, 0)
            
        for i in range(self.body_length - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
            
    def __hit_q(self) -> bool:
        r = False
        
        if ((self.body[0].y <= 0) 
            or (self.body[0].y + self.segment_height >= Window.height)
            or (self.body[0].x <= 0)
            or (self.body[0].x + self.segment_width >= Window.width)
        ):
            r = True
            
        # TODO: implement collision with self.
            
        # for rect in self.body[1 :]:
        #     if (a := self.body[0].colliderect(rect)) != -1:
        #         print(a)
        #         r = True
        
        return r