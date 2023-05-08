def Poker(budget):
    import pygame
    import random
    from time import sleep 
    
    while True:
        while True:
            try:
                deposite = int(input("Enter the amount you want to bet:\n"))
                budget = budget - deposite
                if deposite == 0:
                    print("you can't bet zero")
                else:
                    break
            except ValueError:
                print("*" * 40)
                print("Enter correct syntax int")  
        
        WIN_WIDTH, WIN_HEIGHT = 900, 1000
        
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0,150,0)
        RED = (196, 30, 58)
        BLUE = (0,0,255)
        ORANGE = (255,215,0)

        class Card:
            def __init__(self, rank, suit):
                self.rank = rank
                self.suit = suit

        def load_card_textures():
            textures = {}
            for i in range(1, 14):
                for j in range(1, 5):
                    texture_file = f"cards/{i}{['c', 'd', 'h', 's'][j-1]}.png"
                    if texture_file not in textures:
                        texture = pygame.image.load(texture_file).convert_alpha()
                        textures[texture_file] = texture
            return textures


        def first_card_texture():
            texture_file = f"back_cards/Zadni_strana.png"
            texture = pygame.image.load(texture_file).convert_alpha()
            scale_factor = 1.82
            texture = pygame.transform.scale(texture, (int(texture.get_width() * scale_factor), int(texture.get_height() * scale_factor)))
            return texture

        def first_card(screen, textures, pos):
            sprite = pygame.sprite.Sprite()
            sprite.image = textures
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = pos
            sprite.image = pygame.transform.scale(sprite.image, (sprite.image.get_width() // 2, sprite.image.get_height() // 2))

            screen.blit(sprite.image, sprite.rect)

        def draw_card(screen, textures, card, pos):
            texture_file = f"cards/{card.rank}{['c', 'd', 'h', 's'][card.suit-1]}.png"
            sprite = pygame.sprite.Sprite()
            sprite.image = textures[texture_file]
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = pos

            sprite.image = pygame.transform.scale(sprite.image, (sprite.image.get_width() // 2, sprite.image.get_height() // 2))

            screen.blit(sprite.image, sprite.rect)

        def compare_combinations_player(Computer, Player):
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
            
            def is_flush(hand):
                suits = [card.suit for card in hand]
                return len(set(suits)) == 1     
            
            def is_straight(hand):
                ranks = sorted([card.rank for card in hand])
                return ranks == list(range(ranks[0], ranks[0] + 5))

            def count_ranks(hand):
                ranks = [card.rank for card in hand]
                counts = {}
                for rank in ranks:
                    if rank not in counts:
                        counts[rank] = ranks.count(rank)
                return counts

            def has_four_of_a_kind(hand):
                counts = count_ranks(hand)
                return 4 in counts.values()
            
            def has_three_of_a_kind(hand):
                counts = count_ranks(hand)
                return 3 in counts.values()

            def has_two_pairs(hand):
                counts = count_ranks(hand)
                return list(counts.values()).count(2) == 2

            def has_pair(hand):
                counts = count_ranks(hand)
                return 2 in counts.values()

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

            player1_rank = rank_hand(Computer)
            player2_rank = rank_hand(Player)

            if rankings[player1_rank] > rankings[player2_rank]:
                return "Oponent win you lose your deposite!!!"
            elif rankings[player1_rank] < rankings[player2_rank]:
                return "You win!!! Your deposite was was doubled!"
            else:
                player1_high_card = max([card.rank for card in Computer])
                player2_high_card = max([card.rank for card in Player])
                if player1_high_card > player2_high_card:
                    return "Oponent win you lose your deposite!!!"
                if player1_high_card < player2_high_card:
                    return "You win!!! Your deposite was was doubled!"
                else: 
                    return "Tie!!! your deposit will remain as is."
        def compare_combinations_computer(Computer, Player):
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
            
            def is_flush(hand):
                suits = [card.suit for card in hand]
                return len(set(suits)) == 1        

            def is_straight(hand):
                ranks = sorted([card.rank for card in hand])
                return ranks == list(range(ranks[0], ranks[0] + 5))

            def count_ranks(hand):
                ranks = [card.rank for card in hand]
                counts = {}
                for rank in ranks:
                    if rank not in counts:
                        counts[rank] = ranks.count(rank)
                return counts

            
            def has_four_of_a_kind(hand):
                counts = count_ranks(hand)
                return 4 in counts.values()

            
            def has_three_of_a_kind(hand):
                counts = count_ranks(hand)
                return 3 in counts.values()


            def has_two_pairs(hand):
                counts = count_ranks(hand)
                return list(counts.values()).count(2) == 2

            def has_pair(hand):
                counts = count_ranks(hand)
                return 2 in counts.values()
            
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

            player1_rank = rank_hand(Computer)
            player2_rank = rank_hand(Player)

            if rankings[player1_rank] > rankings[player2_rank]:
                return "Oponent win your deposite was doubled!!!"
            elif rankings[player1_rank] < rankings[player2_rank]:
                return "You win!!! You lost your deposite!"
            else:
                
                player1_high_card = max([card.rank for card in Computer])
                player2_high_card = max([card.rank for card in Player])
                if player1_high_card > player2_high_card:
                    return "Oponent win your deposite was doubled!!!"
                if player1_high_card < player2_high_card:
                    return "You win!!! You lost your deposite!"
                else: 
                    return "Tie!!! your deposit will remain as is."
            
        pygame.init()

        screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        pygame.display.set_caption("Poker")

        card_textures = load_card_textures()
        first_card_textures = first_card_texture()

        deck = [Card(rank, suit) for rank in range(1, 14) for suit in range(1, 5)]

        random.shuffle(deck)

        Computer = deck[:5]
        Player = deck[5:10]

        screen.fill(GREEN)
        for i in range(5):
            draw_card(screen, card_textures, Player[i], (100 + i * 100, 45))

        for i in range(5):   
            first_card(screen,first_card_textures, (200 + i * 100, 530))
            
        font = pygame.font.Font(None, 24)

        text1 = pygame.Rect(150, 5, 600, 30)
        button_rect1 = pygame.Rect(50, 430, 600, 30)
        button_rect2 = pygame.Rect(250, 480, 600, 30)
        text2 = pygame.Rect(5, 900, 600, 80)
        button_rect3 =  pygame.Rect(650, 900, 200, 30)
        text3 = pygame.Rect(650, 925, 200, 30)
        button_rect4 = pygame.Rect(650, 950, 200, 30)
        running = True
        while running:
            for event in pygame.event.get():
                pygame.draw.rect(screen, BLUE, button_rect1)
                text = font.render("If you thing that your combination will win than press this button", True, WHITE)
                text_rect = text.get_rect(center=button_rect1.center)
                screen.blit(text, text_rect)

                pygame.draw.rect(screen, RED, button_rect2)

                text = font.render("If you thing that your combination will lose than press this button", True, WHITE)
                text_rect = text.get_rect(center=button_rect2.center)
                screen.blit(text, text_rect)

                pygame.draw.rect(screen, ORANGE, text1)

                text = font.render("This is your combination of cards. Yhat are youo gonna do?", True, BLACK)
                text_rect = text.get_rect(center=text1.center)
                screen.blit(text, text_rect)
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect1.collidepoint(event.pos):
                        for i in range(5):
                            draw_card(screen, card_textures, Computer[i], (200 + i * 100, 530))
                        sleep(1)
                        x = compare_combinations_player(Computer,Player)
                        pygame.draw.rect(screen, ORANGE, text2)
                        text = font.render(f"{x} Do you want to paly again?", True, BLACK)
                        text_rect = text.get_rect(center=text2.center)
                        screen.blit(text, text_rect)
                        if x == "You win!!! Your deposite was was doubled!":
                            deposite = deposite * 2
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")
                        if x == "Oponent win you lose your deposite!!!":
                            deposite = 0
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")
                        if x == "Tie!!! your deposit will remain as is.":
                            deposite = deposite
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")

                        pygame.draw.rect(screen, BLUE, button_rect3)
                        text = font.render(f"YES", True, WHITE)
                        text_rect = text.get_rect(center=button_rect3.center)
                        screen.blit(text, text_rect)

                        pygame.draw.rect(screen, GREEN, text3)
                        text = font.render(f"Or", True, BLACK)
                        text_rect = text.get_rect(center=text3.center)
                        screen.blit(text, text_rect)

                        pygame.draw.rect(screen, RED, button_rect4)
                        text = font.render(f"NO", True, WHITE)
                        text_rect = text.get_rect(center=button_rect4.center)
                        screen.blit(text, text_rect)
                    if button_rect2.collidepoint(event.pos):
                        for i in range(5):
                            draw_card(screen, card_textures, Computer[i], (200 + i * 100, 530))
                        sleep(1)
                        x = compare_combinations_computer(Computer,Player)
                        pygame.draw.rect(screen, ORANGE, text2)
                        text = font.render(f"{x} Do you want to paly again?", True, BLACK)
                        text_rect = text.get_rect(center=text2.center)
                        screen.blit(text, text_rect)
                        if x == "Oponent win your deposite was doubled!!!":
                            deposite = deposite * 2
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")
                        if x == "You win!!! You lost your deposite!":
                            deposite = 0
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")
                        if x == "Tie!!! your deposit will remain as is.":
                            deposite = deposite
                            budget = budget + deposite
                            print(f"Your total budget is {budget}")
                        pygame.draw.rect(screen, BLUE, button_rect3)

                        text = font.render(f"YES", True, WHITE)
                        text_rect = text.get_rect(center=button_rect3.center)
                        screen.blit(text, text_rect)

                        pygame.draw.rect(screen, GREEN, text3)
                        text = font.render(f"Or", True, BLACK)
                        text_rect = text.get_rect(center=text3.center)
                        screen.blit(text, text_rect)
                        pygame.draw.rect(screen, RED, button_rect4)

                        pygame.draw.rect(screen, RED, button_rect4)
                        text = font.render(f"NO", True, WHITE)
                        text_rect = text.get_rect(center=button_rect4.center)
                        screen.blit(text, text_rect)
                    if button_rect3.collidepoint(event.pos):
                        running = False
                        break
                    if button_rect4.collidepoint(event.pos):
                        print("")
                        exit()
            pygame.display.flip() 

        pygame.quit()
Poker(1000)