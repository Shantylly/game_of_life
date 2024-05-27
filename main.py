import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1920,1080
size = (width, height)

pygame.init()
pygame.display.set_caption("Game Of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
red = (255, 0, 0)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 10
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_a:
                Grid.change_scale(1)
            if event.key == pygame.K_z:
                Grid.change_scale(-1)
            if event.key == pygame.K_q:
                Grid.change_size(1)
            if event.key == pygame.K_s:
                Grid.change_size(-1)
            if event.key is pygame.K_r:
                Grid.toggle_cell_type()
    
    Grid.Conway(off_color=white, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.AddCell(mouseX, mouseY)
    
    if pygame.mouse.get_pressed()[2]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.RemoveCell(mouseX, mouseY)


    pygame.display.update()

pygame.quit()
