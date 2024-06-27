import pygame
pygame.init()


tamanho = (800,600) #tupla - Valores Imutáveis
tela = pygame.display.set_mode( tamanho ) # Cria uma tela
clock = pygame.time.Clock()

pygame.display.set_caption("Exemplo") # Titulo da tela

branco = (255, 255, 255) # Variavel com os valores da cor branca
preto = (0, 0, 0) # Variavel com os valores da cor preta
movxbolinha = 400

direita = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco) # preenche a tela com uma cor desejada

    pygame.draw.circle(tela, preto, (movxbolinha, 300), 30) # Paramentros para desenhar um circulo - (x, y), Diametro
    pygame.draw.line (tela, preto, (100, 100), (300, 100), 3) # Paramentros para desenhar uma linha - (x, y), (x, y), Grossura
    pygame.draw.rect (tela, preto, (400, 100, 200, 100), 3) # Paramentros para desenhar um quadrado - (x, y, Largura, Altura), Grossura

    pygame.display.update() # atualiza a tela
    
    if direita == True:
        
        if movxbolinha < 800:
            movxbolinha = movxbolinha + 2
        else:
            direita = False
    else:
        if movxbolinha > 0:
            movxbolinha = movxbolinha - 2
        else:
            direita = True
    clock.tick(60)


pygame.quit()
