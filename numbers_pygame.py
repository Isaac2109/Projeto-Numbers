import os
from time import sleep
import pygame as pg, random
from pygame.locals import *

# imagem_number = pygame.image.load(os.path.join('imagem_nubers1.jpg'))
clock = pg.time.Clock()
pg.init()
tela = pg.display.set_mode((400,500))
pg.display.set_caption("Numbers")

numero_sorteado = 0
font = pg.font.Font(None, 32)
input_box = pg.Rect(100,150,140,32)
color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
dica_maior = False
dica_menor = False
acertou = False

font_text = pg.font.SysFont('arial', 25)
font_menor = pg.font.SysFont('arial', 20)
running = True

cor_background = 37, 247, 104

def sortear(lista):
    global numero_sorteado
    sorteado = random.choice(lista)
    numero_sorteado = sorteado
    print(numero_sorteado)


def check(numero_certo, palpite):
    if numero_certo > int(palpite):
        return "maior"
    if numero_certo < int(palpite):
        return "menor"
    if numero_certo == int(palpite):
        return "acertou"
    


# tela inicial
tela_inicial = True
text_inicial_1 = font_text.render("Este mini-game consiste em acertar", 1, (0, 50, 150))
text_inicial_2 = font_text.render("dentro do tempo estipulado", 1, (0, 50, 150))
text_inicial_3 = font_text.render("um número que foi sorteado entre 0 e 100", 1, (0, 50, 150))
text_inicial_4 = font_text.render("a cada acerto o tempo diminui", 1, (0, 50, 150))
text_inicial_5 = font_text.render("tente acertar o máximo de números", 1, (0, 50, 150))
text_inicial_6 = font_text.render("que você puder antes que o tempo acabe", 1, (0, 50, 150))
text_inicial_7 = font_text.render("para começar pressione espaço", 1, (10,50,250))

# jogo rodando
playing = False
text_palpite = font_text.render("Digite seu palpite no campo abaixo", 1, (0, 50, 150))
text_dica_menor = font_menor.render("O número sorteado é menor do que seu palpite", 1, (0, 50, 150))
text_dica_maior = font_menor.render("O número sorteado é maior do que seu palpite", 1, (0, 50, 150))
text_acertou = font_text.render("Você acertou o número sorteado", 1, (0, 50, 150))

temporizador = list(range(60))
for sec in temporizador:
    print(len(temporizador))
    sleep(1)
    del temporizador[:-1]
    

# tela restart
tela_restart = False

while running:
    clock.tick(60)
    tela.fill(cor_background)
    # tela.blit(imagem_number, (0,0))
    if tela_inicial:
        tela.blit(text_inicial_1, (40,50))
        tela.blit(text_inicial_2, (80,80))
        tela.blit(text_inicial_3, (12,110))
        tela.blit(text_inicial_4, (70,140))
        tela.blit(text_inicial_5, (45,170))
        tela.blit(text_inicial_6, (15,200))
        tela.blit(text_inicial_7, (60,260))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == K_SPACE:
                    tela_inicial = False
                    playing = True
                    sortear(range(100))
                    
        

    if playing:
        tela.blit(text_palpite, (45,100))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        if check(numero_sorteado, text) == "maior":
                            dica_menor = False
                            dica_maior = True
                        if check(numero_sorteado, text) == "menor":
                            dica_maior = False
                            dica_menor = True
                        if check(numero_sorteado, text) == "acertou":
                            dica_maior = False
                            dica_menor = False
                            acertou = True

                        
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                   
        txt_surface = font.render(text, True, color)

        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        tela.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(tela, color, input_box, 2)

        if dica_maior:
            tela.blit(text_dica_maior, (30,260))
        if dica_menor:
            tela.blit(text_dica_menor, (30,260))
        if acertou:
            tela.blit(text_acertou, (60,260))




    if tela_restart:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    

    
    pg.display.update()





