import pygame
import pygame_widgets
import os
from buttons import *
from stats import *
import random
from randomizer import *


class Main:
    def __init__(self):
        self.stats = Stats()

    def start(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()

        # Set window dimensions
        width = 1280
        height = 720

        # Create the window
        screen = pygame.display.set_mode((width, height))

        # Set window title
        pygame.display.set_caption("Oregon Trail")

        # Load background images
        bg_title = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'oregontrail.jpg')).convert()
        bg_char = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'oregonchar.png')).convert()
        bg_char = pygame.transform.scale(bg_char, (1280, 720))
        bg_saloon = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'pixelsaloon1.png')).convert()
        bg_saloon = pygame.transform.scale(bg_saloon, (500, 400))
        bg_independence = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'independ.png')).convert()
        bg_kearney = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'kearney.png')).convert()
        bg_chimney = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'chimney.png')).convert()
        bg_laramie = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'laramie.png')).convert()
        bg_bridger = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'bridger.png')).convert()
        bg_hall = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'hall.png')).convert()
        bg_boise = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'boise.png')).convert()
        bg_mountain = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'mountain.png')).convert()
        bg_willamette = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'willame.png')).convert()

        # Implement music
        music_title = (
            os.path.join(os.path.dirname(__file__), "songs", "The Oregon Trail_ Title Screen [ ezmp3.cc ].mp3"))
        music_travel = (os.path.join(os.path.dirname(__file__), "songs", "The Oregon Trail [ ezmp3.cc ].mp3"))
        music_event = (os.path.join(os.path.dirname(__file__), "songs", "The Long Road [ ezmp3.cc ].mp3"))
        music_death = (os.path.join(os.path.dirname(__file__), "songs", "A Whisper Of Winter [ ezmp3.cc ].mp3"))
        music_win = (os.path.join(os.path.dirname(__file__), "songs", "Trail's End [ ezmp3.cc ].mp3"))
        music_lose = (os.path.join(os.path.dirname(__file__), "songs", "Winter's Approach [ ezmp3.cc ].mp3"))
        music_shop = (os.path.join(os.path.dirname(__file__), "songs", "Around The Campfire [ ezmp3.cc ].mp3"))

        # Load fonts
        font = pygame.font.Font(
            os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25)
        font1 = pygame.font.Font(
            os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35)
        font2 = pygame.font.Font(
            os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 20)

        # Music helper(s)
        def load_music(music):
            pygame.mixer.music.load(music)

        def ever_music():
            pygame.mixer.music.play(-1)

        def loop_music():
            pygame.mixer.music.play(1)

        def pause_music():
            pygame.mixer.music.pause()

        def unpause_music():
            pygame.mixer.music.unpause()

        def unload_music():
            pygame.mixer.music.unload()

        # Screen helper
        screen_helper = {'screen': 'game'}

        prev_screen = []

        # Track Variables
        selected_month = None  # Start with no month selected
        selected_item = None  # Start with no item selected
        selected_choice = None  # Start with no choice selected
        rested = False
        game_event = None
        hunt = None
        seen = {}
        cost = 0
        store = {'oxen': 0, 'food': 0, 'clothing': 0, 'ammo': 0, 'spare_parts': 0}
        self.total_distances = {
            0: "Independence, Missouri",
            102: "Kansas River Crossing",
            184: "Big Blue River Crossing",
            302: "Fort Kearny",
            552: "Chimney Rock",
            638: "Fort Laramie",
            828: "Independence Rock",
            930: "South Pass",
            1055: "Fort Bridger",
            987: "Green River Crossing",
            1169: "Fort Hall",
            1283: "Snake River Crossing",
            1443: "Fort Boise",
            1568: "Blue Mountains",
            1700: "The Dalles",
            1800: "Willamette Valley, Oregon",
            1850: "Oregon City"
        }
        total_distances = [
            0,    # Independence, Missouri
            102,  # Kansas River Crossing
            184,  # Big Blue River Crossing
            302,  # Fort Kearny
            552,  # Chimney Rock
            638,  # Fort Laramie
            828,  # Independence Rock
            930,  # South Pass
            1055, # Fort Bridger
            987,  # Green River Crossing
            1169, # Fort Hall
            1283, # Snake River Crossing
            1443, # Fort Boise
            1568, # Blue Mountains
            1700, # The Dalles
            1800,  # Willamette Valley, Oregon
            1850
        ]
        location_images = [
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'independ.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'kearney.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'chimney.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'laramie.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'bridger.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'hall.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'boise.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'mountain.png')).convert(),
            pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'willame.png')).convert()
        ]
        locationindex = 0
        next_location = self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)]
        prev_choice = None
        # Quit button helper
        def close_window():
            nonlocal running
            running = False

        # Play button helper
        def click_play():
            prev_screen.append(screen_helper['screen'])
            screen_helper['screen'] = 'char_select'
            credit_message.hide()
            play_button.hide()
            quit_button.hide()

        # Back button helper
        def click_back():
            screen_helper['screen'] = prev_screen.pop()
            next_button.hide()
            back_button.hide()

        def click_next():
            prev_screen.append(screen_helper['screen'])
            if screen_helper['screen'] == 'char_select':
                screen_helper['screen'] = 'month_select'

            elif screen_helper['screen'] == 'month_select':
                screen_helper['screen'] = 'store'

            elif screen_helper['screen'] == 'store':
                screen_helper['screen'] = 'game'
                for key, value in store.items():
                    if key == 'ammo':
                        setattr(self.stats, key, getattr(self.stats, key) + value * 20)
                    else:
                        setattr(self.stats, key, getattr(self.stats, key) + value)
                    store[key] = 0
                self.stats.money -= cost



            back_button.hide()
            next_button.hide()

        # Import button functionality
        credit_message = create_credit_message(screen)
        play_button = create_play_button(screen, click_play)
        quit_button = create_quit_button(screen, close_window)
        back_button = create_back_button(screen, click_back)
        next_button = create_next_button(screen, click_next)
        selection_message = create_selection_message(screen)
        name_inputs = create_name_inputs(screen)
        name_nums = create_name_num(screen)
        user_input = TextBox(
            screen,
            width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
            textColour=(247, 250, 248),
            font=font1, margin=25, colour=(62, 66, 64), radius=5,
        )

        i = 0
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

                # Change music
                if not pygame.mixer.music.get_busy():
                    load_music(music_title)
                    ever_music()

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
                back_button.show()
                back_button.draw()

                selection_message.draw()
                for num in name_nums:
                    num.draw()

                # Draw input boxes
                for input_box in name_inputs:
                    input_box.draw()

                # Only allow next if all input is complete
                if all(input_box.getText() != "" for input_box in name_inputs):
                    next_button.show()
                    next_button.draw()

            # Render month selection screen
            elif screen_helper['screen'] == 'month_select':
                screen.fill((0, 0, 0))
                back_button.draw()
                back_button.show()

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

            # Render store screen
            elif screen_helper['screen'] == 'store':
                screen.fill((0, 0, 0))

                # Draw the inventory items
                back_button.draw()
                back_button.show()
                inventory_items = [
                    f"1. Oxen                    ($40 each): {store['oxen']} ",
                    f"2. Food           ($0.2 a pound): {store['food']} ",
                    f"3. Clothing          ($10 a set): {store['clothing']} ",
                    f"4. Ammunition   ($2 for 20): {store['ammo']} ",
                    f"5. Spare Parts ($10 each): {store['spare_parts']} "
                ]

                # Change music
                unload_music()
                if not pygame.mixer.music.get_busy():
                    load_music(music_shop)
                    ever_music()

                # Calculate the y-coordinate for the first item
                y_offset = 175

                # Draw the prompt for the store
                prompt = font1.render(f"What would you like to buy? You have ${self.stats.money}", True, (255, 255, 255))
                screen.blit(prompt, (width // 2 - prompt.get_width() // 2, 100))

                # Draw each inventory item on a separate line
                i = 0
                for item in inventory_items:
                    label, value = item.split(': ')[0] + ':', item.split(': ')[1]
                    if selected_item == i:
                        label_color = (255, 0, 0)
                        value_color = (255, 0, 0)
                    else:
                        label_color = (255, 255, 255)
                        value_color = (255, 255, 255)

                    label_text = font.render(label, True, label_color)
                    value_text = font.render(value, True, value_color)

                    label_x = (width - label_text.get_width() - 20) // 2  # Center labels
                    value_x = label_x + label_text.get_width() + 20  # Center values next to labels



                    screen.blit(label_text, (label_x, y_offset + 50))
                    screen.blit(value_text, (value_x, y_offset + 50))

                    y_offset += label_text.get_height() + 10  # Add some spacing between items
                    i += 1  # Increment the index

                # Get user input for each item
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1] and selected_item is None:
                    selected_item = 0
                elif keys[pygame.K_2] and selected_item is None:
                    selected_item = 1
                elif keys[pygame.K_3] and selected_item is None:
                    selected_item = 2
                elif keys[pygame.K_4] and selected_item is None:
                    selected_item = 3
                elif keys[pygame.K_5] and selected_item is None:
                    selected_item = 4
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        selected_item = None

                        user_input = TextBox(
                            screen,
                            width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
                            textColour=(247, 250, 248),
                            font=font1, margin=25, colour=(62, 66, 64), radius=5,
                        )

                if len(user_input.getText()) == 2 and (selected_item == 0 or selected_item == 2 or selected_item == 3):
                    text = user_input.getText()[0:2]
                    user_input = TextBox(
                        screen,
                        width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
                        textColour=(247, 250, 248),
                        font=font1, margin=25, colour=(62, 66, 64), radius=5,
                    )
                    user_input.setText(text)
                elif len(user_input.getText()) == 4 and selected_item == 1 :
                    text = user_input.getText()[0:4]
                    user_input = TextBox(
                        screen,
                        width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
                        textColour=(247, 250, 248),
                        font=font1, margin=25, colour=(62, 66, 64), radius=5,
                    )
                    user_input.setText(text)
                elif len(user_input.getText()) == 1 and selected_item == 4:
                    text = user_input.getText()[0:1]
                    user_input = TextBox(
                        screen,
                        width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
                        textColour=(247, 250, 248),
                        font=font1, margin=25, colour=(62, 66, 64), radius=5,

                    )
                    user_input.setText(text)
                if selected_item is None:
                    user_input = TextBox(
                        screen,
                        width // 2 - 50, height - 175, 100, 50,  # Centered horizontally and positioned at the bottom
                        textColour=(247, 250, 248),
                        font=font1, margin=25, colour=(62, 66, 64), radius=5,
                    )

                cost = store['oxen'] * 40 + store['food'] * 0.2 + store['clothing'] * 10 + store['ammo'] * 2 + store['spare_parts'] * 10
                input_prompt = font2.render("Enter quantity here:", True, (255, 255, 255))
                screen.blit(input_prompt, (width // 2 - input_prompt.get_width() // 2, height - 225))
                user_input.draw()
                user_input_text = user_input.getText()
                total_cost_text = font2.render(f"Total cost: ${cost}", True, (255, 255, 255))
                screen.blit(total_cost_text, (width // 2 - total_cost_text.get_width() // 2, 450))
                if user_input_text == "":
                    if selected_item == 0:
                        store['oxen'] = 0
                    elif selected_item == 1:
                        store['food'] = 0
                    elif selected_item == 2:
                        store['clothing'] = 0
                    elif selected_item == 3:
                        store['ammo'] = 0
                    elif selected_item == 4:
                        store['spare_parts'] = 0

                if user_input_text.isdigit():
                    if selected_item == 0:
                        store['oxen'] = int(user_input_text)
                    elif selected_item == 1:
                        store['food'] = int(user_input_text)

                    elif selected_item == 2:
                        store['clothing'] = int(user_input_text)

                    elif selected_item == 3:
                        store['ammo'] = int(user_input_text)
                    elif selected_item == 4:
                        store['spare_parts'] = int(user_input_text)


                if self.stats.oxen != 0 or store['oxen']!=0 and cost <= self.stats.money:
                    next_button.show()
                    next_button.draw()
                else:
                    next_button.hide()

            # Render game screen
            elif screen_helper['screen'] == 'game':
                screen.fill((0, 0, 0))
                stats_text = font.render(f"{self.stats.month_name} {self.stats.day}, 1848", True, (255, 255, 255))
                screen.blit(stats_text, ((width - stats_text.get_width()) // 2, 25))

                # Change music
                unload_music()
                if not pygame.mixer.music.get_busy():
                    load_music(music_travel)
                    ever_music()

                lines = ["1. Continue on the trail", "2. Check supplies", "3. Stop to rest", "4. Hunt for food",
                         "5. Attempt to trade", "6. Purchase supplies", "7. Quit"]
                if prev_choice == 1:
                    screen.blit(font.render("You must rest first before traveling again", True, (255, 255, 255)), (width // 4 + 50, 600))
                # Display the options
                if pygame.key.get_pressed()[pygame.K_1]:
                    if prev_choice != 1:
                        selected_choice = 1

                elif pygame.key.get_pressed()[pygame.K_2]:
                    selected_choice = 2
                elif pygame.key.get_pressed()[pygame.K_3]:
                    selected_choice = 3

                elif pygame.key.get_pressed()[pygame.K_4]:
                    selected_choice = 4
                elif pygame.key.get_pressed()[pygame.K_5]:
                    selected_choice = 5
                elif pygame.key.get_pressed()[pygame.K_6]:
                    selected_choice = 6
                elif pygame.key.get_pressed()[pygame.K_7]:
                    selected_choice = 7
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if selected_choice == 1:
                            if self.stats.oxen == 0:
                                screen_helper['screen'] = 'gameover'
                                unload_music()
                                if not pygame.mixer.music.get_busy():
                                    load_music(music_lose)
                                    ever_music()
                            elif self.stats.distance_travelled == 1800:
                                screen_helper['screen'] = 'win'
                                unload_music()
                                if not pygame.mixer.music.get_busy():
                                    load_music(music_win)
                                    ever_music()
                            else:
                                prev_screen.append(screen_helper['screen'])
                                screen_helper['screen'] = 'travel'
                                prev_choice = None

                        elif selected_choice == 2:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'display_supplies'
                            selected_choice = None
                        elif selected_choice == 3:
                            prev_screen.append(screen_helper['screen'])
                            prev_choice = 3
                            screen_helper['screen'] = 'rest'
                            user_input = TextBox(
                                screen,
                                width // 2 - 26, height - 175, 52, 50,
                                # Centered horizontally and positioned at the bottom
                                textColour=(247, 250, 248),
                                font=font1, margin=25, colour=(62, 66, 64), radius=5,
                            )
                            selected_choice = None
                        elif selected_choice == 4:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'hunt'
                            if self.stats.ammo >= 10:
                                self.stats.ammo -= 10
                                self.stats.days_passed += 1
                                self.stats.day += 1
                                if random.randint(0, 9) <= 2:
                                    hunt = random.randint(10, 70)
                                    self.stats.food += hunt

                                else:
                                    hunt = None
                            else:
                                hunt = -1
                            selected_choice = None
                        elif selected_choice == 5:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'trade'

                            self.stats.days_passed += 1
                            self.stats.day += 1
                            trade_options = {
                                1: ["oxen", random.randint(1, 2)],
                                2: ["spare_parts",random.randint(3, 5)],
                                3: ["clothing", random.randint(5, 9)],
                                4: ["food", random.randint(50, 150)],
                                5: ["ammo" , random.randint(20, 60)]
                            }
                            your_trade = random.randint(1, 5)
                            their_trade = random.randint(1, 5)
                            yourrng = trade_options[your_trade][1]
                            theirrng = trade_options[their_trade][1]
                            while your_trade == their_trade:
                                their_trade = random.randint(1, 5)
                                theirrng = trade_options[their_trade][1]

                            selected_choice = None
                        elif selected_choice == 6:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'store'
                            selected_choice = None
                        elif selected_choice == 7:
                            running = False
                            selected_choice = None

                y_offset = 100
                for line in lines:
                    if str(selected_choice) == line[0]:
                        option_text = font.render(line, True, (255, 0, 0))
                        screen.blit(option_text, (width // 2 - 300 // 2, y_offset + 100))
                        y_offset += option_text.get_height() + 10
                    else:
                        option_text = font.render(line, True, (255, 255, 255))
                        screen.blit(option_text, (width // 2 - 300 // 2, y_offset + 100))
                        y_offset += option_text.get_height() + 10

            elif screen_helper['screen'] == 'display_supplies':
                screen.fill((0, 0, 0))

                # Draw "Your Supplies" title
                supplies_title = font1.render("Your Supplies", True, (255, 255, 255))
                screen.blit(supplies_title, (width // 2 - supplies_title.get_width() // 2, 50))
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            screen_helper['screen'] = prev_screen.pop()

                # Display supplies
                supplies_text = [
                    f"Oxen: {self.stats.oxen}",
                    f"Food: {self.stats.food} lbs",
                    f"Clothing: {self.stats.clothing} sets",
                    f"Ammunition: {self.stats.ammo} bullets",
                    f"Spare Parts: {self.stats.spare_parts}",
                    f"Money: {self.stats.money}"
                ]

                max_label_width = max(font.size(line.split(':')[0] + ': ')[0] for line in supplies_text)
                y_offset = (height - len(supplies_text) * (font.get_height() + 10)) // 2

                for line in supplies_text:
                    label, value = line.split(': ')
                    label_text = font.render(label + ': ', True, (255, 255, 255))
                    value_text = font.render(value, True, (255, 255, 255))

                    screen.blit(label_text, (500, y_offset))
                    screen.blit(value_text, (550 + max_label_width, y_offset))

                    y_offset += label_text.get_height() + 10

            elif screen_helper['screen'] == 'travel':
                screen.fill((0, 0, 0))
                prev_choice = 1

                # Display travel information
                if game_event is None:
                    selected_choice = None
                    self.stats.days_passed += 1
                    self.stats.day += 1
                    self.stats.party_health = max(self.stats.party_health - random.randint(1, 5), 0)
                    if random.randint(0, 10) <= 2:

                        game_event = events_occurred(self.stats)
                        message_text = [game_event,  "Press Space to continue"]

                    else:
                        message_text = ["You continue on the trail"]
                        game_event = None

                    if self.stats.distance_travelled + random.randint(10, 15) >= 1800:
                        self.stats.distance_travelled = 1800
                    else:
                        self.stats.distance_travelled += random.randint(10, 15)
                    if next_location != self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)]:
                        if self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)] == 0 or 302 or 552 or 638 or 1055 or 1169 or 1443 or 1568 or 1800:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'location'
                            next_location = self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)]
                        else:
                            game_event = f"You have reached {next_location}"
                            message_text = [game_event,  "Press Space to continue"]
                            next_location = self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)]
                else:
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game_event = None

                if self.stats.distance_travelled >= 1800:
                    unload_music()
                    screen_helper['screen'] = 'win'

                for line in message_text:

                    travel_info = font.render(line, True, (255, 255, 255))
                    screen.blit(travel_info, ((width - travel_info.get_width()) // 2, (i * 30) + 500 + travel_info.get_height()))
                    i += 1

                travel_text = [
                    f"Date: {self.stats.month_name} {self.stats.day}, {self.stats.year}",
                    f"Distance travelled: {self.stats.distance_travelled} miles",
                    f"Health: {self.stats.party_health}",
                    f"Wagon health: {self.stats.wagon_health}",
                    f"Money: {self.stats.money}",
                    f"Distance to next location: {min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)-self.stats.distance_travelled} miles",
                    f"Next Location: { self.total_distances[min((dist for dist in total_distances if dist >= self.stats.distance_travelled), default=None)]}"
                ]
                y_offset = 100
                for line in travel_text:
                    travel_info = font.render(line, True, (255, 255, 255))
                    screen.blit(travel_info, (width // 2 - 300 // 2, y_offset + 100))
                    y_offset += travel_info.get_height() + 10
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_event = False
                            if prev_screen:
                                screen_helper['screen'] = prev_screen.pop()
                pygame.display.flip()
                pygame.time.wait(1000)

            elif screen_helper['screen'] == 'location':
                screen.fill((0, 0, 0))
                screen.blit(location_images[locationindex], (0, 0))
                
                
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_event = False
                            if prev_screen:
                                print(prev_screen)
                                screen_helper['screen'] = prev_screen.pop()
                                locationindex += 1
                                

            elif screen_helper['screen'] == 'rest':
                screen.fill((0, 0, 0))
                if not rested:
                    user_input.show()
                    rest_prompt = font1.render("How many days do you want to rest?", True, (255, 255, 255))
                    screen.blit(rest_prompt, (width // 2 - rest_prompt.get_width() // 2, 100))
                else:
                    continue_prompt = font1.render("Press Enter to continue", True, (255, 255, 255))
                    screen.blit(continue_prompt, (width // 2 - continue_prompt.get_width() // 2, height - 100))
                    rest_prompt = font1.render("You have rested ", True, (255, 255, 255))
                    screen.blit(rest_prompt, (width // 2 - rest_prompt.get_width() // 2, 100))

                user_input.draw()
                user_input_text = user_input.getText()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and user_input_text.isdigit():
                            for i in range(int(user_input_text)):
                                screen.fill((0, 0, 0))
                                date_text = font.render(f"{self.stats.month_name} {self.stats.day}, {self.stats.year}",
                                                        True, (255, 255, 255))
                                screen.blit(date_text, (width // 2 - date_text.get_width() // 2, 200))
                                self.stats.days_passed += 1
                                self.stats.day += 1
                                self.stats.party_health = min(self.stats.party_health + 1, 100)
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                rested = True

                            user_input = TextBox(
                                screen,
                                width // 2 - 26, height - 175, 52, 50,
                                # Centered horizontally and positioned at the bottom
                                textColour=(247, 250, 248),
                                font=font1, margin=25, colour=(62, 66, 64), radius=5,
                            )
                            user_input.hide()
                            events.clear()

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and rested:
                            screen_helper['screen'] = prev_screen.pop()
                            rested = False

                # Display the date
                date_text = font.render(f"{self.stats.month_name} {self.stats.day}, {self.stats.year}", True,
                                        (255, 255, 255))
                screen.blit(date_text, (width // 2 - date_text.get_width() // 2, 200))

            elif screen_helper['screen'] == 'hunt':
                screen.fill((0, 0, 0))
                if hunt is None:
                    hunt_text = font1.render("You didn't find anything", True, (255, 255, 255))
                elif hunt == -1:
                    hunt_text = font1.render("You don't have enough ammo", True, (255, 255, 255))
                else:
                    hunt_text = font1.render(f"You found {hunt} lbs of food", True, (255, 255, 255))
                screen.blit(hunt_text, (width // 2 - hunt_text.get_width() // 2, 100))
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            screen_helper['screen'] = prev_screen.pop()

            elif screen_helper['screen'] == 'trade':

                screen.fill((0, 0, 0))
                trade_text = font1.render(f"Do you want to trade {yourrng} of your {trade_options[your_trade][0]} for {theirrng} of their {trade_options[their_trade][0]} Y/N", True, (255, 255, 255))
                screen.blit(trade_text, (width // 2 - trade_text.get_width() // 2, 100))

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            seen['y'] = event
                            if getattr(self.stats, trade_options[your_trade][0]) >= yourrng:
                                setattr(self.stats, trade_options[your_trade][0], getattr(self.stats, trade_options[your_trade][0]) - yourrng)
                                setattr(self.stats, trade_options[their_trade][0], getattr(self.stats, trade_options[their_trade][0]) + theirrng)
                                screen_helper['screen'] = prev_screen.pop()
                            else:
                                trade_text = font1.render("You don't have enough to trade", True, (255, 255, 255))
                                screen.blit(trade_text, (width // 2 - trade_text.get_width() // 2, 200))
                        elif event.key == pygame.K_n:
                            screen_helper['screen'] = prev_screen.pop()
                            seen = {}
                        if event.key == pygame.K_RETURN:
                            seen = {}
                            screen_helper['screen'] = prev_screen.pop()

                if 'y' in seen and not getattr(self.stats, trade_options[your_trade][0]) >= yourrng:
                    trade_text = font1.render("You don't have enough to trade", True, (255, 255, 255))
                    screen.blit(trade_text, (width // 2 - trade_text.get_width() // 2, 200))
            elif screen_helper['screen'] == 'gameover':
                screen.fill((0, 0, 0))
                gameover_text = font1.render("You have no oxen left. Game Over.", True, (255, 255, 255))
                screen.blit(gameover_text, (width // 2 - gameover_text.get_width() // 2, height // 2))
                pygame.display.flip()
            elif screen_helper['screen'] == 'win':
                screen.fill((0, 0, 0))
                gameover_text = font1.render("You Win", True, (255, 255, 255))
                screen.blit(gameover_text, (width // 2 - gameover_text.get_width() // 2, height // 2))
                if not pygame.mixer.music.get_busy():
                    load_music(music_win)
                    ever_music()
                pygame.display.flip()
            # Update the display
            pygame.display.flip()

            # Update widget events
            pygame_widgets.update(events)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    m = Main()
    m.start()
