import pygame
import random


# Set window dimensions
WIN_WIDTH, WIN_HEIGHT = 900, 1000

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,150,0)
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

def compare_combinations(player1_cards, player2_cards):
    # Define the ranking of the hands
    rankings = {
        "royal flush": 10,
        "straight flush": 9,
        "four of a kind": 8,
        "full house": 7,
        "flush": 6,
        "straight": 5,
        "three of a kind": 4,
        "two pair": 3,
        "pair": 2,
        "high card": 1
    }
    
    # Define a function to check if a hand is a flush
    def is_flush(hand):
        suits = [card.suit for card in hand]
        return len(set(suits)) == 1        

    # Define a function to check if a hand is a straight
    def is_straight(hand):
        ranks = sorted([card.rank for card in hand])
        return ranks == list(range(ranks[0], ranks[0] + 5))

    # Define a function to count the number of cards with each rank
    def count_ranks(hand):
        ranks = [card.rank for card in hand]
        counts = {}
        for rank in ranks:
            if rank not in counts:
                counts[rank] = ranks.count(rank)
        return counts

    # Define a function to check if a hand has four of a kind
    def has_four_of_a_kind(hand):
        counts = count_ranks(hand)
        return 4 in counts.values()

    # Define a function to check if a hand has three of a kind
    def has_three_of_a_kind(hand):
        counts = count_ranks(hand)
        return 3 in counts.values()

    # Define a function to check if a hand has two pairs
    def has_two_pairs(hand):
        counts = count_ranks(hand)
        return list(counts.values()).count(2) == 2

    # Define a function to check if a hand has a pair
    def has_pair(hand):
        counts = count_ranks(hand)
        return 2 in counts.values()

    # Define a function to rank a hand
    def rank_hand(hand):
        if is_flush(hand) and is_straight(hand) and hand[-1].rank == 14:
            return "royal flush"
        elif is_flush(hand) and is_straight(hand):
            return "straight flush"
        elif has_four_of_a_kind(hand):
            return "four of a kind"
        elif has_three_of_a_kind(hand) and has_pair(hand):
            return "full house"
        elif is_flush(hand):
            return "flush"
        elif is_straight(hand):
            return "straight"
        elif has_three_of_a_kind(hand):
            return "three of a kind"
        elif has_two_pairs(hand):
            return "two pair"
        elif has_pair(hand):
            return "pair"
        else:
            return "high card"

    # Rank the hands of the players
    player1_rank = rank_hand(player1_cards)
    player2_rank = rank_hand(player2_cards)

    # Compare the ranks of the hands
    if rankings[player1_rank] > rankings[player2_rank]:
        return "Player 1 wins"
    elif rankings[player1_rank] < rankings[player2_rank]:
        return "Player 2 wins"
    else:
        # If the ranks are equal, compare the highest cards
        player1_high_card = max([card.rank for card in player1_cards])
        player2_high_card = max([card.rank for card in player2_cards])
        if player1_high_card > player2_high_card:
            return "Player 1 wins"
        if player1_high_card < player2_high_card:
            return "Player 2 wins"
        else: return "Tie"
       
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
screen.fill(GREEN)

# Draw the cards on the screen
for i in range(5):
    draw_card(screen, card_textures, player1_cards[i], (200 + i * 100, 600))
    draw_card(screen, card_textures, player2_cards[i], (100 + i * 100, 100))
    
print(compare_combinations(player1_cards,player2_cards))

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