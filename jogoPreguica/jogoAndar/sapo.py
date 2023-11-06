# Bibliotecas
import pygame
from pygame.locals import *
from sys import exit

# Inicia pygame e define cores, tamanho da tela, e nome da mesma
pygame.init()

largura = 640
altura = 480

PRETO = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Andar Andar')

# Classe do sapo
class Sapo(pygame.sprite.Sprite):
    #self é o para falar que a propriedade e da classe, como atributos em JAVA
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [] #sprites é o nome do meu array que acomula tds as fts do meu sapo
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('./Youtube/sprites/attack_10.png'))

        self.atual = 0 # imagem atual é 0 q  ue é = a 1°

        self.image = self.sprites[self.atual] # recebe a imagem atual no array

        self.image = pygame.transform.scale(self.image, (128*3, 64*3))


        self.animar = False
        self.andandoFrente = False
        self.andandoCostas = False

        self.posicao_x = 100
        self.posicao_y = 100
        
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
        #Se animar for verdadeiro
        if (self.animar == True):

            self.atual = self.atual + 0.5 #Muda sua posição (ele usa numero quebrado para ficar 2 vezes em cada imagem pois arredonda para baixo)

            if self.atual >= len(self.sprites): # se ma posição atual for maior ou igual ao tamnho de sprites

                self.atual = 0 # volta ela para 0
                self.animar = False # animar vira falso

            self.image = self.sprites[int(self.atual)] # imagem

            # print("=====================================")
            # print(self.atual)
            # print(int(self.atual))

            self.image = pygame.transform.scale(self.image, (128*3, 64*3))

        if(self.andandoFrente == True):
            self.posicao_x = self.posicao_x  + 20
            self.rect.topleft = self.posicao_x, self.posicao_y
            self.andandoFrente = False

        if(self.andandoCostas == True):
            self.posicao_x = self.posicao_x - 20
            self.rect.topleft = self.posicao_x, self.posicao_y
            self.andandoCostas = False



todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)
relogio = pygame.time.Clock()

while True:
    relogio.tick(30) # tempo para atualizar (qnt maior mais rápido)
    tela.fill(PRETO)

    for event in pygame.event.get(): #Se alguem apertar qualquer coisa
    
        if (event.type == QUIT): # se esse evento for sair ele fecha o programa
            pygame.quit()
            exit()
        if (event.type == KEYDOWN): # agora se ele apertou qualquer coisa do teclado
            sapo.atacar() # chama o função atacar para ficar ativo

            if event.key == pygame.K_d:
                sapo.andarFrente()
            if event.key == pygame.K_a:
                sapo.andarCostas()
            
            print(event.type)

    
    todas_as_sprites.draw(tela) # desenha tds as sprites na tela
    todas_as_sprites.update() # chama a função que vai atualizar o sapo (a imagem q aparece)
    pygame.display.flip() # fica no loop

