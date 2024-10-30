import pygame
import pygame_widgets
import os
from buttons import *
from stats import *
import random


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
        bg_title = pygame.image.load(os.path.join(os.path.dirname(__file__),'images', 'oregontrail.jpg')).convert()
        bg_char = pygame.image.load(os.path.join(os.path.dirname(__file__),'images', 'oregonchar.png')).convert()
        bg_char = pygame.transform.scale(bg_char, (1280, 720))
        bg_saloon = pygame.image.load(os.path.join(os.path.dirname(__file__),'images', 'pixelsaloon1.png')).convert()
        bg_saloon = pygame.transform.scale(bg_saloon, (500, 400))

        # Screen helper
        screen_helper = {'screen': 'game'}
        prev_screen = []

        # Track Variables
        selected_month = None  # Start with no month selected
        selected_item = None  # Start with no item selected
        selected_choice = None  # Start with no choice selected
        rested = False
        # Quit button helper
        def close_window():
            nonlocal running
            running = False

        # Play button helper
        def click_play():
            prev_screen.append( screen_helper['screen'])
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
            width // 2 - 26, height - 175, 52, 50,  # Centered horizontally and positioned at the bottom
            textColour=(247, 250, 248),
            font=pygame.font.Font(os.path.join(os.path.dirname(__file__),'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
            margin=25,
            colour=(62, 66, 64),
            radius=5,
            )

        # Create the font
        font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25)
        font1 = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35)

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
                    screen.blit(story, (25, 25 + y_offset)) # Align text to the left with an x-offset of 50
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
                    # Draw the inventory items
                    back_button.draw()
                    back_button.show()
                    inventory_items = [
                        f"1 Oxen: {self.stats.oxen} ",
                        f"2 Food: {self.stats.food} ",
                        f"3 Clothing: {self.stats.clothing} ",
                        f"4 Ammunition: {self.stats.ammo} ",
                        f"5 Spare Parts: {self.stats.spare_parts} "
                    ]

                    # Calculate the y-coordinate for the first item
                    y_offset = 175
                    # Draw the prompt for the store
                    prompt = font1.render("What would you like to buy?", True, (255, 255, 255))
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
                        
                        label_x = 500  # Align labels to the left
                        value_x = width - 550 - value_text.get_width()  # Align values to the right
                        
                        screen.blit(label_text, (label_x, y_offset + 50))
                        screen.blit(value_text, (value_x, y_offset + 50))
                        
                        y_offset += label_text.get_height() + 10  # Add some spacing between items
                        i += 1  # Increment the index


                        

                    # Get user input for each item

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_1] and selected_item == None:
                        selected_item = 0
                    elif keys[pygame.K_2] and selected_item == None:
                        selected_item = 1
                    elif keys[pygame.K_3] and selected_item == None:
                        selected_item = 2
                    elif keys[pygame.K_4] and selected_item == None:
                        selected_item = 3
                    elif keys[pygame.K_5] and selected_item == None:
                        selected_item = 4
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            selected_item = None

                            user_input = TextBox(
                            screen,
                            width // 2 - 26, height - 175, 52, 50,  # Centered horizontally and positioned at the bottom
                            textColour=(247, 250, 248),
                            font=pygame.font.Font(os.path.join(os.path.dirname(__file__),'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
                            margin=25,
                            colour=(62, 66, 64),
                            radius=5,
                            )
                    if len(user_input.getText()) == 2:
                        text = user_input.getText()[0:2]
                        user_input = TextBox(
                            screen,
                            width // 2 - 26, height - 175, 52, 50,  # Centered horizontally and positioned at the bottom
                            textColour=(247, 250, 248),
                            font=pygame.font.Font(os.path.join(os.path.dirname(__file__),'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
                            margin=25,
                            colour=(62, 66, 64),
                            radius=5,
                            )
                        user_input.setText(text)
                    input_prompt = font1.render("Enter quantity here:", True, (255, 255, 255))
                    screen.blit(input_prompt, (width // 2 - input_prompt.get_width() // 2, height - 225))
                    user_input.draw()
                    user_input_text = user_input.getText()
                    if user_input_text == "":
                        if selected_item == 0:
                            self.stats.oxen = 0
                        elif selected_item == 1:
                            self.stats.food = 0
                        elif selected_item == 2:
                            self.stats.clothing = 0
                        elif selected_item == 3:
                            self.stats.ammo = 0
                        elif selected_item == 4:
                            self.stats.spare_parts = 0
                    if user_input_text.isdigit():
                        if selected_item == 0:
                            self.stats.oxen = int(user_input_text)
                        elif selected_item == 1:
                            self.stats.food = int(user_input_text)
                        elif selected_item == 2:
                            self.stats.clothing = int(user_input_text)
                        elif selected_item == 3:
                            self.stats.ammo = int(user_input_text)
                        elif selected_item == 4:
                            self.stats.spare_parts = int(user_input_text)
                    if self.stats.oxen != 0 and self.stats.food != 0 and self.stats.clothing != 0 and self.stats.ammo != 0 and self.stats.spare_parts != 0:
                        next_button.show()
                        next_button.draw()

            elif screen_helper['screen'] == 'game':
                screen.fill((0, 0, 0))
                stats_text = font.render(f"{self.stats.month_name} {self.stats.day}, 1848", True, (255, 255, 255))
                screen.blit(stats_text, ((width - stats_text.get_width()) // 2, 25))

                lines = ["1. Continue on the trail", "2. Check supplies", "3. Stop to rest", "4. Hunt for food", "5. Attempt to trade", "6. Purchase supplies", "7. Quit"]

                # Display the options
                
                if pygame.key.get_pressed()[pygame.K_1]:
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
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'travel'
                            self.stats.days_passed += 1
                            self.stats.day += 1
                            self.stats.distance_travelled += random.randint(10, 15)
                            selected_choice = None
                        elif selected_choice == 2:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'display_supplies'
                            selected_choice = None
                        elif selected_choice == 3:
                            prev_screen.append(screen_helper['screen'])
                            screen_helper['screen'] = 'rest'
                            selected_choice = None
               
                    

                
                y_offset = 100
                for line in lines:
                    if str(selected_choice) == line[0]:
                        option_text = font.render(line, True, (255, 0, 0))
                        screen.blit(option_text, (width // 2 - 300 // 2, y_offset+100))
                        y_offset += option_text.get_height() + 10
                    else:
                        option_text = font.render(line, True, (255, 255, 255))
                        screen.blit(option_text, (width // 2 - 300 // 2, y_offset+100))
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
                    f"Ammunition: {self.stats.ammo} rounds",
                    f"Spare Parts: {self.stats.spare_parts}"
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
                # Draw the buttons
                
            
            elif screen_helper['screen'] == 'travel':
                screen.fill((0, 0, 0))
                # Display travel information
                
                travel_text = [
                    f"Date: {self.stats.month_name} {self.stats.day}, {self.stats.year}",
                    f"Distance travelled: {self.stats.distance_travelled} miles",
                    f"Health: {self.stats.party_health}",
                    f"Wagon health: {self.stats.wagon_health}"
                ]
                y_offset = 100
                for line in travel_text:
                    travel_info = font.render(line, True, (255, 255, 255))
                    screen.blit(travel_info, (width // 2 - 300 // 2, y_offset+100))
                    y_offset += travel_info.get_height() + 10
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            screen_helper['screen'] = prev_screen.pop()
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
                                date_text = font.render(f"{self.stats.month_name} {self.stats.day}, {self.stats.year}", True, (255, 255, 255))
                                screen.blit(date_text, (width // 2 - date_text.get_width() // 2, 200))
                                self.stats.days_passed += 1
                                self.stats.day += 1
                                self.stats.party_health = min(self.stats.party_health + 1, 100)
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                rested = True
                            
                                
                            user_input = TextBox(
                            screen,
                            width // 2 - 26, height - 175, 52, 50,  # Centered horizontally and positioned at the bottom
                            textColour=(247, 250, 248),
                            font=pygame.font.Font(os.path.join(os.path.dirname(__file__),'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
                            margin=25,
                            colour=(62, 66, 64),
                            radius=5,
                            )
                            user_input.hide()
                            events.clear()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and rested:
                            screen_helper['screen'] = prev_screen.pop()
                            rested = False

                
               
                    
                # Display the date
                date_text = font.render(f"{self.stats.month_name} {self.stats.day}, {self.stats.year}", True, (255, 255, 255))
                screen.blit(date_text, (width // 2 - date_text.get_width() // 2, 200))
                
            # Update the display
            pygame.display.flip()

            # Update widget events
            pygame_widgets.update(events)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    m = main()
    m.start()
