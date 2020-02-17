import math
import time
import random
import numpy as np
import pygame


class snake:
    # Intialize the pygame
    def __init__(self):
        pygame.init()

        # Define tamanhos
        self.width = self.height = 640
        
        # crea la ventana
        self.screen = pygame.display.set_mode((self.width + 200, self.height))

        # fondo png
        self.background = pygame.image.load('cpatt.png')

        # nombre e icono
        pygame.display.set_caption("Snake 3000")
        self.icon = pygame.image.load('snake_tongue.png')
        pygame.display.set_icon(self.icon)

        self.scl = 32 # tamanho de un cuadro

        # cabeza png
        self.cabezaImg = pygame.image.load('snake.png')
        self.cabezaLenguaImg = pygame.image.load('snake_tongue.png')
        
        # cola png
        self.colaImg = pygame.image.load('cola.png')

        # Manzana png

        self.manzImg = pygame.image.load('manz.png')

        # Score
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Pone en cero todos los valores
        self.setup()

        # Game Over
        self.h1_font = pygame.font.Font('freesansbold.ttf', 64)
        self.h2_font = pygame.font.Font('freesansbold.ttf', 32)
        self.clock = pygame.time.Clock()

    def setup(self):

        # cabeza
        self.cabezaX = 160
        self.cabezaY = 320
        self.mov_x = 1
        self.mov_y = 0
        self.new_mov_x = 1
        self.new_mov_y = 0
        self.tiempo_ini = 0 


        # Cola
        self.colaX = []
        self.colaY = []
        self.num_cola = 3

        for i in range(self.num_cola, 0, -1):
            self.colaX.append(self.cabezaX-self.scl*(i+1))
            self.colaY.append(self.cabezaY)

        # score
        self.score_value = 0
        f= open("scores.txt","r")
        self.max_score = int(f.read())
        f.close()

        # manzana
        self.manzX = 416
        self.manzY = self.cabezaY

        self.estado = 'pausado'

    # El juego en si
    def game_on(self):
        # Game Loop
        running = True
        while running:

            self.tiempo_ini = int(round(time.time() * 1000))  # toma el tiempo actual para calculos

            self.clock.tick_busy_loop(7)  # pone la velocidad 
            
            
            for event in pygame.event.get():  # Determinaa que evento sucedio
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:  # Determinaa que tecla se apreto
                    if event.key == pygame.K_LEFT and not self.mov_x == 1:
                        self.new_mov_x = -1
                        self.new_mov_y = 0
                    elif event.key == pygame.K_RIGHT and not self.mov_x == -1:
                        self.new_mov_x = 1
                        self.new_mov_y = 0
                    elif event.key == pygame.K_UP and not self.mov_y == 1:
                        self.new_mov_y = -1
                        self.new_mov_x = 0
                    elif event.key == pygame.K_DOWN and not self.mov_y == -1:
                        self.new_mov_x = 0
                        self.new_mov_y = 1
                    if event.key == pygame.K_SPACE:
                        if self.estado == 'pausado':
                            self.estado = 'jugando'
                        elif self.estado == 'jugando':
                            self.estado = 'pausado'
                        elif self.estado == 'perdio':
                            self.setup()
                            self.estado = 'jugando'
                        elif self.estado == 'gano':
                            self.setup()
                            self.estado = 'jugando'

                    if event.key == pygame.K_f:   #CHEAT# APRETAR LA TECLA 'f' PARA GANAR
                        print("HOLA")
                        self.score_value = self.max_score + 42
                        self.actu_score()
                        self.estado = 'gano'

            if self.estado == 'jugando':  # dependiendo del estado se juega 

                self.screen.fill((0, 0, 0))
                self.screen.blit(self.background, (0, 0))
                self.manzana(self.manzX, self.manzY)

                self.colaX[0] = self.cabezaX  # mueve la cola
                self.colaY[0] = self.cabezaY
                self.cola(self.colaX[0], self.colaY[0])
                
                for i in range(self.num_cola-1, 0, -1):
                        
                    self.colaX[i] = self.colaX[i-1]
                    self.colaY[i] = self.colaY[i-1]
                    self.cola(self.colaX[i], self.colaY[i])

                if self.cabezaX % 32 == 0:  #asegura la direccion del movimiento
                    self.mov_x = self.new_mov_x 
                if self.cabezaY % 32 == 0:
                    self.mov_y = self.new_mov_y
                
                self.cabezaX += self.mov_x*self.scl  # mueve la serpiente
                self.cabezaY += self.mov_y*self.scl

                self.cabeza(self.mov_x, self.mov_y, self.cabezaX, self.cabezaY)
                self.show_score()
                self.show_max_score()
                self.chequeo_colisiones()
                
            elif self.estado == 'pausado':
                self.paused()
            elif self.estado == 'perdio':
                self.game_over()
            elif self.estado == 'gano':
                self.win()
            pygame.display.update()

    def chequeo_colisiones(self):

                #  chequea si comio su cola
                for i in range(self.num_cola):
                    if self.isCollision(self.colaX[i], self.colaY[i], self.cabezaX, self.cabezaY):
                        self.game_over()
                        self.estado = 'perdio'
                
                #  Chequea si come la manzana
                if self.isCollision(self.manzX, self.manzY, self.cabezaX, self.cabezaY):
                    self.num_cola += 1
                    self.colaX.append(1)
                    self.colaY.append(1)
                    self.score_value += round(self.num_cola/(round(time.time() * 1000) - self.tiempo_ini)*100)  # El score depende de que tan largo sea y del tiempo que tardo en conseguir
                    if self.num_cola == 19*19:  # si llego al max gana
                        self.estado = 'gano'
                        self.actu_score()
                    else:  # si no pone otr manzana
                        self.manzX, self.manzY = self.pos_manz()
                        self.manzana(self.manzX, self.manzY)
                
                #  cheackea si no choco contra los bordes
                if self.cabezaX <= 0:
                    self.cabezaX = 0
                    self.game_over()
                    self.estado = 'perdio'
                    
                if self.cabezaY <= 0:
                    self.cabezaY = 0
                    self.game_over()
                    self.estado = 'perdio'
                    
                if self.cabezaX >= self.width - self.scl:
                    self.cabezaX = self.width - self.scl
                    self.game_over()
                    self.estado = 'perdio'
                    
                if self.cabezaY >= self.height - self.scl:
                    self.cabezaY = self.height - self.scl
                    self.game_over()
                    self.estado = 'perdio'

    # texto de ganar
    def win(self):
        over_text = self.h1_font.render("Ganaste!", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2 - over_text.get_width()/2, 100))
        over_text = self.h2_font.render("Tu score fue de: "+ str(self.score_value), True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2- over_text.get_width()/2, 200))
        over_text = self.h2_font.render("Espacio para continuar", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2- over_text.get_width()/2, 300+ over_text.get_height()/2))

