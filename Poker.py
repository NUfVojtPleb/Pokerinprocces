import pygame
import random


# Set window dimensions
WIN_WIDTH, WIN_HEIGHT = 900, 1000

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (196, 30, 58)
PURPLE = (139,0,139)
BLUE = (0,0,255)

# Define the card class for representing the cards
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

# Load card textures from files
def load_card_textures():
    textures = {}
    # Load textures for all cards
    for i in range(1, 14):
        for j in range(1, 5):
            texture_file = f"cards/{i}{['c', 'd', 'h', 's'][j-1]}.png"
            if texture_file not in textures:
                texture = pygame.image.load(texture_file).convert_alpha()
                textures[texture_file] = texture
    return textures

def draw_card(screen, textures, card, pos):
    # Create a sprite for the card
    texture_file = f"cards/{card.rank}{['c', 'd', 'h', 's'][card.suit-1]}.png"
    sprite = pygame.sprite.Sprite()
    sprite.image = textures[texture_file]
    sprite.rect = sprite.image.get_rect()
    # Set the position of the sprite on the screen
    sprite.rect.x, sprite.rect.y = pos

    # Scale the sprite
    sprite.image = pygame.transform.scale(sprite.image, (sprite.image.get_width() // 2, sprite.image.get_height() // 2))

    # Draw the sprite on the screen
    screen.blit(sprite.image, sprite.rect)

# Initialize Pygame
pygame.init()

# Create a window of size 800x600
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Poker")

# Load card textures
card_textures = load_card_textures()

# Create a deck of cards
deck = [Card(rank, suit) for rank in range(1, 14) for suit in range(1, 5)]

# Shuffle the deck
random.shuffle(deck)

# Deal cards to the players
player1_cards = deck[:5]
player2_cards = deck[5:10]

# Bacck gouund color
screen.fill(PURPLE)

# Draw the cards on the screen
for i in range(5):
    draw_card(screen, card_textures, player1_cards[i], (200 + i * 100, 600))
    draw_card(screen, card_textures, player2_cards[i], (100 + i * 100, 100))

# Start the main loop of the program
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        # If the "close" button is pressed, exit the program
        if event.type == pygame.QUIT:
            running = False
  
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()