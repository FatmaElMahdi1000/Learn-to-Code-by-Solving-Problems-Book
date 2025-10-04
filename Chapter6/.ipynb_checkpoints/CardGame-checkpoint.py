def playingCards(deckcards):
    player_A_scores = 0
    player_B_scores = 0
    player_A_turn = True  # ✅ True = A's turn, False = B's turn
    
    high_card_list = ["ace", "jack", "queen", "king"]
    
    for idx in range(len(deckcards)):
        current_card = deckcards[idx]
        
        if player_A_turn:  # ✅ Player A's turn
            if current_card == "ace":
                if idx + 4 < len(deckcards):
                    next_four_cards = deckcards[idx+1:idx+5]
                    if not any(card in high_card_list for card in next_four_cards):
                        player_A_scores += 4
                        
            elif current_card == "king":
                if idx + 3 < len(deckcards):
                    next_three_cards = deckcards[idx+1:idx+4]
                    for card in next_three_cards:
                        if not (card in high_card_list):
                            player_A_scores += 3
                            
            elif current_card == "queen":
                if idx + 2 < len(deckcards):
                    next_two_cards = deckcards[idx+1:idx+3]
                    for card in next_two_cards:
                        if not (card in high_card_list):
                            player_A_scores += 2
            
            elif current_card == "jack":
                if idx + 1 < len(deckcards):
                    next_one_card = deckcards[idx+1:idx+2]
                    for card in next_one_card:
                        if not (card in high_card_list):
                            player_A_scores += 1
        
        else:  # ✅ Player B's turn
            if current_card == "ace":
                if idx + 4 < len(deckcards):
                    next_four_cards = deckcards[idx+1:idx+5]
                    if not any(card in high_card_list for card in next_four_cards):
                        player_B_scores += 4
                        
            elif current_card == "king":
                if idx + 3 < len(deckcards):
                    next_three_cards = deckcards[idx+1:idx+4]
                    for card in next_three_cards:
                        if not (card in high_card_list):
                            player_B_scores += 3
                            
            elif current_card == "queen":
                if idx + 2 < len(deckcards):
                    next_two_cards = deckcards[idx+1:idx+3]
                    for card in next_two_cards:
                        if not (card in high_card_list):
                            player_B_scores += 2
            
            elif current_card == "jack":
                if idx + 1 < len(deckcards):
                    next_one_card = deckcards[idx+1:idx+2]
                    for card in next_one_card:
                        if not (card in high_card_list):
                            player_B_scores += 1
        
        # ✅ Switch turn after each card
        player_A_turn = not player_A_turn
    
    return player_A_scores, player_B_scores
            

def deckcards(numberofcards):
    cards_list = []
    reset = 0
    while len(cards_list) < numberofcards:
        next_card = input()
        if not next_card or next_card == "":
            reset += 1
        else:
            cards_list.append(next_card)
    return cards_list  
        
numberofcards = 52
print(deckcards(numberofcards))
print(playingCards(deckcards))