import os
from pieces import Piece

import pygame
import sys

pygame.init()
path = os.getcwd()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((720, 720))
font = pygame.font.SysFont("Arial", 15, bold=False, italic=False)

pieces_list: [[Piece]] = [[None for i in range(8)] for j in range(8)]


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
                x = int((event.pos[0] / screen.get_width()) * 8)
                y = int((event.pos[1] / screen.get_height()) * 8)
                print(x, y)

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
    width = screen.get_width() / 8
    height = screen.get_height() / 8
    default_size = (int(screen.get_width() / 8), int(screen.get_height() / 8))

    pieces_img = pygame.image.load("assets/pieces.png")

    pieces_width = pieces_img.get_width() / 6
    pieces_height = pieces_img.get_height() / 2

    king_white = pieces_img.subsurface(pygame.rect.Rect(0, 0, pieces_width, pieces_height))
    king_white = pygame.transform.scale(king_white, default_size)
    king_black = pieces_img.subsurface(pygame.rect.Rect(0, pieces_height, pieces_width, pieces_height))
    king_black = pygame.transform.scale(king_black, default_size)

    queen_white = pieces_img.subsurface(pygame.rect.Rect(pieces_width, 0, pieces_width, pieces_height))
    queen_white = pygame.transform.scale(queen_white, default_size)
    queen_black = pieces_img.subsurface(pygame.rect.Rect(pieces_width, pieces_height, pieces_width, pieces_height))
    queen_black = pygame.transform.scale(queen_black, default_size)

    bishop_white = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 2, 0, pieces_width, pieces_height))
    bishop_white = pygame.transform.scale(bishop_white, default_size)
    bishop_black = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 2, pieces_height, pieces_width, pieces_height))
    bishop_black = pygame.transform.scale(bishop_black, default_size)

    knight_white = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 3, 0, pieces_width, pieces_height))
    knight_white = pygame.transform.scale(knight_white, default_size)
    knight_black = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 3, pieces_height, pieces_width, pieces_height))
    knight_black = pygame.transform.scale(knight_black, default_size)

    rook_white = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 4, 0, pieces_width, pieces_height))
    rook_white = pygame.transform.scale(rook_white, default_size)
    rook_black = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 4, pieces_height, pieces_width, pieces_height))
    rook_black = pygame.transform.scale(rook_black, default_size)

    pawn_white = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 5, 0, pieces_width, pieces_height))
    pawn_white = pygame.transform.scale(pawn_white, default_size)
    pawn_black = pieces_img.subsurface(pygame.rect.Rect(pieces_width * 5, pieces_height, pieces_width, pieces_height))
    pawn_black = pygame.transform.scale(pawn_black, default_size)

    pieces_list[1] = [Piece((width * i, height), pawn_black, "black", "pawn") for i in range(8)]
    pieces_list[0][0] = Piece((0, 0), rook_black, "black", "rook")
    pieces_list[0][7] = Piece((width * 7, 0), rook_black, "black", "rook")
    pieces_list[0][1] = Piece((width, 0), knight_black, "black", "knight")
    pieces_list[0][6] = Piece((width * 6, 0), knight_black, "black", "knight")
    pieces_list[0][2] = Piece((width * 2, 0), bishop_black, "black", "bishop")
    pieces_list[0][5] = Piece((width * 5, 0), bishop_black, "black", "bishop")
    pieces_list[0][3] = Piece((width * 3, 0), queen_black, "black", "queen")
    pieces_list[0][4] = Piece((width * 4, 0), king_black, "black", "king")

    pieces_list[6] = [Piece((width * i, height * 6), pawn_white, "white", "pawn") for i in range(8)]
    pieces_list[7][0] = Piece((0, height * 7), rook_white, "white", "rook")
    pieces_list[7][7] = Piece((width * 7, height * 7), rook_white, "white", "rook")
    pieces_list[7][1] = Piece((width, height * 7), knight_white, "white", "knight")
    pieces_list[7][6] = Piece((width * 6, height * 7), knight_white, "white", "knight")
    pieces_list[7][2] = Piece((width * 2, height * 7), bishop_white, "white", "bishop")
    pieces_list[7][5] = Piece((width * 5, height * 7), bishop_white, "white", "bishop")
    pieces_list[7][3] = Piece((width * 3, height * 7), queen_white, "white", "queen")
    pieces_list[7][4] = Piece((width * 4, height * 7), king_white, "white", "king")

    for i in range(8):
        for j in range(8):
            try:
                screen.blit(pieces_list[i][j].img, pieces_list[i][j].pos)
            except:
                pass

    # print_board()


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


def print_board():
    print("=" * 50)
    for row in pieces_list:
        for piece in row:
            try:
                print(f"{piece.name[0]}_{piece.color[0]}", end=" ")
            except:
                print(0, end=" ")
        print("")
    print("=" * 50)


if __name__ == '__main__':
    main()
