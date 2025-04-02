import itertools

# 카드 모양
suits = ['S', 'H', 'D', 'C']
# 카드 순위
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# 덱 만들기
deck = [(f+s).upper() for f in ranks for s in suits]

deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], ['H', 'D', 'C', 'S']))
my_cards = []
table_cards = []


# 카드 입력 받기
my_cards = input("나의 패를 입력하세요 (예: AS KD): ").upper().split()
table_cards = input("테이블의 카드를 입력하세요 (예: QH 7D 3C): ").upper().split()

total_possible_hands = comb(len(deck) - len(my_cards) - len(table_cards), 2)

# 카드 제거하기
for card in my_cards + table_cards:
    if card not in deck:
        print(f"{card}는 덱에 존재하지 않는 카드입니다. 다시 입력해주세요.")
    else:
        deck.remove(card)
        
print("남은 덱의 카드 수:", len(deck))

# my cards
for card in my_cards.split():
    card_name = card.upper()
    if card_name not in [c.upper() for c in deck]:
        print(f"{card} is not a valid card name")
    else:
        deck.remove(tuple(card.split()))

# table cards
for card in table_cards.split():
    card_name = card.upper()
    if card_name not in [c.upper() for c in deck]:
        print(f"{card} is not a valid card name")
    else:
        deck.remove(tuple(card.split()))


while len(my_cards) < 2:
    card = input("나의 패를 입력하세요 (예: AS KD): ")
    card_name = card.upper().split()
    if card_name in [c.upper() for c in my_cards]:
        print("이미 입력한 카드입니다. 다시 입력해주세요.")
    elif card_name in [c.upper() for c in table_cards]:
        print("이미 테이블에 있는 카드입니다. 다시 입력해주세요.")
    elif card_name not in [c.upper() for c in deck]:
        print("올바른 카드 이름을 입력해주세요.")
    else:
        my_cards.append(card)
        deck.remove(card_name)

while len(table_cards) < 5:
    card = input("테이블의 카드를 입력하세요 (예: QH 7D 3C): ")
    card_name = card.upper().split()
    if card_name in [c.upper() for c in my_cards]:
        print("이미 입력한 카드입니다. 다시 입력해주세요.")
    elif card_name in [c.upper() for c in table_cards]:
        print("이미 테이블에 있는 카드입니다. 다시 입력해주세요.")
    elif card_name not in [c.upper() for c in deck]:
        print("올바른 카드 이름을 입력해주세요.")
    else:
        table_cards.append(card)
        deck.remove(card_name)
        
        # 나머지 카드에서 남은 상대방 카드 조합 수를 계산합니다
opponent_wins = 0
total_combinations = itertools.combinations(deck, 2)
for opp_cards in total_combinations:
    all_cards = my_cards + table_cards + list(opp_cards)
    hand_strength = evaluate_hand(all_cards)
    if hand_strength < my_strength:
        opponent_wins += 1

# 상대방이 이길 확률을 계산합니다
opponent_win_prob = opponent_wins / total_possible_hands * 100
print(f"상대방이 이길 확률: {opponent_win_prob:.2f}%")

print(my_cards)
print(table_cards)
