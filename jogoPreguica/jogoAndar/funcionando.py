import pygame
import sys
from pygame.locals import *

pygame.init()
global tudo
tudo = 0
largura = 854 
altura = 480
velocidadeAndar = 10

FUNDO = pygame.image.load('./img/fundo.jpg')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Andar Andar')


# Defina a classe do boneco
class Boneco(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.spritesFrente = [] #sprites 
        self.spritesFrente.append(pygame.image.load('./img/homem/homem1.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem2.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem3.png'))
        self.spritesFrente.append(pygame.image.load('./img/homem/homem4.png'))

        self.spritesCostas = [] #sprites 
        self.spritesCostas.append(pygame.image.load('./img/homem/homem5.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem6.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem7.png'))
        self.spritesCostas.append(pygame.image.load('./img/homem/homem8.png'))

        self.atual = 0

        self.geral = 0

        self.image = self.spritesFrente[self.atual] # recebe a imagem atual no array
        self.image = pygame.transform.scale(self.image, (64*1.3, 32*3.3))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.vel_y = 0  # Velocidade inicial no eixo Y
        self.gravidade = 1.3  # Ajuste a gravidade conforme necessário
        
        self.andando = False
        self.andandoRe = False
        self.posicao_x = 40

    def re(self):
        self.andandoRe = True

    def andar(self):
        self.andando = True

    def update(self):
        # Atualiza a posição vertical do boneco com base na gravidade
        global tudo
        self.vel_y += self.gravidade
        self.rect.y += self.vel_y

        #Mudar de tela
        if(self.posicao_x >= largura):
            self.posicao_x = -50
            tudo = 1
        elif(self.posicao_x <= -80):
            self.posicao_x = largura
            tudo = 0

        #Andando para frente
        if(self.andando):
            self.andando = False

            self.posicao_x = self.posicao_x  + velocidadeAndar
            self.rect.topleft = self.posicao_x, self.rect.y

            self.atual = self.atual + 0.5 
 
            if self.atual >= len(self.spritesFrente): 
                self.atual = 0


            self.image = self.spritesFrente[int(self.atual)] 

            self.image = pygame.transform.scale(self.image, (64*1.3, 32*3.3))

            # print(self.posicao_x)

        #Andando para Tras
        if(self.andandoRe):
            self.andandoRe = False

            self.posicao_x = self.posicao_x  -velocidadeAndar
            self.rect.topleft = self.posicao_x, self.rect.y

            self.atual = self.atual + 0.5 
 
            if self.atual >= len(self.spritesCostas): 
                self.atual = 0


            self.image = self.spritesCostas[int(self.atual)] 

            self.image = pygame.transform.scale(self.image, (64*1.3, 32*3.3))
        

        # Verifica se o boneco atingiu o chão
        if self.rect.y > 300:
            self.rect.y = 300
            self.vel_y = 0  # Reinicia a velocidade ao atingir o chão


# Criação do boneco
boneco = Boneco(50, 300)
todos_sprites = pygame.sprite.Group()
todos_sprites.add(boneco)

clock = pygame.time.Clock()

while True:
    tela.blit(FUNDO, (0,0))
    print(tudo)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada é a tecla de espaço

            if event.key == pygame.K_SPACE and boneco.rect.y == 300:
                
                boneco.vel_y = -14  # Ajuste a altura do pulo conforme necessário
    if(tudo == 1):
        FUNDO = pygame.image.load('./img/fundo.jpg')
    else:
        FUNDO = pygame.image.load('./img/fundo.jpg')

    # Tecla D e A
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        boneco.andar()
    elif keys[pygame.K_a]:
        boneco.re()

    # Atualizações
    todos_sprites.update()
    todos_sprites.draw(tela)
    pygame.display.flip()

    clock.tick(20)
