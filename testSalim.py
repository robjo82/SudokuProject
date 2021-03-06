import pygame

pygame.init()

#Get the screen
pygame.display.set_caption("Sudoku")
screen_size = 600, 600
background_color = (255, 255, 255)
added_element_color = (50, 30, 150)
buffer = 5

grid_completed = [
    [2,9,4,3,5,7,8,1,6],
    [3,5,7,8,1,6,9,2,4],
    [8,1,6,9,2,4,5,3,7],
    [5,7,9,6,3,8,1,4,2],
    [4,3,1,5,7,2,6,8,9],
    [6,2,8,4,9,1,7,5,3],
    [1,4,5,2,6,3,9,7,8],
    [9,6,3,7,8,5,2,4,1],
    [7,8,2,1,4,9,3,6,5]
]

grid_original = [
    [0,3,9,6,7,8,4,2,1],
    [6,7,2,1,9,5,3,4,8],
    [1,4,8,3,5,2,9,7,6],
    [8,5,7,9,0,1,2,3,4],
    [3,6,4,2,8,7,1,9,5],
    [0,2,1,4,3,9,8,5,7],
    [7,1,3,8,2,4,5,6,9],
    [4,9,5,7,1,3,6,8,2],
    [2,8,6,5,4,9,7,1,0]
]

grid = grid_original


def insert(screen, position):
        font = pygame.font.SysFont("Inter", 35)
        i = position[1]
        j = position[0]
        while True :
             for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    #1. tries to edit the original grid
                    if (grid_original[i-1][j-1] != 0):
                       return
                    #2. edit
<<<<<<< HEAD
                    if(event.key == 48): #checking with 0
                        pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50 + buffer,50 - 2*buffer,50 - 2*buffer))
                        value = font.render(str(event.key-48), True, (50, 30, 150))
                        screen.blit(value, (position[0]*50+18, position[1]*50+15))
                        grid[i-1][j-1] = 0
=======
                    if(event.key ==48): #checking with 0
                        grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50 + buffer,50 - 2*buffer,50 - 2*buffer))
>>>>>>> 029c3efa9ac0eb83a70833a62f2439e826769c7a
                        pygame.display.update()
                        return
                    #3. adding digits to the grid
                    if(1 < event.key - 48 < 10) : #Checking for valid input
                        pygame.draw.rect(screen, background_color, (position[0]*50 + buffer, position[1]*50 + buffer,50 - 2*buffer,50 - 2*buffer))
                        value = font.render(str(event.key-48), True, (50, 30, 150))
                        screen.blit(value, (position[0]*50+18, position[1]*50+15))
                        grid[i-1][j-1] = event.key - 48
                        pygame.display.update()
                        return
                    return


def main():
    screen = pygame.display.set_mode(screen_size)
    screen.fill(background_color)
    font = pygame.font.SysFont("Inter", 35)


    for i in range(10):
        if(i%3 == 0):   #If the number is divisible by 3, draw a line
            pygame.draw.line(screen, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i ,500), 4) # Vertical bold lines : line(Surface, color, start_pos, end_pos, width)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 4) # Horizontal bold lines
        pygame.draw.line(screen, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i ,500), 2) # Vetical lines
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2) # Horizontal lines
        pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0,len(grid[0])):
            if(0<grid[i][j]<10):
                text = font.render(str(grid[i][j]), True, (0,0,0))
                screen.blit(text, ((j+1)*50 + 20, (i+1)*50 + 15)) # blit(text, position)
    pygame.display.update()
    running = True

    while running :

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    insert(screen, (pos[0]//50,pos[1]//50))

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    


main()    