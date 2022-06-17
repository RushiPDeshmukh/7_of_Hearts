import pygame
import numpy as np



class Card:
    def __init__(self,num,type) -> None:
        self.num = num
        self.type = type
        self.surface = pygame.Surface((60,120))
        self.num_image = pygame.image.load(num+".png")
        self.num_image = pygame.image.load(type+".png")
        


