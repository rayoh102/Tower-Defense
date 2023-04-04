import pygame
import os

pygame.init()
win = pygame.display.set_mode((500, 500))

# Load Images of the Character (there are two popular ways)
stationary = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))
# One way to do it - using the sprites that face left.
left =  [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L1.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L2.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L3.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L4.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L5.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L6.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L7.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L8.png")), (70, 70)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Hero", "L9.png")), (70, 70))]

# Another (faster) way to do it - using the sprites that face right.
right = [None]*10
for picIndex in range(1,10):
    right[picIndex-1] = pygame.image.load(os.path.join("Assets/Hero", "R" + str(picIndex) + ".png"))
    picIndex+=1


x = 250
y = 250
vel = 10
move_left = False
move_right = False
stepIndex = 0

# Draw the Game
def draw_game():
    global stepIndex
    win.fill((0, 0, 0))
    if stepIndex >= 36:
        stepIndex = 0
    if move_left:
        win.blit(left[stepIndex//4], (x, y))
        stepIndex += 1
    elif move_right:
        win.blit(right[stepIndex//4], (x,y))
        stepIndex += 1
    else:
        win.blit(stationary, (x,y))


# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_game()

    # Movement
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        x -= vel
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT]:
        x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        stepIndex = 0

    pygame.time.delay(30)
    pygame.display.update()
