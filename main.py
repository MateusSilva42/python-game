import pygame
from pygame import Rect

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324

# Inicializar o Módulo do PyGame
pygame.init()
print('setup start')

# Criação de janela do pygame
window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surface = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retângulo da superfície
bg_rectangle: Rect = bg_surface.get_rect(left=0, top=0)
player1_rectangle: Rect = player1_surface.get_rect(left=100, top=100)

# Desenhar na window
window.blit(source=bg_surface, dest=bg_rectangle)
window.blit(source=player1_surface, dest=player1_rectangle)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no jogo
clock = pygame.time.Clock()

# Carregar musica e deixar ela tocando
pygame.mixer_music.load('./asset/stage1.flac')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)

print('setup end')

print('loop start')
while True:
    clock.tick(140)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()

    # Limpar a tela
    window.blit(bg_surface, bg_rectangle)

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rectangle.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rectangle.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rectangle.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rectangle.centerx -= 1

    # Desenhar a nave na nova posição
    window.blit(player1_surface, player1_rectangle)

    # Atualizar a janela
    pygame.display.flip()
#
