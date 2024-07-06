import components
import pygame

win_height = 680
win_width = 1250
window = pygame.display.set_mode((win_width, win_height))

ground = components.Ground(win_width)
pipes = []