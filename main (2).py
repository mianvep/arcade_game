import pygame
import sys,time

# this is the pygame initialization and initializing the main screen
pygame.init()
screensize=(1400,700)   #size of the screen
Width=1400
width = Width
Height=700
height = Height
colour=(255,0,10)
screen = pygame.display.set_mode((screensize)) #displaying the actual screen
font=pygame.font.SysFont("arialblack",30) #fonts
font2=pygame.font.SysFont("arialblack",18) #fonts
font3=pygame.font.SysFont("arialblack",50) #fonts




Animation=pygame.image.load("animation2/7.png")
Animation=pygame.transform.scale(Animation,(440,410))

Background=pygame.image.load("background game.jpg")
Background=pygame.transform.scale(Background,(width,height))

play=pygame.Surface.convert(pygame.image.load('PLay button.webp'))
play=pygame.transform.scale(play,(300,150))

quit=pygame.Surface.convert(pygame.image.load("QUIT button.webp"))
quit=pygame.transform.scale(quit,(300,150))

play1=pygame.Surface.convert(pygame.image.load('PLay button.webp'))
play1=pygame.transform.scale(play1,(120,75))
Level = 1

# Set up platforms
platforms = [
    pygame.Rect(100, height - 100, 200, 20),
    pygame.Rect(450, height - 250, 200, 20),
    pygame.Rect(100, height - 400, 200, 20),
    pygame.Rect(400, height - 570, 200, 20),
    pygame.Rect(1100, height - 420, 200, 20),
    pygame.Rect(880, height - 280, 200, 20),
    pygame.Rect(1300, height - 500, 200, 20),
]

Spikes = [
    pygame.Rect(1190, height - 470, 30, 50),
    pygame.Rect(600, height - 300, 30, 50),
    pygame.Rect(100, height - 450, 30, 50),
    pygame.Rect(480, height - 620, 30, 50),
]
coin1 = pygame.Rect(200,250,40,40)
coin2 = pygame.Rect(550,80,40,40)
coin3 = pygame.Rect(1320,120,40,40)
coin4 = pygame.Rect(560,120,40,40)
coin5 = pygame.Rect(1300,500,40,40)


pygame.mixer.music.load('song.mp3')

# Set the volume for the background music
pygame.mixer.music.set_volume(0.05)  # Set the volume to half for the background music

# Play the music indefinitely
pygame.mixer.music.play(-1)
class ClickableButton:
    def __init__(self, x_position, y_position, button_image, button_scale):
        # Set the button's image with the specified scale
        self.button_image = pygame.transform.scale(button_image, (int(button_image.get_width() * button_scale), int(button_image.get_height() * button_scale)))

        # Create a rectangle for the button and position it on the screen
        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (x_position, y_position)
        self.is_clicked = False

    def check_mouse_interaction(self):
        mouse_position = pygame.mouse.get_pos()

        # Initialize the clicked variable
        button_clicked = False

        # Check if the mouse is over the button and the left mouse button is pressed
        if self.button_rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked:
            # Set the button as clicked
            self.is_clicked = True
            button_clicked = True

        # Reset the clicked status if the left mouse button is not pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False

        return button_clicked

    def render(self, screen):
        action_taken = self.check_mouse_interaction()
        screen.blit(self.button_image, (self.button_rect.x, self.button_rect.y))
        return action_taken


playbutton= ClickableButton(570,320,play,1)
quitbutton= ClickableButton(570,500,quit,1)
playbutton1= ClickableButton(100,620,play1,1)

def drawtext(text,font,colour,x,y): #draws text with colour and font onto the screen
    image=font.render(text,True,colour)
    screen.blit(image,(x,y))

