import pygame
import random
import time

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
    textures = []
    loaded_textures = set()
    # Load textures for all cards
    for i in range(1, 14):
        for j in range(1, 5):
            texture_file = "cards/" + str(i) + "c.png"
            if texture_file not in loaded_textures:
                texture = pygame.image.load(texture_file).convert_alpha() # Load texture for clubs
                textures.append(texture)
                loaded_textures.add(texture_file)

            texture_file = "cards/" + str(i) + "d.png"
            if texture_file not in loaded_textures:
                texture = pygame.image.load(texture_file).convert_alpha() # Load texture for diamonds
                textures.append(texture)
                loaded_textures.add(texture_file)

            texture_file = "cards/" + str(i) + "h.png"
            if texture_file not in loaded_textures:
                texture = pygame.image.load(texture_file).convert_alpha() # Load texture for hearts
                textures.append(texture)
                loaded_textures.add(texture_file)

            texture_file = "cards/" + str(i) + "s.png"
            if texture_file not in loaded_textures:
                texture = pygame.image.load(texture_file).convert_alpha() # Load texture for spades
                textures.append(texture)
                loaded_textures.add(texture_file)
    return textures
# Function to draw a card on the screen
def draw_card(screen, textures, card, pos):
    # Create a sprite for the card
    sprite = pygame.sprite.Sprite()
    sprite.image = textures[4 * (card.suit - 1) + (card.rank - 1)]
    sprite.rect = sprite.image.get_rect()

    # Set the position of the sprite on the screen
    sprite.rect.x, sprite.rect.y = pos

    # Scale the sprite
    sprite.image = pygame.transform.scale(sprite.image, (sprite.image.get_width() // 2, sprite.image.get_height() // 2))

    # Draw the sprite on the screen
    screen.blit(sprite.image, sprite.rect)

    # Remove the card texture from the list to prevent duplicate cards
    textures.pop(4 * (card.suit - 1) + (card.rank - 1))

# Initialize Pygame
pygame.init()

# Create a window of size 800x600
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Poker")

# Load card textures
card_textures = load_card_textures()

# Create a deck of cards
deck = []
for i in range(1, 14):
    for j in range(1, 5):
        card = Card(i, j)
        deck.append(card)

# Shuffle the deck
random.shuffle(deck)

# Deal cards to the players
player1_cards, player2_cards = [], []
for i in range(5):
    player1_cards.append(deck.pop())
    player2_cards.append(deck.pop())

# Bacck gouund color
screen.fill(PURPLE)

# Draw the cards on the screen
def Oponent_Cards():
    for i in range(5):
        draw_card(screen, card_textures, player1_cards[i], (200 + i * 100, 600))

def Our_Cards():
    for i in range(5):
        draw_card(screen, card_textures, player2_cards[i], (100 + i * 100, 100))

Our_Cards()

def Combination_recognition(cards):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def is_flush(cards):
        return len(set([card[1] for card in cards])) == 1
    
    def is_straight(cards):
        sorted_cards = sorted([values[card[0]] for card in cards])
        return sorted_cards == list(range(sorted_cards[0], sorted_cards[0] + 5))

    def is_same_value(cards, num):
        values_list = [card[0] for card in cards]
        for value in set(values_list):
            if values_list.count(value) == num:
                return True
        return False

    def get_hand_strength(cards):
        if is_flush(cards) and is_straight(cards):
            if cards[0][0] == 'T':
                return "Royal Flush"
            else:
                return "Straight Flush"
        elif is_same_value(cards, 4):
            return "Four of a Kind"
        elif is_same_value(cards, 3) and is_same_value(cards, 2):
            return "Full House"
        elif is_flush(cards):
            return "Flush"
        elif is_straight(cards):
            return "Straight"
        elif is_same_value(cards, 3):
            return "Three of a Kind"
        elif is_same_value(cards, 2) and is_same_value(cards, 2):
            return "Two Pair"
        elif is_same_value(cards, 2):
            return "One Pair"
        else:
            return "High Card"
        
    print(get_hand_strength(cards))  

# Create a font object
font = pygame.font.Font(None, 24)

# Create two a buttons rectangle

text1 = pygame.Rect(150, 25, 600, 45)
button_rect1 = pygame.Rect(50, 475, 600, 45)
button_rect2 = pygame.Rect(250, 540, 600, 45)

# Start the main loop of the program
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        # If the "close" button is pressed, exit the program
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is over the button
            if button_rect1.collidepoint(event.pos):

                print("Button clicked! You win")
            if button_rect2.collidepoint(event.pos):
                print("Button clicked! You lose")
    # Draw the button
    pygame.draw.rect(screen, GREEN, button_rect1)

    # Draw the text on the button
    text = font.render("If you thing that your combination will win than press this button", True, BLACK)
    text_rect = text.get_rect(center=button_rect1.center)
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, RED, button_rect2)

    text = font.render("If you thing that your combination will lose than press this button", True, WHITE)
    text_rect = text.get_rect(center=button_rect2.center)
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, BLUE, text1)

    text = font.render("This is your combination of cards. Yhat are youo gonna do?", True, WHITE)
    text_rect = text.get_rect(center=text1.center)
    screen.blit(text, text_rect)
    # Update the screen
    pygame.display.flip()


# Quit Pygame
pygame.quit()
