import pygame
import sys
import time
import math

pygame.init()


W, H = 400, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()

center = (W // 2, H // 2)
radius = 150

def draw_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12 

    
    pygame.draw.circle(screen, (255, 255, 255), center, radius, 5)

    for i in range(12):
        angle = math.radians(i * 30) 
        start_x = center[0] + (radius - 20) * math.cos(angle)
        start_y = center[1] - (radius - 20) * math.sin(angle)
        end_x = center[0] + (radius - 40) * math.cos(angle)
        end_y = center[1] - (radius - 40) * math.sin(angle)
        pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 3)

   
    second_angle = math.radians(90 - seconds * 6)  
    second_end_x = center[0] + (radius - 20) * math.cos(second_angle)
    second_end_y = center[1] - (radius - 20) * math.sin(second_angle)
    pygame.draw.line(screen, (255, 0, 0), center, (second_end_x, second_end_y), 2)

    
    minute_angle = math.radians(90 - minutes * 6)  
    minute_end_x = center[0] + (radius - 40) * math.cos(minute_angle)
    minute_end_y = center[1] - (radius - 40) * math.sin(minute_angle)
    pygame.draw.line(screen, (0, 0, 0), center, (minute_end_x, minute_end_y), 6)

    hour_angle = math.radians(90 - (hours * 30 + minutes * 0.5)) 
    hour_end_x = center[0] + (radius - 60) * math.cos(hour_angle)
    hour_end_y = center[1] - (radius - 60) * math.sin(hour_angle)
    pygame.draw.line(screen, (0, 0, 0), center, (hour_end_x, hour_end_y), 8)

running = True
while running:
    screen.fill((255, 255, 255)) 
    draw_clock()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()  
    clock.tick(1) 

pygame.quit()
sys.exit()
