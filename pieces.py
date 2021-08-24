import pygame


class Piece:
    def __init__(self, pos: [int, int], img: pygame.Surface, color: str, name: str):
        self.pos = pos
        self.img = img
        self.color = color
        self.name = name
