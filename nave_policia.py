from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modelos import draw_police

# --- VARIÁVEIS DE TRANSFORMAÇÃO ---
angle_x = 0
angle_y = 0
angle_z = 0

tx, ty, tz = 0, 0, 0
sx, sy, sz = 1, 1, 1

blink = 0.0
direction = 1

def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

# --- FUNÇÕES DE TEXTO E MENU ---
def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))

def draw_menu():
    # Alterna temporariamente para projeção 2D ortogonal
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1, 1, 1)

    draw_text(-0.95, 0.9, "=== CONTROLES ===")
    draw_text(-0.95, 0.8, "Translacao:")
    draw_text(-0.95, 0.7, "t / T  -> eixo X")
    draw_text(-0.95, 0.6, "g / G  -> eixo Y")
    draw_text(-0.95, 0.5, "h / H  -> eixo Z")

    draw_text(-0.95, 0.4, "Rotacao:")
    draw_text(-0.95, 0.3, "x / X  -> eixo X")
    draw_text(-0.95, 0.2, "y / Y  -> eixo Y")
    draw_text(-0.95, 0.1, "z / Z  -> eixo Z")

    draw_text(-0.95, 0.0, "Escala:")
    draw_text(-0.95, -0.1, "r / R  -> eixo X")
    draw_text(-0.95, -0.2, "f / F  -> eixo Y")
    draw_text(-0.95, -0.3, "e / E  -> eixo Z")

    # Restaura as matrizes para não quebrar o ambiente 3D
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# --- DISPLAY ---
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # 1. Posiciona a câmera primeiro para o espaço 3D
    gluLookAt(0, 1, 6, 0, 0, 0, 0, 1, 0)
    
    # 2. Renderiza o modelo da nave aplicando as transformações interativas
    glPushMatrix()
    
    glTranslatef(tx, ty, tz)
    glScalef(sx, sy, sz)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)
    
    # CORREÇÃO 1: Passando o valor global 'blink' como argumento
    draw_police() 
    
    glPopMatrix()
    
    # CORREÇÃO 2: Renderiza o menu 2D por ÚLTIMO, garantindo que ele fique por cima de tudo
    draw_menu()
    
    glutSwapBuffers()

# --- ATUALIZAÇÃO DO MOTOR ---
def update(value):
    global blink, direction

    blink += 0.05 * direction

    if blink > 1:
        blink = 1
        direction = -1
    elif blink < 0:
        blink = 0
        direction = 1

    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

# --- ENTRADA DE TECLADO ---
def keyboard(key, x, y):
    global angle_x, angle_y, angle_z
    global tx, ty, tz
    global sx, sy, sz

    step = 0.2
    angle = 5
    scale = 0.1

    # Translação
    if key == b't': tx += step
    elif key == b'T': tx -= step
    elif key == b'g': ty += step
    elif key == b'G': ty -= step
    elif key == b'h': tz += step
    elif key == b'H': tz -= step

    # Rotação
    elif key == b'x': angle_x += angle
    elif key == b'X': angle_x -= angle
    elif key == b'y': angle_y += angle
    elif key == b'Y': angle_y -= angle
    elif key == b'z': angle_z += angle
    elif key == b'Z': angle_z -= angle

    # Escala
    elif key == b'e': sz += scale
    elif key == b'E': sz -= scale
    elif key == b'r': sx += scale
    elif key == b'R': sx -= scale
    elif key == b'f': sy += scale
    elif key == b'F': sy -= scale

    glutPostRedisplay()

def reshape(w, h):
    if h == 0: h = 1
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 50)

    glMatrixMode(GL_MODELVIEW)

# --- EXECUÇÃO ---
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Visualizador de Modelo Independente")

init()

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutReshapeFunc(reshape)
glutTimerFunc(0, update, 0)

glutMainLoop()