import pygame
import sys
from pygame.locals import *
from Personagens import Boneco
from Nuvens import Nuvem

pygame.init()
LARGURA = 854 
ALTURA = 480
velocidadeAndar = 10

FUNDO = pygame.image.load('./img/fundo.jpg')

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Andar Andar')

# Criação do boneco
boneco = Boneco(50, 300)
nuvem = Nuvem()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(boneco)

for i in range(2):
    nuvem = Nuvem()
    todos_sprites.add(nuvem)

clock = pygame.time.Clock()

totalNuvens = 0

while True:
    tela.blit(FUNDO, (0,0))
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada é a tecla de espaço

            if event.key == pygame.K_SPACE and boneco.rect.y == 300:
                boneco.vel_y = -14  # Ajuste a ALTURA do pulo conforme necessário

    # Tecla D e A
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        boneco.andar()
        nuvem.velocidade = 2
    elif keys[pygame.K_a]:
        boneco.re()
        nuvem.velocidade = 1
    else:
        nuvem.velocidade = 2

    # Atualizações
    todos_sprites.update()
    todos_sprites.draw(tela)
    pygame.display.flip()

    clock.tick(20)
