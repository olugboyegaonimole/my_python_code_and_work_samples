import pygame, sys #gives you exit function
import random #place the snake's food in a random location
import time #sleep for a few seconds after the game ends



check_errors = pygame.init()  #initialise pygame, initial output was (6,0) ie 6 tasks, 0 errors
if check_errors[1] > 0:
    print("had {0} initial errors, quiting...".format(check_errors[1]))
    sys.exit(-1) #-1 is the standard error code
else:
    print("pygame successfully initialised")



#play surface
play_surface = pygame.display.set_mode((720, 460)) # x coordinate is measured from left to right, y from top to bottom
pygame.display.set_caption('snake game')
time.sleep(2)



#COLORS
red = pygame.Color(255,0,0) # r,g,b,alpha channel - game over
green = pygame.Color(0,255,0) # r,g,b,alpha channel - snake
black = pygame.Color(0,0,0) # r,g,b,alpha channel - score
white = pygame.Color(255,255,255) # r,g,b,alpha channel - background
brown = pygame.Color(165,42,42) # r,g,b,alpha channel - food



#frame controller to control the fps of the game
fps_controller = pygame.time.Clock() # this will update every frame



#important variables
snakePos = [100,50]
snakeBody = [[100,50], [90,50], [80,50]] # composed of blocks

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10] # a list of two numbers chosen at random
foodSpawn = True # a boolean to knnow if we've spawned a new food or not, initially set to true

score = 0
choice = 1


#direction
direction = 'RIGHT' # the direction, initially set to RIGHT
changeTo = direction # variable used for changing the direction



#game over function
def game_over(choice):
    myfont = pygame.font.SysFont('monaco', 72) # use system font or font file, here we use system font
    game_over_surface = myfont.render('Game Over', True, red) # for the second argument (anti aliasing) you can use a value (1) or a boolean (true), here we use true # the fourth argument is the background - none by default
    g_over_rectangle = game_over_surface.get_rect() # here we use the rectangular component of the game over surface
    g_over_rectangle.midtop = (360,15) # place the message somewhere in the middle and at the top
    play_surface.blit(game_over_surface, g_over_rectangle) # we have to put those things under the blare? surface

    # if we don't give an update after what we just did, it won't show up
    # so if you want that thing to show up on the screen you have to update the screen
    # to update we can use the update function or the flip function, here we use the flip function
    show_score(choice)
    pygame.display.flip() #update the screen
    time.sleep(5)
    pygame.quit() # close pygame wnidow
    sys.exit() # close console


def show_score(choice=1):
    scorefont = pygame.font.SysFont('monaco', 24) # use system font or font file, here we use system font
    score_surface = scorefont.render('Score: {}'.format(score), True, black) # for the second argument (anti aliasing) you can use a value (1) or a boolean (true), here we use true # the fourth argument is the background - none by default
    score_rectangle = score_surface.get_rect() # here we use the rectangular component of the  surface
    if choice == 1:
        score_rectangle.midtop = (80,20)
    else:
        score_rectangle.midtop = (360,120)

    play_surface.blit(score_surface, score_rectangle) # we have to put those things under the blare? surface



# event special occasion where something happens

# main logic

while 1:
    for event in pygame.event.get(): #here we accept the events (controls, inputs) to the game
        if event.type == pygame.QUIT: # FOR EVERY FRAME WE WILL GET AN EVENT, WE WILL LOOP THROUGH ALL THE EVENTS
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # VALIDATION OF DIRECTION
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'


    # UPDATE SNAKE POSITION
    if direction == 'RIGHT':
        snakePos[0] +=10
    if direction == 'LEFT':
        snakePos[0] -=10
    if direction == 'UP':
        snakePos[1] -=10
    if direction == 'DOWN':
        snakePos[1] +=10


    # SNAKE BODY
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score+=1
    
    else:
        snakeBody.pop()
    
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10] # a list of two numbers chosen at random
    foodSpawn = True


    # background
    play_surface.fill(white)


    # draw snake
    for position in snakeBody:
        rectangle = pygame.Rect(position[0], position[1], 10, 10)
        pygame.draw.rect(play_surface, green, rectangle)
    

    #draw food
    pygame.draw.rect(play_surface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))


    # collide with wall
    if snakePos[0] > 710 or snakePos[0] < 0:
        choice+=1
        game_over(choice)

    if snakePos[1] > 450 or snakePos[1] < 0:
        choice+=1
        game_over(choice)

    
    # collide with self
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            choice+=1
            game_over(choice)


    show_score(choice)
    pygame.display.flip() #update the screen
    fps_controller.tick(15)

    #convert to executable using installer
    #use images for snake body
    #use sounds
    #set up difficulty levels using     fps_controller.tick(?)
    #create a menu
    #create settings