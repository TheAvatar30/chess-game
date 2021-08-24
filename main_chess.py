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
    pass


def draw_pieces():
    pass


def move_entity(entity, pressed_keys):
    distance = 10

    if len(pressed_keys) > 0:
        print(pressed_keys)

    # only 'w' pressed
    if len(pressed_keys) == 1 and pressed_keys[0] == "w":
        if entity.pos[1] <= distance:
            entity.pos = (entity.pos[0], 0)
        else:
            entity.pos = (entity.pos[0], entity.pos[1] - distance)

    # only 'a' pressed
    if len(pressed_keys) == 1 and pressed_keys[0] == "a":
        if entity.pos[0] <= distance:
            entity.pos = (0, entity.pos[1])
        else:
            entity.pos = (entity.pos[0] - distance, entity.pos[1])

    # only 's' pressed
    if len(pressed_keys) == 1 and pressed_keys[0] == "s":
        if entity.pos[1] + entity.data.get_height() >= screen.get_height() - distance:
            entity.pos = (entity.pos[0], screen.get_height() - entity.data.get_height())
        else:
            entity.pos = (entity.pos[0], entity.pos[1] + distance)

    # only 'd' pressed
    if len(pressed_keys) == 1 and pressed_keys[0] == "d":
        if entity.pos[0] + entity.data.get_width() >= screen.get_width() - distance:
            entity.pos = (screen.get_width() - entity.data.get_width(), entity.pos[1])
        else:
            entity.pos = (entity.pos[0] + distance, entity.pos[1])

    # 'w' and 'a' pressed
    if len(pressed_keys) == 2 and "w" in pressed_keys and "a" in pressed_keys:
        if entity.pos[1] <= distance:
            entity.pos = (entity.pos[0], 0)
        else:
            entity.pos = (entity.pos[0], entity.pos[1] - distance / np.sqrt(2))

        if entity.pos[0] <= distance:
            entity.pos = (0, entity.pos[1])
        else:
            entity.pos = (entity.pos[0] - distance / np.sqrt(2), entity.pos[1])

    # 'w' and 'd' pressed
    if len(pressed_keys) == 2 and "w" in pressed_keys and "d" in pressed_keys:
        if entity.pos[1] <= distance:
            entity.pos = (entity.pos[0], 0)
        else:
            entity.pos = (entity.pos[0], entity.pos[1] - distance / np.sqrt(2))

        if entity.pos[0] + entity.data.get_width() >= screen.get_width() - distance:
            entity.pos = (screen.get_width() - entity.data.get_width(), entity.pos[1])
        else:
            entity.pos = (entity.pos[0] + distance / np.sqrt(2), entity.pos[1])

    # 's' and 'a' pressed
    if len(pressed_keys) == 2 and "s" in pressed_keys and "a" in pressed_keys:
        if entity.pos[1] + entity.data.get_height() >= screen.get_height() - distance:
            entity.pos = (entity.pos[0], screen.get_height() - entity.data.get_height())
        else:
            entity.pos = (entity.pos[0], entity.pos[1] + distance / np.sqrt(2))

        if entity.pos[0] <= distance:
            entity.pos = (0, entity.pos[1])
        else:
            entity.pos = (entity.pos[0] - distance / np.sqrt(2), entity.pos[1])

    # 's' and 'd' pressed
    if len(pressed_keys) == 2 and "s" in pressed_keys and "d" in pressed_keys:
        if entity.pos[1] + entity.data.get_height() >= screen.get_height() - distance:
            entity.pos = (entity.pos[0], screen.get_height() - entity.data.get_height())
        else:
            entity.pos = (entity.pos[0], entity.pos[1] + distance / np.sqrt(2))

        if entity.pos[0] + entity.data.get_width() >= screen.get_width() - distance:
            entity.pos = (screen.get_width() - entity.data.get_width(), entity.pos[1])
        else:
            entity.pos = (entity.pos[0] + distance / np.sqrt(2), entity.pos[1])


def move_entity_to_mouse(entity):
    distance = 10
    e_x, e_y = entity.pos[0], entity.pos[1]
    m_x, m_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    angle = math.atan2(m_y - e_y, m_x - e_x)
    e_x += distance * np.cos(angle)
    if e_x < distance:
        e_x = 1
    elif e_x + entity.data.get_width() >= screen.get_width():
        e_x = screen.get_width() - entity.data.get_width()

    e_y += distance * np.sin(angle)
    if e_y < distance:
        e_y = 1
    elif e_y + entity.data.get_height() >= screen.get_height():
        e_y = screen.get_height() - entity.data.get_height()

    entity.pos = (e_x, e_y)


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


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    screen.blit(fps_text, (screen.get_width() - 0.5 * variables.FONT_SIZE * len(fps), 0))


if __name__ == '__main__':
    main()
