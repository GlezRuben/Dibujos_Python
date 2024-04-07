import pygame
import math
import random

pygame.init()

ANCHO_VENTANA = 800
ALTURA_VENTANA = 600
COLOR_FONDO = (0, 0, 0)
TAMAÑO_PARTICULA = 10
DURACION_PARTICULA = 5
NUM_PARTICULAS = 10000

COLOR_PARTICULAS = [(234, 128, 176)]

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("I Love You <3")

class Particle:
    def __init__(self):
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.age = 0
        self.color = (0, 0, 0)
        
    def initialize(self, x, y, dx, dy, color):
        self.position = [x, y]
        self.velocity = [dx, dy]
        self.acceleration = [dx*-0.75, dy*-0.75]
        self.age = 0
        self.color = color
        
    def update(self, delta_time):
        self.position[0] += self.velocity[0]*delta_time
        self.position[1] += self.velocity[1]*delta_time
        self.velocity[0] += self.acceleration[0]*delta_time
        self.velocity[1] += self.acceleration[1]*delta_time
        self.age += delta_time
        
    def draw(self, surface):
        size = TAMAÑO_PARTICULA * (1-self.age/DURACION_PARTICULA)
        alpha = int(255*(1-self.age/DURACION_PARTICULA))
        pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), int(size/2), 0, alpha)
        
class ParticlePool:
    def __init__(self, length):
        self.particles = [Particle() for _ in range(length)]
        self.first_active = 0
        self.first_free = 0
        
    def add(self, x, y, dx, dy, color):
        self.particles[self.first_free].initialize(x, y, dx, dy, color)
        self.first_free = (self.first_free + 1) % len(self.particles)
        if self.first_active == self.first_free:
            self.first_active = (self.first_active + 1) % len(self.particles)
            
    def update(self, delta_time):
        if self.first_active < self.first_free:
            for i in range(self.first_active, self.first_free):
                self.particles[i].update(delta_time)
        if self.first_free < self.first_active:
            for i in range(self.first_active, len(self.particles)):
                self.particles[i].update(delta_time)
            for i in range(0, self.first_free):
                self.particles[i].update(delta_time)
                
    def draw(self, surface):
        for i in range(len(self.particles)):
            if self.first_active < self.first_free:
                if self.first_active <= i < self.first_free:
                    self.particles[i].draw(surface)
            elif self.first_free < self.first_active:
                if not (self.first_free <= i < self.first_active):
                    self.particles[i].draw(surface)
                    
def point_on_heart(t):
    x = 160 * math.pow(math.sin(t), 3)
    y = 130 * math.cos(t) - 50*math.cos(2*t) - 20*math.cos(3*t) - 10*math.cos(4*t) + 25
    return [x, y]

particles = ParticlePool(NUM_PARTICULAS)
particle_rate = NUM_PARTICULAS / DURACION_PARTICULA

running = True
clock = pygame.time.Clock()
time = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    new_time = pygame.time.get_ticks() / 1000
    delta_time = new_time - (time or new_time)
    time = new_time
    
    screen.fill(COLOR_FONDO)
    
    amount = particle_rate * delta_time
    for _ in range(int(amount)):
        pos = point_on_heart(math.pi - 2 * math.pi * random.random())
        dir = [pos[0], -pos[1]]
        length = math.sqrt(dir[0] ** 2 + dir[1] ** 2)
        dir[0] = dir[0] * random.uniform(50, 150) / length
        dir[1] = dir[1] * random.uniform(50, 150) / length
        color = random.choice(COLOR_PARTICULAS)
        particles.add(ANCHO_VENTANA / 2 + pos[0], ALTURA_VENTANA / 2-pos[1], dir[0], dir[1], color)
    
    particles.update(delta_time)
    particles.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()