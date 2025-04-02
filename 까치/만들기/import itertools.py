import itertools

suits = ['h', 's', 'd', 'c']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']
deck = [(f+s).upper() for f in faces for s in suits]

def find_outs(my_cards, table_cards):
    my_cards = my_cards.split()
    table_cards = table_cards.split()

    # remove my cards and table cards from the deck
    for card in my_cards + table_cards:
        card_name = card[:-1].lower()
        if card_name in faces:
            card_name = str(faces.index(card_name)+2)
        elif card_name == 'a':
            card_name = '1'
        card_suit = card[-1].lower()
        if card_name.upper()+card_suit in deck:
            deck.remove(card_name.upper()+card_suit)

    # calculate number of outs
    remaining_cards = list(itertools.combinations(deck, 2))
    total_possible_hands = len(remaining_cards) + len(table_cards)
    flush_outs = 9*4 - len([c for c in remaining_cards if 'h' not in c and 's' not in c])
    straight_outs = 0
    for i in range(0, 10):
        straight_outs += len([c for c in remaining_cards for j in range(0, 5) if str(i+j) in c[0]])

    straight_outs -= len(table_cards)
    four_of_a_kind_outs = 0
    three_of_a_kind_outs = 0
    pair_outs = 0
    for card in remaining_cards:
        if card[0] in faces:
            card_name = faces.index(card[0])+2
        elif card[0] == 'a':
            card_name = 1
        else:
            card_name = int(card[0])
        if len([c for c in remaining_cards if c[0] == card[0]]) == 3:
            three_of_a_kind_outs += 1
        if len([c for c in remaining_cards if c[0] == card[0]]) == 2:
            pair_outs += 1
        if len([c for c in remaining_cards if c[0] == card[0]]) == 1:
            four_of_a_kind_outs += 1
    pair_outs = pair_outs - three_of_a_kind_outs - 2*four_of_a_kind_outs
    total_outs = flush_outs + straight_outs + four_of_a_kind_outs + 2*three_of_a_kind_outs + pair_outs
    return round(total_outs/total_possible_hands*100, 2)

my_cards = input("나의 패를 입력하세요 (예: AS KD): ")
table_cards = input("테이블의 카드를 입력하세요 (예: QH 7D 3C): ")
print("확률은 " + str(find_outs(my_cards, table_cards)) + "% 입니다.")
