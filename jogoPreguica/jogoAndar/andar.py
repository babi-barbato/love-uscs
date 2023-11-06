# Bibliotecas
import pygame
import time
from pygame.locals import *
from sys import exit

# Inicia pygame e define cores, tamanho da tela, e nome da mesma
pygame.init()

largura = 620
altura = 370

# PRETO = (200,0,0)
FUNDO = pygame.image.load('./img/fundo.jpg')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Andar Andar')

# Classe do sapo
class Sapo(pygame.sprite.Sprite):
    #self é o para falar que a propriedade e da classe, como atributos em JAVA
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spritesFrente = [] #sprites é o nome do meu array que acomula tds as fts do meu sapo
        self.spritesFrente.append(pygame.image.load('./img/homem/homem1.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem2.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem3.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem4.png'))

        self.spritesCostas = [] #sprites é o nome do meu array que acomula tds as fts do meu sapo
        self.spritesCostas.append(pygame.image.load('./img/homem/homem5.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem6.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem7.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem8.png'))

        self.atual = 0 # imagem atual é 0 q  ue é = a 1°

        self.image = self.spritesFrente[self.atual] # recebe a imagem atual no array

        self.image = pygame.transform.scale(self.image, (64*1, 32*3))


        self.animar = False
        self.andandoFrente = False
        self.andandoCostas = False

        self.posicao_x = 100
        self.posicao_y = 200
        
        # onde o sapo vai ficar na tela
        self.rect = self.image.get_rect()
        self.rect.topleft = self.posicao_x, self.posicao_y

    def atacar(self):
        self.animar = True

    def andarFrente(self):
        self.andandoFrente = True

    def andarCostas(self):
        self.andandoCostas = True

    def update(self):

        if(self.andandoFrente == True):

            #Posição dela
            self.posicao_x = self.posicao_x  + 4
            self.rect.topleft = self.posicao_x, self.posicao_y

            #imagens
            self.atual = self.atual + 0.5 
 
            if self.atual >= len(self.spritesFrente): 

                self.atual = 0 
                self.andandoFrente = False 

            self.image = self.spritesFrente[int(self.atual)] 

            self.image = pygame.transform.scale(self.image, (64*1, 32*3))

        if(self.andandoCostas == True):
            #Posição dela
            self.posicao_x = self.posicao_x  - 4
            self.rect.topleft = self.posicao_x, self.posicao_y

            #imagens
            self.atual = self.atual + 0.5 

            if self.atual >= len(self.spritesCostas): 

                self.atual = 0 
                self.andandoCostas = False

            self.image = self.spritesCostas[int(self.atual)] 

            self.image = pygame.transform.scale(self.image, (64*1, 32*3))



todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)
relogio = pygame.time.Clock()

while True:
    relogio.tick(20) # tempo para atualizar (qnt maior mais rápido)
    tela.blit(FUNDO, (0,0))
    

    # sapo.atacar() # chama o função atacar para ficar ativo
    for event in pygame.event.get(): #Se alguem apertar qualquer coisa
    
        if (event.type == QUIT): # se esse evento for sair ele fecha o programa
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_d]:
            sapo.andarFrente()

        if pygame.key.get_pressed()[K_a]:
            sapo.andarCostas()
    
    todas_as_sprites.draw(tela) # desenha tds as sprites na tela
    todas_as_sprites.update() # chama a função que vai atualizar o sapo (a imagem q aparece)
    pygame.display.flip() # fica no loop

