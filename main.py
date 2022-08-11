import pygame
import pymunk

pygame.init()
W, H = 800, 600
display = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60

def createSpace():
    space = pymunk.Space()
    space.gravity = (0, 1000)
    return space

def addBall(space, size, pos):
    mass = 1
    moment = pymunk.moment_for_circle(mass, 0, size)
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, size)
    shape.density = 1
    shape.elasticity = 0.85
    space.add(body, shape)
    return body

def addLine(space, a, b):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, a, b, 5)
    shape.elasticity = 1
    space.add(body)
    space.add(shape)

def drawCircle(screen, body, size):
    pos = int(body.position.x), int(body.position.y)
    color = (20, 255, 90)
    pygame.draw.circle(screen, color, pos, size)

def drawLine(_display, a, b):
    color = (100, 55, 255)
    pygame.draw.line(_display, color, a, b, 20)

space = createSpace()
ball = addBall(space, 10, (400, 300))

a1, b1 = (0, 500), (800, 550)
addLine(space, a1, b1)

a2, b2 = (W-50, H), (W, 0)
addLine(space, a2, b2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((20, 20, 20))
        drawCircle(display, ball, 10)
        drawLine(display, a1, b1)
        drawLine(display, a2, b2)

        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

if __name__ == '__main__':
    main()