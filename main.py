import pygame
import pygame_widgets
from buttons import *
from stats import *


class main:
    def __init__(self):
        self.stats = Stats()

    def start(self):
        # Initialize Pygame
        pygame.init()

        # Set window dimensions
        width = 1280
        height = 720

        # Create the window
        screen = pygame.display.set_mode((width, height))

        # Set window title
        pygame.display.set_caption("Oregon Trail")

        # Load background images
        bg_title = pygame.image.load("oregontrail.jpg").convert()
        bg_char = pygame.image.load("oregonchar.png").convert()
        bg_char = pygame.transform.scale(bg_char, (1280, 720))
        bg_saloon = pygame.image.load("pixelsaloon1.png").convert()
        bg_saloon = pygame.transform.scale(bg_saloon, (500, 400))

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
                font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 25)
                font1 = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 35)
                lines = ["It is February of 1852 in Independence, Missouri. Over the past few years you have been hearing",
                         "rumblings of prospectors getting rich from gold in California. Late last year a traveller in town",
                         "spread word of the first nuggets being discovered in Oregon. You decide to spend your last bit of",
                         "inheritance to scrape together supplies and a band of travellers and hit the Oregon trail to filfull" ,
                         "your dreams of a lavish lifestlye powered by gold! Begin planning your expedition. When will you leave?"]
                y_offset = 0
                for line in lines:
                    txtsurf = font.render(line, True, (255, 255, 255))
                    screen.blit(txtsurf, (25, 25 + y_offset))  # Align text to the left with an x-offset of 50
                    y_offset += txtsurf.get_height()

                lines = ["1.    March", "2.    April", "3.    May", "4.    June", "5.    July"]
                for line in lines:
                    txtsurf = font1.render(line, True, (255, 255, 255))
                    screen.blit(txtsurf, (150, 100 + y_offset))  # Align text to the left with an x-offset of 50
                    y_offset += txtsurf.get_height()

                txtsurf = font1.render("What is your choice?", True, (255, 255, 255))
                screen.blit(txtsurf, (75, 500))  # Align text to the left with an x-offset of 50
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    print("March selected")
                elif keys[pygame.K_2]:
                    print("April selected")
                elif keys[pygame.K_3]:
                    print("May selected")
                elif keys[pygame.K_4]:
                    print("June selected")
                elif keys[pygame.K_5]:
                    print("July selected")

                # Import saloon cutout image
                screen.blit(bg_saloon, (625, 175))

            # Update the display
            pygame.display.flip()

            # Update widget events
            pygame_widgets.update(events)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    m = main()
    m.start()
