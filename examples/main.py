import pygame
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projet Tuteuré - Pygame")

clock = pygame.time.Clock()
running = True

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # fond gris foncé
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
