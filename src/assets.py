import os

import pygame

def load(dir: str) -> dict[str, pygame.image]:
    images = {}
    for filename in os.listdir(os.path.abspath(dir)):
        name = filename.split(".")[0]
        img = pygame.image.load(os.path.join(dir, filename))
        images[name] = img
    return images

ASSETS = load("res")