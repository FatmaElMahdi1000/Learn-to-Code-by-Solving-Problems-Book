def playing_Cards(N, cards):
    Full_deck_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10','A', 'J', 'K', 'Q'] * 4
    cards_left_in_theDeck = Full_deck_cards.copy()
    for card in cards: 
        if card in cards_left_in_theDeck:
            cards_left_in_theDeck.remove(card)
    
    sum_of_left_deckCard = 0
    def card_value(card):
        if card == 'A':
            return 11
        elif card in ['J', 'K', 'Q']:
            return 10 
        else:
            return int(card)
    drawn_cards_sum = 0
    for card in cards:
        drawn_cards_sum = drawn_cards_sum + card_value(card)
    x = 21 - drawn_cards_sum
    
    safe_count = 0
    bust_count = 0
    
    for deckcard in cards_left_in_theDeck:
        value = card_value(deckcard)
        if value <= x:
            safe_count += 1
        else:
            bust_count += 1
        
    if bust_count > safe_count:
        return "vuci"
    else:
        return "dosta"

# FIXED PART: This function no longer prints error messages.
def drawn_card(N):
    Input = []
    for _ in range(N):
        Q = input()
        Input.append(Q)
    return Input
    
Deck_cards= 52
N= int(input()) #number of the drawn cards.

cards = drawn_card(N)            # ✅ store the returned list
print(playing_Cards(N, cards))   # ✅ pass the list, not the function