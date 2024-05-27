import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.current_cell_type = 1
        self.update_dimensions()

    def update_dimensions(self):
        self.columns = int(self.height / self.scale)
        self.rows = int(self.width / self.scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.zeros(self.size)

    def change_scale(self, change):
        self.scale += change
        self.update_dimensions()

    def change_size(self, change):
        self.width += change * self.scale
        self.height += change * self.scale
        self.update_dimensions()

    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,2)

    def Conway(self, off_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                #random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, (0, 0, 255), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                elif self.grid_array[x][y] == 2:
                    pygame.draw.rect(surface, (255, 0, 0), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    blue_neighbors, red_neighbors, neighbours = self.get_neighbours(x, y)
                    if neighbours == 3:
                        if (blue_neighbors > red_neighbors):
                            next[x][y] = 1
                        else:
                            next[x][y] = 2
                    elif (state == 1 or state == 2) and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    elif (neighbours == 6 or neighbours == 7):
                        if (blue_neighbors >= 4):
                            next[x][y] = 1
                        elif (red_neighbors >= 4):
                            next[x][y] = 2
                        else:
                            next[x][y] = state
                    else:
                        next[x][y] = state
            self.grid_array = next

    def toggle_cell_type(self):
        if self.current_cell_type == 1:
            self.current_cell_type = 2 
        else:
            self.current_cell_type = 1

    def AddCell(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = self.current_cell_type
    
    def RemoveCell(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = 0
        

    def get_neighbours(self, x, y):
        red_count = 0
        blue_count = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                if n == 0 and m == 0:
                    continue
                x_edge = (x + n + self.rows) % self.rows
                y_edge = (y + m + self.columns) % self.columns
                if self.grid_array[x_edge][y_edge] == 1:
                    blue_count += 1
                elif self.grid_array[x_edge][y_edge] == 2:
                    red_count += 1

        total = blue_count + red_count
        return (blue_count, red_count, total)