# actualiza el max score con el archivo
    def actu_score(self):
        if self.score_value>self.max_score:
            self.max_score = self.score_value
            f = open("scores.txt","w")
            max_sco = str(self.max_score)
            f.write(max_sco)
            f.close()

    # texto de score
    def show_score(self):
        score = self.font.render("Score: ", True, (255, 255, 255))
        self.screen.blit(score, (740 - score.get_width()/2, 0))
        score = self.font.render(str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (740 - score.get_width()/2, score.get_height()))

    #texto del max score
    def show_max_score(self):
        score = self.font.render("Max score: ", True, (255, 255, 255))
        self.screen.blit(score, (740 - score.get_width()/2, self.height/2-score.get_height()))
        score = self.font.render(str(self.max_score), True, (255, 255, 255))
        self.screen.blit(score, (740 - score.get_width()/2, self.height/2+score.get_height()/2))

    # texto de perdiste
    def game_over(self):
        over_text = self.h1_font.render("Perdiste!", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2 - over_text.get_width()/2, 100))
        over_text = self.h2_font.render("Espacio para jugar de nuevo", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2- over_text.get_width()/2, 200))

    # Imprime la cabeza, con lengua si esta cerca de la manzana y gira hacia donde va
    def cabeza(self, rx, ry, x, y):
        distance = math.sqrt(math.pow(self.manzX - x, 2) + (math.pow(self.manzY - y, 2)))
        if distance < self.scl*4:
            snakeImage = self.cabezaLenguaImg
        else:
            snakeImage = self.cabezaImg

        # aca rota con respecto a donde va la serpiente
        if rx == 1:
            self.screen.blit(pygame.transform.rotate(snakeImage, 90), (x, y))
        elif rx == -1:
            self.screen.blit(pygame.transform.rotate(snakeImage, -90), (x, y))
        elif ry == 1:
            self.screen.blit(pygame.transform.rotate(snakeImage, 0), (x, y))
        else:
            self.screen.blit(pygame.transform.rotate(snakeImage, 180), (x, y))

    # imprime la manzana
    def manzana(self, x, y):
        self.screen.blit(self.manzImg, (x, y))

    #imprime una cola
    def cola(self, x, y):
        self.screen.blit(self.colaImg, (x, y))

    # retorna si hay una colision, una colision se da cuando la distancia entre dos puntos es menor a 32 (el tam de un cuadro)
    def isCollision(self, cosa1X, cosa1Y, cosa2X, cosa2Y):
        distance = math.sqrt(math.pow(cosa1X - cosa2X, 2) + (math.pow(cosa1Y - cosa2Y, 2)))
        return distance < 32

    #retorna los lugares disponibles para poner la manzana en el tablero, excluyendo la cabeza y la cola
    def pos_manz(self):
        arr = [[False for x in range(20)] for y in range(20)]  #matriz de tamanho del tablero
        tarr = []  # vector de posiciones disponibles
        for i in range(1, 19):
            for j in range(1, 19):
                if not (i == self.cabezaX and j == self.cabezaY):
                    for k in range(self.num_cola):
                        arr[i][j] = arr[i][j] or self.isCollision(i*self.scl+16, j*self.scl+16, self.colaX[k], self.colaY[k])
                    if not arr[i][j]:
                        tarr.append((i*32,j*32))  # si esta disponible el lugar guarda en el array

        return random.choice(tarr)

    #text de pausa
    def paused(self):
        over_text = self.h1_font.render("Pausado", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2 - over_text.get_width()/2, 100))
        over_text = self.h2_font.render("Espacio para continuar", True, (255, 255, 255))
        self.screen.blit(over_text, (self.width/2- over_text.get_width()/2, 200))

h = snake()

h.game_on()