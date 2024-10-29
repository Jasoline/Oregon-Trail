import pygame
import pygame_widgets
import os
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
        pygame.mixer.music.load(os.path.join("songs", "The Oregon Trail_ Title Screen [ ezmp3.cc ].mp3"))
        pygame.mixer.music.play(-1)

        # Load background images
        bg_title = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'oregontrail.jpg')).convert()
        bg_char = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'oregonchar.png')).convert()
        bg_char = pygame.transform.scale(bg_char, (1280, 720))
        bg_saloon = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'pixelsaloon1.png')).convert()
        bg_saloon = pygame.transform.scale(bg_saloon, (500, 400))

        '''
        # Implement music
        music_background = pygame.mixer.music.load(os.path.join("songs", "The Oregon Trail_ Title Screen [ ezmp3.cc ].mp3"))
        music_travel = pygame.mixer.music.load(os.path.join("songs", "The Oregon Trail [ ezmp3.cc ].mp3"))
        music_event = pygame.mixer.music.load(os.path.join("songs", "The Long Road [ ezmp3.cc ].mp3"))
        music_death = pygame.mixer.music.load(os.path.join("songs", "A Whisper Of Winter [ ezmp3.cc ].mp3"))
        music_win = pygame.mixer.music.load(os.path.join("songs", "Trail's End [ ezmp3.cc ].mp3"))
        music_lose = pygame.mixer.music.load(os.path.join("songs", "Winter's Approach [ ezmp3.cc ].mp3"))
        music_shop = pygame.mixer.music.load(os.path.join("songs", "Around The Campfire [ ezmp3.cc ].mp3"))

        # Music helper(s)
        def load_music(type):
            pygame.mixer.music.load(type)

        def ever_music():
            pygame.mixer.music.play(1)

        def loop_music():
            pygame.mixer.music.play(-1)  #it's -1 to loop and 1 to just play it once

        def pause_music():
            pygame.mixer.music.pause()
        
        def unpause_music():
            pygame.mixer.music.unpause()
        
        def stop_music():
            pygame.mixer.music.stop()
        '''

        # Screen helper
        screen_helper = {'screen': 'title'}
        prev_screen = []

        # Track the selected month
        selected_month = None  # Start with no month selected

        # Quit button helper
        def close_window():
            nonlocal running
            running = False

        # Play button helper
        def click_play():
            prev_screen.append(screen_helper['screen'])
            screen_helper['screen'] = 'char_select'

        # Back button helper
        def click_back():
            screen_helper['screen'] = prev_screen.pop()
            if screen_helper['screen'] == 'title':
                back_button.hide()
                next_button.hide()

        def click_next():
            prev_screen.append(screen_helper['screen'])
            if screen_helper['screen'] == 'char_select':
                screen_helper['screen'] = 'month_select'
                next_button.hide()
            elif screen_helper['screen'] == 'month_select':
                screen_helper['screen'] = 'store'

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

                play_button.show()
                credit_message.show()
                quit_button.show()
                play_button.draw()
                quit_button.draw()
                credit_message.draw()


            # Render character selection screen
            elif screen_helper['screen'] == 'char_select':
                screen.fill((0, 0, 0))
                screen.blit(bg_char, (0, 0))

                # Draw the buttons
                credit_message.hide()
                play_button.hide()
                quit_button.hide()
                back_button.show()
                next_button.show()
                back_button.draw()
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

                back_button.draw()

                # Load fonts

                font = pygame.font.Font(
                    os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25)
                font1 = pygame.font.Font(
                    os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35)

                # Story text
                lines = [
                    "It is February of 1852 in Independence, Missouri. Over the past few years you have been hearing",
                    "rumblings of prospectors getting rich from gold in California. Late last year a traveller in town",
                    "spread word of the first nuggets being discovered in Oregon. You decide to spend your last bit of",
                    "inheritance to scrape together supplies and a band of travellers and hit the Oregon trail to fulfill",
                    "your dreams of a lavish lifestyle powered by gold! Begin planning your expedition. When will you leave?"
                ]
                y_offset = 0
                for line in lines:
                    story = font.render(line, True, (255, 255, 255))
                    screen.blit(story, (25, 25 + y_offset))  # Align text to the left with an x-offset of 50
                    y_offset += story.get_height()

                # Month options
                month_lines = ["1.    March", "2.    April", "3.    May", "4.    June", "5.    July"]

                # Check for key presses to update the selected month
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    selected_month = 0  # March
                    next_button.draw()
                    next_button.show()
                    self.stats.month = 3
                elif keys[pygame.K_2]:
                    selected_month = 1  # April
                    self.stats.month = 4
                elif keys[pygame.K_3]:
                    selected_month = 2  # May
                    self.stats.month = 5
                elif keys[pygame.K_4]:
                    selected_month = 3  # June
                    self.stats.month = 6
                elif keys[pygame.K_5]:
                    selected_month = 4  # July
                    self.stats.month = 7
                if self.stats.month != 0:
                    next_button.show()
                    next_button.draw()
                # Draw month options with red selection
                i = 0  # Index counter for tracking the month
                for line in month_lines:
                    if selected_month == i:
                        color = (255, 0, 0)
                    else:
                        color = (255, 255, 255)
                    months = font1.render(line, True, color)
                    screen.blit(months, (150, 100 + y_offset))  # Align text to the left with an x-offset of 50
                    y_offset += months.get_height()
                    i += 1  # Increment the index

                # example how to display stats variables
                # screen.blit(font.render(str(self.stats.month), True, color), (50, 600))

                # Draw the prompt
                prompt = font1.render("What is your choice?", True, (255, 255, 255))
                screen.blit(prompt, (75, 500))

                # Draw the saloon image
                screen.blit(bg_saloon, (625, 175))

            elif screen_helper['screen'] == 'store':
                screen.fill((0, 0, 0))
                pygame.mixer.music.unload()
                pygame.mixer.music.load(os.path.join("songs", "Around The Campfire [ ezmp3.cc ].mp3"))
                pygame.mixer.music.play(-1)
                # Draw the inventory items
                inventory_items = [
                    "Oxen",
                    "Food",
                    "Clothing",
                    "Ammunition",
                    "Spare Parts"
                ]

                # Load font
                font = pygame.font.Font(
                    os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25)

                # Calculate the y-coordinate for the first item
                y_offset = 175

                # Draw each inventory item on a separate line
                for item in inventory_items:
                    item_text = font.render(item, True, (255, 255, 255))
                    item_x = 25  # Calculate the x-coordinate to center the text
                    screen.blit(item_text, (item_x, y_offset))
                    y_offset += item_text.get_height() + 10  # Add some spacing between items
            elif screen_helper['screen'] == 'game':
                screen.fill((0, 0, 0))
                pygame.mixer.music.unload()
                pygame.mixer.music.load(os.path.join("songs", "The Oregon Trail [ ezmp3.cc ].mp3"))
                pygame.mixer.music.play(-1)

                # Draw the buttons
                back_button.draw()
                # Draw the stats
                stats_text = font.render(f"Month: {self.stats.month_name}  Day: {self.stats.day}", True,
                                         (255, 255, 255))
                screen.blit(stats_text, (width - stats_text.get_width() - 25, 25))

                # Load fonts
                font = pygame.font.Font(
                    os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25)
                font1 = pygame.font.Font(
                    os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35)

            # Update the display
            pygame.display.flip()

            # Update widget events
            pygame_widgets.update(events)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    m = main()
    m.start()
