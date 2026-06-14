from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

from modelos import draw_ship, draw_meteor, draw_police

WIDTH, HEIGHT = 800, 600

NUM_STARS = 150
stars = [[random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-20, 1)] for _ in range(NUM_STARS)]

NUM_METEORS = 3
meteors = [[random.uniform(-4, 4), random.uniform(-3, -1), random.uniform(-20, -10), random.uniform(0.2, 0.4)] for _ in range(NUM_METEORS)]

# Variáveis de Controle (Animação e Tempo)
frame = 0
star_speed = 0.05
ship_vibration = 0.0
fov_zoom = 45.0
story_text = "---"
enemy_z = -25

# VARIAVEIS DE CONTROLE DAS NAVES
policia_y = 6.0
policia_z = -15.0
angulo_arrancada = 0.0
nave_z = -6.5

# texto
def draw_text(x, y, text):
    glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2i(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# função de update das fases
def update_logic(value):
    global frame, star_speed, ship_vibration, story_text, fov_zoom
    global policia_y, policia_z, angulo_arrancada, nave_z
    
    frame += 1
    segundos = frame / 60.0
    
    if segundos < 48.0:

        star_speed = 0.05
        ship_vibration = 0.0
        angulo_arrancada = 0.0
        nave_z = -6.5

    elif segundos < 55.0:
        
        star_speed = 0.05
        ship_vibration = random.uniform(-0.02, 0.02)

    elif segundos < 65.0:

        # POLICIA SE APROXIMA
        if policia_y > 1.5:
            policia_y -= 0.2
        if policia_z < -8.0:
            policia_z += 0.05
            
        ship_vibration = random.uniform(-0.03, 0.03)

    elif segundos < 67.0:

        if angulo_arrancada < 35.0:
            angulo_arrancada += 1.5
            
        ship_vibration = random.uniform(-0.08, 0.08)

    elif segundos < 70.0:

        star_speed = 0.8
        ship_vibration = random.uniform(-0.15, 0.15)
        
        policia_z += 0.8
        if angulo_arrancada > 0.0:
            angulo_arrancada -= 2.0
    
    else:
        
        star_speed = 1.2
        
        # DISTORÇÃO NA CAMERA
        nave_z -= 0.6
        if fov_zoom < 110.0:
            fov_zoom += 1.5
        
        # NAVE DA POLICIA FICA PARA TRAS
        policia_z += 1.5

    for star in stars:
        star[2] += star_speed
        if star[2] > 1:
            star[2] = random.uniform(-20, -10)
            star[0] = random.uniform(-5, 5)
            star[1] = random.uniform(-5, 5)

    for meteor in meteors:
        meteor[2] += star_speed * 1.2
        if meteor[2] > 2:
            meteor[2] = random.uniform(-30, -15)
            meteor[0] = random.uniform(-6, 6)

    glutPostRedisplay()
    glutTimerFunc(16, update_logic, 0)

# função de renderização
def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    glLoadIdentity()
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(fov_zoom, (WIDTH / HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # DESENHAR ESTRELAS
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    for star in stars:
        glVertex3f(star[0], star[1], star[2])
    glEnd()

    # DESENHAR METEOROS
    for meteor in meteors:
        glPushMatrix()
        glTranslatef(meteor[0], meteor[1], meteor[2])
        draw_meteor(meteor[3])
        glPopMatrix()

    segundos = frame / 60.0

    if segundos >= 55.0:
        glPushMatrix()
        glTranslatef(0.0, policia_y, policia_z)
        glScalef(3.0, 3.0, 3.0)
        draw_police()
        glPopMatrix()

    blink_value = (math.sin(frame * 0.5) + 1.0) / 2.0 if segundos >= 65.0 else 1.0

    float_y = math.sin(frame * 0.05) * 0.15          
    roll_z = math.cos(frame * 0.03) * 12.0          
    pitch_x = math.sin(frame * 0.02) * 5.0          

    glPushMatrix()
    
    # RECUO DA NAVE EM Z, PARA DAR IMPRESSAO DE DISTANCIA
    glTranslatef(0.0 + ship_vibration, -0.3 + float_y + ship_vibration, nave_z)
    
    glRotatef(pitch_x + angulo_arrancada, 1, 0, 0) 
    glRotatef(180, 0, 1, 0)     
    glRotatef(roll_z, 0, 0, 1)
    
    draw_ship(blink_value)
    glPopMatrix()

    # narrativa
    draw_text(30, 40, story_text)

    glutSwapBuffers()

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"Fuga / animacao")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(16, update_logic, 0)
    glutMainLoop()
