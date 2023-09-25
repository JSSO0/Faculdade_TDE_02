import pygame
import sys

pygame.init()

largura, altura = 400, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Reflexão de Objeto")

branco = (255, 255, 255)
vermelho = (255, 0, 0)

x_objeto, y_objeto = 100, 100
largura_objeto, altura_objeto = 50, 50

eixo_reflexao = "horizontal"  

velocidade_reflexao = 1

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.fill(branco)

    pygame.draw.rect(janela, vermelho, (x_objeto, y_objeto, largura_objeto, altura_objeto))

    if eixo_reflexao == "horizontal":
        x_objeto += velocidade_reflexao
        if x_objeto >= largura - largura_objeto or x_objeto <= 0:
            velocidade_reflexao *= -1 
    elif eixo_reflexao == "vertical":
        y_objeto += velocidade_reflexao
        if y_objeto >= altura - altura_objeto or y_objeto <= 0:
            velocidade_reflexao *= -1 

    pygame.display.flip()
