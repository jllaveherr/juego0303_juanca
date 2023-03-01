import pygame
from ladrillo import Brick

# Setup del juego
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juan Carlos")


# Musica
musica_fondo = pygame.mixer.Sound("deephouse.mp3")
pitidoarbi = pygame.mixer.Sound("pitidoarbi.mp3")
rebote = pygame.mixer.Sound("rebote.mp3")
pygame.mixer.Sound.play(musica_fondo)

# Fondo de pantalla
fondo = pygame.image.load("messi.png")
fondo = pygame.transform.scale(fondo, (800, 600))


# Bases de la pelota
ball = pygame.image.load("pelota.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed = [2, 5]
ballrect.move_ip(400, 400)

# Bases de la barra
barra = pygame.image.load("CR7_siiii.png")
barrarect = barra.get_rect()
barrarect.move_ip(450,580)
fuente = pygame.font.Font(None, 40)
barraSpeed = 3

# Base fin de juego
texto = pygame.image.load("gameover.png")
texto_rect = texto.get_rect()
texto_x = ventana.get_width() / 2 - texto_rect.width / 2
texto_y = ventana.get_height() / 2 - texto_rect.height / 2

#añadir ladrillos

lista_ladrillos = []
for posx in range(20):
    for posy in range(3):
        lista_ladrillos.append(Brick(45*posx, 45*posy, "barsa.png"))

# Funciones del juego
jugando = True
while jugando:
    ventana.blit(fondo, (0, 0))
    ventana.blit(ball, ballrect)
    ventana.blit(barra, barrarect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barrarect.left > 0:
        barrarect = barrarect.move(-5,0)
    if keys[pygame.K_RIGHT]and barrarect.right < 800:
        barrarect = barrarect.move(5,0)


    for brick in lista_ladrillos:
        ventana.blit(brick.img,brick.rect)
        if ballrect.colliderect(brick.rect):
            lista_ladrillos.remove(brick)
            speed[1] = -speed[1]

    # Velocidad al colisionar con la barra
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
        if speed[0] < 20 and speed[1] < 20:
            speed[0] += 1
            if speed[1] < 0:
                speed[1] -= 1
            else:
                speed[1] += 1

    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]


    # Pantalla de derrota
    if ballrect.bottom > 1000:
        ventana.blit(texto, texto_rect)
        pygame.mixer.Sound.play(pitidoarbi, 1)
        pygame.mixer.Sound.stop(musica_fondo)

    pygame.display.flip()
    pygame.time.Clock().tick(120)

pygame.quit()