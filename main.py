import os
import sys

import pygame

sys.path.append(os.path.abspath("src"))

from game import Game

def main() -> None:
    Game().run()

if __name__ == "__main__":
    main()