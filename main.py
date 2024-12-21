
import pygame
import sys
import random
import math

from NPC import *

# Inicializa Pygame
pygame.init()

# Configura la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RPG con NPC inmóvil")

# Cargar imágenes
background_image = pygame.image.load('assets/background.png').convert()
player_image = pygame.image.load('assets/player.png').convert_alpha()
npc1_image = pygame.image.load('assets/npc.png').convert_alpha()
npc2_image = pygame.image.load('assets/npc2.png').convert_alpha()
npc3_image = pygame.image.load('assets/npc3.png').convert_alpha()

# Configurar el jugador
player_rect = player_image.get_rect()
player_rect.topleft = (screen_width // 2, screen_height // 2)
player_speed = 5

# Configurar el NPC 1 (Inmóvil)
npc1_rect = npc1_image.get_rect()
npc1_rect.topleft = (200, 200)

# Configurar el NPC 2 (Inmóvil)
npc2_rect = npc2_image.get_rect()
npc2_rect.topleft = (400, 400) # Dfine la ubicación del NPC

# Instancia NPC 3 (Inmovil)
npc3 = NPC(npc3_image, 500, 100)



# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Movimiento del player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
    if keys[pygame.K_UP]:
            player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
            player_rect.y += player_speed

    # Asegurarse de que el jugador se mantenga dentro de la ventana
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_width:
        player_rect.right = screen_width
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > screen_height:
        player_rect.bottom = screen_height

    # Dibujar todo
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, player_rect.topleft)
    screen.blit(npc1_image, npc1_rect.topleft)
    screen.blit(npc2_image, npc2_rect.topleft)
    screen.blit(npc3.npc_image, npc3.ubicacion)



    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
sys.exit()
