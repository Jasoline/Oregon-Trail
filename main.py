import pygame
import pygame_widgets
from buttons import *

def start():
    # Initialize Pygame
    pygame.init()

    # Set window dimensions
    width = 1280
    height = 720

    # Create the window
    screen = pygame.display.set_mode((width, height))

    # Set window title
    pygame.display.set_caption("My Pygame Window")

    # Load background images
    bg_title = pygame.image.load("oregontrail.jpg").convert()
    bg_char = pygame.image.load("oregonchar.png").convert()
    bg_char = pygame.transform.scale(bg_char, (1280, 720))

    # Screen helper
    screen_helper = {'screen': 'title'}
    prev_screen = []
    

    # Quit button helper
    def close_window():
        nonlocal running
        running = False

    # Play button helper
    def click_play():
        screen_helper['screen'] = 'char_select'
        prev_screen.append('title')

    # Back button helper
    def click_back():
        screen_helper['screen'] = prev_screen.pop()
    
    def click_next():
        if screen_helper['screen'] == 'char_select':
            prev_screen.append('char_select')            
            screen_helper['screen'] = 'month_select'
        
        


    # Import button functionality
    credit_message = create_credit_message(screen)
    play_button = create_play_button(screen, click_play)
    quit_button = create_quit_button(screen, close_window)
    back_button = create_back_button(screen, click_back)
    next_button = create_next_button(screen, click_next)
    selection_message = create_selection_message(screen)
    name_inputs = create_name_inputs(screen)
    name_nums = create_name_num(screen)

    # Game loop
    running = True
    while running:
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Render title screen
        if screen_helper['screen'] == 'title':
            screen.fill((0, 0, 0))
            screen.blit(bg_title, (0, 0))

            # Draw the buttons
            play_button.listen(events)
            play_button.show()
            play_button.draw()
            quit_button.listen(events)
            quit_button.draw()
            quit_button.show()
            back_button.hide()            
            next_button.hide()

            
            credit_message.draw()

        # Render character selection screen
        elif screen_helper['screen'] == 'char_select':
            screen.fill((0, 0, 0))
            screen.blit(bg_char, (0, 0))

            # Draw the buttons
            play_button.hide()
            quit_button.hide()
            back_button.show()
            back_button.draw()
            next_button.show()
            next_button.draw()
            

            selection_message.draw()
            for num in name_nums:
                num.draw()

            # Draw input boxes
            for input_box in name_inputs:
                
                input_box.draw()

        elif screen_helper['screen'] == 'month_select':
            
            screen.fill((0, 0, 0))
            

            # Draw the buttons
            
            next_button.draw()
            
            back_button.draw()
            

        # Update the display
        pygame.display.flip()

        # Update widget events
        pygame_widgets.update(events)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    start()