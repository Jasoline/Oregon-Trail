import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
width = 800
height = 600

# Create the window
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("My Pygame Window")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic (update game state, etc.)
    # ...

    # Drawing (render graphics, etc.)
    # ...

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()