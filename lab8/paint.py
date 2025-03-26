import pygame
import sys

pygame.init()


w , h = 800, 600
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Paint")

WH = (255, 255, 255)
b = (0, 0, 0)
cp = {
    pygame.K_1: b,
    pygame.K_2: (255, 0, 0),
    pygame.K_3: (0, 255, 0),
    pygame.K_4: (0, 0, 255),
    pygame.K_5: (255, 255, 0),
}


clk = pygame.time.Clock()
sc.fill(WH)
drawg = False
tool = "line"
color = b
start_pos = (0, 0)

ERASER_SIZE = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                drawing = True
                if tool == "line":
                    pygame.draw.circle(sc, color, event.pos, 2)

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "line":
                    pygame.draw.line(sc, color, start_pos, event.pos, 3)
                    start_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.rect(sc, WH,
                                     (event.pos[0] - ERASER_SIZE // 2,
                                      event.pos[1] - ERASER_SIZE // 2,
                                      ERASER_SIZE, ERASER_SIZE))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool == "rect":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]),
                                       abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(sc, color, rect, 2)
                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 +
                                  (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(sc, color, start_pos, radius, 2)
            drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key in cp:
                color = cp[event.key]

    pygame.display.update()
    clk.tick(60)