def Level_change(level):
    global platforms, Spikes
    if level == 2:
        platforms = [
                pygame.Rect(0, height - 500, 200, 20),
                pygame.Rect(450, height - 250, 140, 20),
                pygame.Rect(500, 180, 100, 20),
                pygame.Rect(200, height - 370, 100, 20),
                pygame.Rect(800, height - 420, 50, 20),
                pygame.Rect(1050, height - 280, 50, 20),
                pygame.Rect(1300, 600, 200, 20),
            ]
                
        Spikes = [
            # pygame.Rect(1190, height - 470, 30, 50),
            pygame.Rect(550, height - 300, 30, 50),
            pygame.Rect(200, height - 420, 30, 50),
            pygame.Rect(500, height - 570, 30, 50),
        ]
        

    elif level == 1:
        # Set up platforms
        platforms = [
            pygame.Rect(100, height - 100, 200, 20),
            pygame.Rect(450, height - 250, 200, 20),
            pygame.Rect(100, height - 400, 200, 20),
            pygame.Rect(400, height - 570, 200, 20),
            pygame.Rect(1100, height - 420, 200, 20),
            pygame.Rect(880, height - 280, 200, 20),
            pygame.Rect(1300, height - 500, 200, 20),
        ]

        Spikes = [
            pygame.Rect(1190, height - 470, 30, 50),
            pygame.Rect(600, height - 300, 30, 50),
            pygame.Rect(100, height - 450, 30, 50),
            pygame.Rect(480, height - 620, 30, 50),
        ]
       



