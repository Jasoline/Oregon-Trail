import pygame
import pygame_widgets
from buttons import create_credit_message, create_play_button, create_quit_button, create_back_button, create_selection_message, create_name_inputs, create_name_num

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

    # Quit button helper
    def close_window():
        nonlocal running
        running = False

    # Play button helper
    def click_play():
        screen_helper['screen'] = 'char_select'

    # Back button helper
    def click_back():
        screen_helper['screen'] = 'title'

    # Import button functionality
    credit_message = create_credit_message(screen)
    play_button = create_play_button(screen, click_play)
    quit_button = create_quit_button(screen, close_window)
    back_button = create_back_button(screen, click_back)
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
            screen.blit(bg_title, (0, 0))

            # Draw the buttons
            play_button.listen(events)
            play_button.draw()
            quit_button.listen(events)
            quit_button.draw()
            credit_message.draw()

        # Render character selection screen
        elif screen_helper['screen'] == 'char_select':
            screen.blit(bg_char, (0, 0))

            # Draw the buttons
            back_button.listen(events)
            back_button.draw()
            selection_message.draw()
            for num in name_nums:
                num.draw()

            # Draw input boxes
            for input_box in name_inputs:
                input_box.listen(events)
                input_box.draw()

        # Update the display
        pygame.display.flip()

        # Update widget events
        pygame_widgets.update(events)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    start()