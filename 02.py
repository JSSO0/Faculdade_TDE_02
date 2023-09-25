import pygame
import sys
import math

pygame.init()


largura, altura = 400, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rotação de Objeto")

branco = (255, 255, 255)
vermelho = (255, 0, 0)

centro_rotacao = (200, 200)

angulo = 0
velocidade_rotacao = math.radians(2)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.fill(branco)

    x_objeto, y_objeto = 100, 100 
    x_objeto_rot, y_objeto_rot = (
        centro_rotacao[0] + (x_objeto - centro_rotacao[0]) * math.cos(angulo)
        - (y_objeto - centro_rotacao[1]) * math.sin(angulo),
        centro_rotacao[1] + (x_objeto - centro_rotacao[0]) * math.sin(angulo)
        + (y_objeto - centro_rotacao[1]) * math.cos(angulo),
    )

    pygame.draw.rect(janela, vermelho, (x_objeto_rot, y_objeto_rot, 50, 50))

    angulo += velocidade_rotacao

    pygame.display.flip()
