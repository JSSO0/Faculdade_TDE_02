import pygame
import sys

pygame.init()

largura, altura = 400, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Escala de Objeto")

branco = (255, 255, 255)
vermelho = (255, 0, 0)

ponto_escala = (200, 200)

escala_x, escala_y = 1.0, 1.0
velocidade_escala = 0.01

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.fill(branco)

    objeto = pygame.Surface((50, 50))
    objeto.fill(vermelho)

    objeto = pygame.transform.scale(
        objeto, (int(50 * escala_x), int(50 * escala_y))
    )

    x_objeto, y_objeto = (
        ponto_escala[0] - objeto.get_width() / 2,
        ponto_escala[1] - objeto.get_height() / 2,
    )

    janela.blit(objeto, (x_objeto, y_objeto))

    escala_x += velocidade_escala
    escala_y += velocidade_escala

    pygame.display.flip()