def main(difficulty):
    global Level, coin1,coin2,coin3,coin4,coin5
    square_size = 50
    square_color = (255, 0, 0)  # Red
    square_x, square_y = 100,600
    square_speed = 15
    jump_strength = 50
    animate = 1
    # Set up hearts
    hearts = 3
    heart_image = pygame.transform.scale(pygame.image.load("heart.png"),(50,50))  # Replace "heart.png" with your heart image file
    spike_image = pygame.transform.scale(pygame.image.load("spike.png"),(50,50))  # Replace "heart.png" with your heart image file
    coin_image = pygame.transform.scale(pygame.image.load("coin.png"),(50,50))  # Replace "heart.png" with your heart image file

    coins = 0
     # Function to display math questions

 
    # Gravity settings
    gravity = 6
    fall_speed = 0

    # Flag to track if the square is on a platform
    on_platform = False

    # Flag to track the game state (paused or not)
    game_paused = False

    # Set up hearts
    hearts = 3

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gravity+=0.5
                elif event.key == pygame.K_b and gravity>0.5:
                    gravity-=0.5
                

        # Get the state of all keys
        keys = pygame.key.get_pressed()

        # Check if the square is on a platform
        on_platform = any(pygame.Rect(square_x, square_y + 10, square_size, square_size).colliderect(platform) for platform in platforms)

        # Check for collisions with the target rectangle
     
        if square_x>1300 and Level == 1:

            
            Level = 2
            square_x = 20
            Level_change(Level)

        if square_x<10 and Level == 2:
            
        
            Level = 1
            square_x = 1300
            Level_change(Level)
        if game_paused:
            pass
        # Update square position based on key input only if the game is not paused
        if not game_paused:
            
            
            
            Animation=pygame.image.load("animation2/"+str(animate)+".png")
            Animation=pygame.transform.scale(Animation,(440,410))
            if keys[pygame.K_LEFT] :
                if fall_speed == 0:
                    animate+=1
                    if animate>6:
                        animate = 1
                square_x -= square_speed
                Animation=pygame.image.load("animation2/"+str(animate)+".png")
                Animation=pygame.transform.scale(Animation,(440,410))
                Animation = pygame.transform.flip(Animation, True, False)
                
            elif keys[pygame.K_RIGHT] :
                if fall_speed == 0:
                    animate+=1
                    if animate>6:
                        animate = 1
                square_x += square_speed

            elif fall_speed == 0 or fall_speed == 0.5 :
                Animation=pygame.image.load("animation2/"+str(7)+".png")
                Animation=pygame.transform.scale(Animation,(440,410))
                

            # Check if the "Up" arrow key is pressed for jumping
            if keys[pygame.K_UP] and (square_y == height - square_size or on_platform):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('JUMP.mp3'))
                animate = 10
                
                fall_speed = -jump_strength  # Apply an upward force

            # Apply gravity
            fall_speed += gravity
            square_y += fall_speed

            # Check for collisions with platforms
            for platform in platforms:
                if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(platform) and fall_speed > 0:
                    square_y = platform.y - square_size
                    fall_speed = 0  # Stop falling when on a platform

            # Check if the square has fallen below the platforms
            if square_y > height:
                hearts -= 1
                Level = 1
                square_x, square_y = 100,500
                Level_change(Level)
                
            if hearts <= 0:
                # Game over, reset everything
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('DEATH.mp3'))
                drawtext('YOU LOSE!',font3,colour,570,350)
                
                                    
                pygame.display.update()
                time.sleep(3)
                coin1 = pygame.Rect(200,250,40,40)
                coin2 = pygame.Rect(550,80,40,40)
                coin3 = pygame.Rect(1320,120,40,40)
                coin4 = pygame.Rect(560,120,40,40)
                coin5 = pygame.Rect(1300,500,40,40)
                menu()
                    
                   

        # Fill the screen with a white background
        screen.blit(Background,(0,0))

        border_thickness = 1
        # Draw the platforms
        for platform in platforms:
           
            pygame.draw.rect(screen, (0, 0, 0), platform, border_thickness)

            # Draw the inner squares with the specified color
            for x in range(platform.left + border_thickness, platform.right - border_thickness, square_size):
                for y in range(platform.top + border_thickness, platform.bottom - border_thickness, square_size):
                    square_rect = pygame.Rect(x, y, square_size, square_size)
                    pygame.draw.rect(screen, 'brown', square_rect)
                    pygame.draw.rect(screen, (0, 0, 0), square_rect, border_thickness)

        for spike in Spikes:
            screen.blit(spike_image,(spike.x,spike.y))
            if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(spike):
                hearts -= 1
                square_x, square_y = 100,500
                Level = 1
                Level_change(Level)

        if square_y > height:
                hearts -= 1
                square_x, square_y = 100,500
                Level = 1
                Level_change(Level)
                
                if hearts == 0:
                    # Game over, reset everything
                    hearts = 3
                    square_x, square_y = 100,500
                    Level = 1
                    Level_change(Level)
                   

        # Draw the square on the screen
        screen.blit(Animation,(square_x-190,square_y-208))

        # Draw hearts
        for i in range(hearts):
            screen.blit(heart_image, (10 + i * 70, 10))

        # print(answer[3])
        if game_paused:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('WIN.wav'))
            drawtext('YOU WIN!',font3,colour,570,350)
            pygame.display.update()
            time.sleep(3)
            menu()

        drawtext('GRAVITY: '+str(gravity),font,'green',70,80)

        drawtext('Coins collected: '+str(coins),font,'yellow',1100,20)
        

        if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(coin1) and Level == 1:
            coin1.x = -1000
            coins+=1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('coin.wav'))

        if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(coin2) and Level == 1:
            coin2.x = -1000
            coins+=1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('coin.wav'))

        if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(coin3)  and Level == 1:
            coin3.x = -1000
            coins+=1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('coin.wav'))

        if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(coin4) and Level == 2:
            coin4.x = -1000
            coins+=1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('coin.wav'))

        if pygame.Rect(square_x, square_y, square_size, square_size).colliderect(coin5)  and Level == 2:
            coin5.x = -1000
            coins+=1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('coin.wav'))

        if coins == 5:
            game_paused = True
        # pygame.draw.rect(screen,'black',coin1)
        if Level == 1:
            screen.blit(coin_image,(coin1.x,coin1.y-10))
            screen.blit(coin_image,(coin2.x,coin2.y-10))
            screen.blit(coin_image,(coin3.x,coin3.y-10))

        if Level == 2:
            screen.blit(coin_image,(coin4.x,coin4.y-10))
            screen.blit(coin_image,(coin5.x,coin5.y-10))
        pygame.display.update()
            
        pygame.time.Clock().tick(50)

def menu():
    menustate='main' #for changing screens
    while True: # the main menu - to exit the game and updating the main menu
        # screen.blit(background,(0,0))
        screen.blit(Background,(0,0))
        if menustate =='playbutton':
            drawtext('This is the main game',font,(150,100,100),50,10)

        if menustate=='main': #main menu screen

            drawtext('MENU',font3,colour,320,80)
            if quitbutton.render(screen): 
                sys.exit() 
 
                    
            if playbutton.render(screen): #the playbutton (main game will be here)
                menustate='playbutton'
                main('easy')
                
        for event in pygame.event.get(): #loops over the game to check if the user has exited and to quit accordigly
            if event.type == pygame.QUIT:
                sys.exit() 
            

        pygame.display.update() #updates the images on to the screen
         # # Cap the frame rate
        
menu()