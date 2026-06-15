from OpenGL.GL import *

def draw_ship(blink):

    glBegin(GL_QUADS)
    
    # Face Superior (Verde)
    glColor3f(0.75, 0.75, 0.78)
    glVertex3f(-0.5,  0.5, -1.0)
    glVertex3f( 0.5,  0.5, -1.0)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

    # Face Inferior (Azul Escuro)
    glColor3f(0.55, 0.55, 0.58)
    glVertex3f(-0.5, -0.5, -1.0)
    glVertex3f( 0.5, -0.5, -1.0)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Face Lateral Direita (Verde Escuro)
    glColor3f(0.35, 0.35, 0.38)
    glVertex3f( 0.5, -0.5, -1.0)
    glVertex3f( 0.5,  0.5, -1.0)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)

    # Face Lateral Esquerda (Verde Escuro)
    glColor3f(0.35, 0.35, 0.38)
    glVertex3f(-0.5, -0.5, -1.0)
    glVertex3f(-0.5,  0.5, -1.0)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Face Traseira (Azul)
    glColor3f(0.25, 0.25, 0.28)
    glVertex3f(-0.5, -0.5, -1.0)
    glVertex3f( 0.5, -0.5, -1.0)
    glVertex3f( 0.5,  0.5, -1.0)
    glVertex3f(-0.5,  0.5, -1.0)

    glEnd()

    # Criada com triângulos que partem da face frontal do cubo (Z = 0.5) até o bico (Z = 1.5)
    glBegin(GL_TRIANGLES)
    
    # Rampa Superior do Bico (Vermelho)
    glColor3f(0.85, 0.85, 0.90)
    glVertex3f( 0.0,  0.5,  1.5) # Ponta do bico (centralizada em X)
    glVertex3f(-0.5,  0.5,  0.5) # Canto superior esquerdo do cubo
    glVertex3f( 0.5,  0.5,  0.5) # Canto superior direito do cubo

    # Rampa Inferior do Bico (Vermelho Escuro)
    glColor3f(0.55, 0.55, 0.60)
    glVertex3f( 0.0,  0.5,  1.5)
    glVertex3f(-0.5, -0.5,  0.5) # Canto inferior esquerdo do cubo
    glVertex3f( 0.5, -0.5,  0.5) # Canto inferior direito do cubo

    # Lateral Esquerda do Bico
    glColor3f(0.45, 0.45, 0.50)
    glVertex3f( 0.0,  0.5,  1.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    # Lateral Direita do Bico
    glColor3f(0.45, 0.45, 0.50)
    glVertex3f( 0.0,  0.5,  1.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)

    glColor3f(0.40, 0.40, 0.45)
    # Face Superior da Asa
    glVertex3f(-0.5,  0.0,  0.0)  # Conectado na parede do cubo
    glVertex3f(-2.0, -0.2, -0.5)  # Ponta extrema da asa
    glVertex3f(-0.5,  0.0, -1.0)  # Conectado atrás na parede do cubo
    
    # Face Traseira da Asa
    glVertex3f(-2.0, -0.2, -0.5)
    glVertex3f(-0.5,  0.0, -1.0)
    glVertex3f(-0.5, -0.5, -1.0)
    
    # Face Dianteira da Asa
    glVertex3f(-0.5,  0.0,  0.0)
    glVertex3f(-2.0, -0.2, -0.5)
    glVertex3f(-0.5, -0.5,  0.0)
    
    # Face Inferior da Asa
    glVertex3f(-2.0, -0.2, -0.5)
    glVertex3f(-0.5, -0.5,  0.0)
    glVertex3f(-0.5, -0.5, -1.0)

    glColor3f(0.40, 0.40, 0.45)
    # Face Superior da Asa
    glVertex3f(0.5,  0.0,  0.0)
    glVertex3f(2.0, -0.2, -0.5)
    glVertex3f(0.5,  0.0, -1.0)
    
    # Face Traseira da Asa
    glVertex3f(2.0, -0.2, -0.5)
    glVertex3f(0.5,  0.0, -1.0)
    glVertex3f(0.5, -0.5, -1.0)
    
    # Face Dianteira da Asa
    glVertex3f(0.5,  0.0,  0.0)
    glVertex3f(2.0, -0.2, -0.5)
    glVertex3f(0.5, -0.5,  0.0)
    
    # Face Inferior da Asa
    glVertex3f(2.0, -0.2, -0.5)
    glVertex3f(0.5, -0.5,  0.0)
    glVertex3f(0.5, -0.5, -1.0)

    glEnd()
    # Propulsor
    glBegin(GL_QUADS)
    glColor3f(1, blink, 0)
    # Posicionado levemente recuado em Z (-1.01) para não dar conflito de pixels com a traseira do cubo
    glVertex3f(-0.3, -0.3, -1.01)
    glVertex3f( 0.3, -0.3, -1.01)
    glVertex3f( 0.3,  0.3, -1.01)
    glVertex3f(-0.3,  0.3, -1.01)
    glEnd()

def draw_meteor(size):
    glColor3f(0.5, 0.4, 0.3)
    glBegin(GL_QUADS)
    vertices = [
        [-size, -size, -size], [size, -size, -size], [size, size, -size], [-size, size, -size],
        [-size, -size, size], [size, -size, size], [size, size, size], [-size, size, size],
    ]
    faces = [[0,1,2,3], [4,5,6,7], [0,1,5,4], [2,3,7,6], [0,3,7,4], [1,2,6,5]]
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_police():
    glBegin(GL_TRIANGLES)

    glColor3f(0.8, 0.1, 0.1)
    glVertex3f(0, 0.3, 1)
    glVertex3f(-0.4, -0.3, 0)
    glVertex3f(0.4, -0.3, 0)

    glColor3f(0.5, 0, 0)
    glVertex3f(0, 0.3, 1)
    glVertex3f(0.4, -0.3, 0)
    glVertex3f(0, 0.2, -1)

    glVertex3f(0, 0.3, 1)
    glVertex3f(0, 0.2, -1)
    glVertex3f(-0.4, -0.3, 0)

    glColor3f(0.3, 0, 0)
    glVertex3f(-0.4, -0.3, 0)
    glVertex3f(0.4, -0.3, 0)
    glVertex3f(0, -0.3, -1)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)

    glVertex3f(-0.2, -0.1, -1.1)
    glVertex3f(0.2, -0.1, -1.1)
    glVertex3f(0.2, 0.1, -1.1)
    glVertex3f(-0.2, 0.1, -1.1)

    glEnd()

    glBegin(GL_TRIANGLES)

    # Asa esquerda
    glColor3f(0.6, 0.0, 0.0)
    glVertex3f(-0.4, -0.1, 0.2)
    glVertex3f(-1.0, -0.2, -0.3)
    glVertex3f(-0.4, 0.0, -0.3)
    
    # Asa direita
    glVertex3f(0.4, -0.1, 0.2)
    glVertex3f(1.0, -0.2, -0.3)
    glVertex3f(0.4, 0.0, -0.3)
    
    glEnd()

    glBegin(GL_QUADS)

    glColor3f(0.2, 0.5, 1.0)
    
    glVertex3f(-0.15, 0.1, 0.3)
    glVertex3f( 0.15, 0.1, 0.3)
    glVertex3f( 0.10, 0.25, -0.1)
    glVertex3f(-0.10, 0.25, -0.1)
    
    glEnd()