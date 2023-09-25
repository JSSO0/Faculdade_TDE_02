import pygame
import sys


pygame.init()

largura, altura = 400, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Translação de Objeto")

branco = (255, 255, 255)
vermelho = (255, 0, 0)

x_objeto, y_objeto = 50, 50

velocidade = 0.5

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x_objeto -= velocidade
    if teclas[pygame.K_RIGHT]:
        x_objeto += velocidade
    if teclas[pygame.K_UP]:
        y_objeto -= velocidade
    if teclas[pygame.K_DOWN]:
        y_objeto += velocidade

    janela.fill(branco)

    pygame.draw.rect(janela, vermelho, (x_objeto, y_objeto, 50, 50))

    pygame.display.flip()
