import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("recursos/iconePidao.png")
personagem = pygame.image.load("recursos/homemPidao.png")
fundo = pygame.image.load("recursos/florestaPidona.png")
fundoStart = pygame.image.load("recursos/comecoPidao2.png")
fundoDead = pygame.image.load("recursos/final2.png")

lua = pygame.image.load("recursos/lua.png")
bala = pygame.image.load("recursos/balaAntiPidao.png")
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("A Jornada Pidona")
pygame.display.set_icon(icone)
somBala = pygame.mixer.Sound("recursos/bala.mp3")
finalSound = pygame.mixer.Sound("recursos/somFinal.mp3")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("recursos/somFundo.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )


def jogar(nome):
    pygame.mixer.Sound.play(somBala)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 300
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXLua = 400
    posicaoYLua = -240
    velocidadeLua = 1
    posicaoXBala = 300
    posicaoYBala = -140
    velocidadeBala = 1
    pontos = 0
    larguraPersona = 224
    alturaPersona = 250
    larguaLua  = 100
    alturaLua  = 100
    larguaBala  = 19
    alturaBala  = 100
    dificuldade  = 20

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0

                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >550:
            posicaoXPersona = 540
            
        if posicaoYPersona < 0 :
            posicaoYPersona = 10
        elif posicaoYPersona > 473:
            posicaoYPersona = 463
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( personagem, (posicaoXPersona, posicaoYPersona) )
        
        posicaoYLua = posicaoYLua + velocidadeLua
        if posicaoYLua > 600:
            posicaoYLua = -240
            pontos = pontos + 1
            velocidadeLua = velocidadeLua + 1
            posicaoXLua = random.randint(0,800)
            pygame.mixer.Sound.play(somBala)

        posicaoYBala = posicaoYBala + velocidadeBala
        if posicaoYBala > 600:
            posicaoYBala = -240
            pontos = pontos + 1
            velocidadeBala = velocidadeBala + 1
            posicaoXBala = random.randint(0,800)
            pygame.mixer.Sound.play(somBala)
            
            
        tela.blit( lua, (posicaoXLua, posicaoYLua) )
        tela.blit( bala, (posicaoXBala, posicaoYBala) )

        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))

        pixelsLuaX = list(range(posicaoXLua, posicaoXLua + larguaLua))
        pixelsLuaY = list(range(posicaoYLua, posicaoYLua + alturaLua))
        
        pixelsBalaX = list(range(posicaoXBala, posicaoXBala + larguaBala))
        pixelsBalaY = list(range(posicaoYBala, posicaoYBala + alturaBala))
        
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsLuaY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsLuaX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        if len( list( set(pixelsBalaY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsBalaX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
    
        
        pygame.display.update()
        relogio.tick(60)



def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(finalSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Iron Man","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()