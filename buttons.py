import pygame
import os
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox


# Create credit message
def create_credit_message(screen):
    return Button(
        screen,
        335, 580, 620, 40,
        text='Created by: David Tran, Josh Hunt, Lilly Jackson',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 25),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(62, 66, 64),
        radius=5,
    )


# Create the play button
def create_play_button(screen, on_click):
    return Button(
        screen,
        550, 380, 180, 60,
        text='Play',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 50),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(197, 200, 198),
        radius=5,
        onClick=on_click
    )


# Create the quit button
def create_quit_button(screen, on_click):
    return Button(
        screen,
        550, 480, 180, 60,
        text='Quit',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 50),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(197, 200, 198),
        radius=5,
        onClick=on_click
    )


# Create the back button
def create_back_button(screen, on_click):
    return Button(
        screen,
        500, 620, 150, 50,
        text='Back',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 40),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(197, 200, 198),
        radius=5,
        onClick=on_click
    )


def create_next_button(screen, on_click):
    return Button(
        screen,
        670, 620, 150, 50,
        text='Next',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 40),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(197, 200, 198),
        radius=5,
        onClick=on_click
    )


# Create character selection info
def create_selection_message(screen):
    return Button(
        screen,
        100, 100, 740, 50,
        text='What are the names of your companions?',
        textColour=(247, 250, 248),
        font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
        margin=50,
        inactiveColour=(62, 66, 64),
        inactiveBorderColour=(247, 250, 248),
        hoverColour=(62, 66, 64),
        radius=5,
    )


# Create character name input
def create_name_inputs(screen):
    input_boxes = [
        TextBox(
            screen,
            275, 225 + i * 80, 412, 50,
            textColour=(247, 250, 248),
            font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
            margin=50,
            colour=(62, 66, 64),
            radius=5,
        )
        for i in range(4)
    ]
    return input_boxes


# Create character name input number system
def create_name_num(screen):
    name_nums = [
        Button(
            screen,
            200, 225 + i * 80, 50, 50,
            text=f'{i+1}.',
            textColour=(247, 250, 248),
            font=pygame.font.Font(os.path.join(os.path.dirname(__file__), 'images', 'PixelifySans-VariableFont_wght.ttf'), 35),
            margin=50,
            inactiveColour=(62, 66, 64),
            inactiveBorderColour=(247, 250, 248),
            hoverColour=(62, 66, 64),
            radius=5,
        )
        for i in range(4)
    ]
    return name_nums
