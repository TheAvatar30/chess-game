import math

import numpy as np
import os
import pygame
import sys

pygame.init()
path = os.getcwd()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((720, 720))
font = pygame.font.SysFont("Arial", 15, bold=False, italic=False)


def main():
    start_game()


def start_game():
    pygame.display.set_caption("Chess")
    while True:
        draw_tiles()
        draw_pieces()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

        pressed_keys = get_pressed_keys()

        dt = clock.tick(60)
        pygame.display.update()


def draw_tiles():
    width = screen.get_width() / 8
    height = screen.get_height() / 8
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (235, 209, 185)
            else:
                color = (162, 110, 91)
            pygame.draw.rect(screen, color, pygame.Rect(i * width, j * height, width, height))


def draw_pieces():
    pass


def get_pressed_keys():
    key_list = []

    if pygame.key.get_pressed()[pygame.K_w] == 1:
        key_list.append("w")
    if pygame.key.get_pressed()[pygame.K_a] == 1:
        key_list.append("a")
    if pygame.key.get_pressed()[pygame.K_s] == 1:
        key_list.append("s")
    if pygame.key.get_pressed()[pygame.K_d] == 1:
        key_list.append("d")
    if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
        key_list.append("space")

    return key_list


if __name__ == '__main__':
    main()
