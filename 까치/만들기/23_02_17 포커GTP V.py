from itertools import combinations
import numpy as np
import pandas as pd

# 테이블에 있는 카드와 내가 가진 카드를 리스트로 저장


# 카드 모양
suits = ['S', 'H', 'D', 'C']
# 카드 순위
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# 카드 덱 모델링
deck_suit = ['s', 'h', 'd', 'c']  # 스페이드, 하트, 다이아몬드, 클로버
deck_rank = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
deck_df = pd.DataFrame(index=pd.MultiIndex.from_product([deck_rank, deck_suit]))

# 내 패와 테이블의 카드 입력
my_hand = ['10D', 'JC']
table_cards = ['4S', '5D', 'KH']


# 카드 덱 생성
deck = [rank + suit for suit in suits for rank in ranks]


# 카드별 확률 계산
card_df = pd.DataFrame({'prob': 1 / len(deck)}, index=[''.join(card) for card in deck])

# 덱에서 내 패와 테이블의 카드 제거
my_df = card_df.loc[my_hand]
table_df = card_df.loc[table_cards]
deck_df = card_df.drop(my_hand + table_cards)

# 패를 계산하는 함수
def calculate_score(cards):
    pass  # 패 계산 함수 구현

# 상대방의 나머지 패의 확률 계산
opponent_hand = ['2D', '3D']
opponent_remain_cards = 5 - len(opponent_hand)
opponent_combinations = list(combinations(deck_df.index, opponent_remain_cards))
opponent_prob = 1 / len(opponent_combinations)
opponent_prob_df = pd.DataFrame({'name': opponent_combinations, 'prob': opponent_prob})
opponent_prob_df = opponent_prob_df.explode('name').reset_index(drop=True)
opponent_prob_df = opponent_prob_df.groupby('name').sum()

#my_hand1 = input('나의 패1= ')
#my_hand2 = input('나의 패2= ')

#table_cards1 = input('바닥패1= ')
#table_cards2 = input('바닥패2= ')
#table_cards3 = input('바닥패3= ')

# 내 패와 테이블의 카드 입력
#my_hand = [my_hand1, my_hand2]
#table_cards = [table_cards1, table_cards2, table_cards3]

my_hand = ['2D', '2D']
table_cards = ['3D', '6D', '7D']
# 덱에서 내 패와 테이블의 카드 제거
my_df = card_df.loc[my_hand]
table_df = card_df.loc[table_cards]
deck_df = card_df.drop(my_hand + table_cards)

# 가능한 모든 조합 계산
def get_combinations(df, num_cards):
    return list(combinations(df.index, num_cards))

my_remain_cards = 5 - len(my_hand) - len(table_cards)
my_combinations = get_combinations(deck_df, my_remain_cards)

# 모든 가능한 조합 계산
possible_combinations = []
for combination in my_combinations:
    possible_combinations.extend(list(combinations(combination, my_remain_cards)))

possible_df = pd.DataFrame({'name': possible_combinations})
possible_df = possible_df.explode('name').reset_index(drop=True)
possible_df = possible_df.groupby('name').size().reset_index(name='count')
possible_df = possible_df.set_index('name')

# 패 계산 함수 구현
def calculate_score(cards):
    score = 0
    card_ranks = [card[0] for card in cards]

    # 로얄 스트레이트 플러시
    if all(card[1] == cards[0][1] and card[0] in ['10', 'J', 'Q', 'K', 'A'] for card in cards):
        score = 10_000 + ranks.index(card_ranks[-1])

    # 스트레이트 플러시
    elif all(card[1] == cards[0][1] and card[0] in ranks[ranks.index(cards[0][0]):ranks.index(cards[0][0]) + 5] for card in cards):
        score = 9_000 + ranks.index(card_ranks[-1])

    # 포카드
    elif any(card_ranks.count(rank) == 4 for rank in ranks):
        rank = [rank for rank in ranks if card_ranks.count(rank) == 4][0]
        score = 8_000 + ranks.index(rank)

    # 풀하우스
    elif any(card_ranks.count(rank) == 3 for rank in ranks) and any(card_ranks.count(rank) == 2 for rank in ranks):
        score = 7_000 + ranks.index([rank for rank in ranks if card_ranks.count(rank) == 3][0])

    # 플러시
    elif any(card_ranks.count(rank) == 5 for rank in ranks):
        rank = [rank for rank in ranks if card_ranks.count(rank) == 5][0]
        score = 6_000 + ranks.index(rank)

    # 스트레이트
    elif all(card[0] in ranks[ranks.index(cards[0][0]):ranks.index(cards[0][0]) + 5] for card in cards):
        score = 5_000 + ranks.index(card_ranks[-1])

    # 트리플
    elif any(card_ranks.count(rank) == 3 for rank in ranks):
        rank = [rank for rank in ranks if card_ranks.count(rank) == 3][0]
        score = 4_000 + ranks.index(rank)

    # 투페어
    elif len(set(card_ranks)) == 3:
        pair_ranks = [rank for rank in ranks if card_ranks.count(rank) == 2]
        score = 3_000 + ranks.index(max(pair_ranks)) * 100 + ranks.index(min(pair_ranks))

    # 원페어
    elif len(set(card_ranks)) == 4:
        rank = [rank for rank in ranks if card_ranks.count(rank) == 2][0]
        score = 2_000 + ranks.index(rank)

   


# 카드 모델링
cards = [(n, s) for n in range(2, 15) for s in ['H', 'D', 'S', 'C']]
card_df = pd.DataFrame(cards, columns=['number', 'suit'])
card_df['number'] = card_df['number'].replace({11: 'J', 12: 'Q', 13: 'K', 14: 'A'})
card_df['name'] = card_df['number'].astype(str) + card_df['suit']
card_df = card_df.set_index('name')

opponent_hand1 = input('상대방의 패1= ')
opponent_hand2 = input('상대방의 패2= ')

# 상대방의 패 입력
opponent_hand = [opponent_hand1, opponent_hand2]

# 덱에서 상대방의 패 제거
opponent_df = card_df.loc[opponent_hand]
deck_df = card_df.drop(opponent_hand)


# 상대방의 나머지 패의 확률 계산
from itertools import combinations

opponent_remain_cards = 5 - len(opponent_hand)
opponent_combinations = list(combinations(deck_df.index, opponent_remain_cards))
opponent_prob = 1 / len(opponent_combinations)
opponent_prob_df = pd.DataFrame({'name': opponent_combinations, 'prob': opponent_prob})
opponent_prob_df = opponent_prob_df.explode('name').reset_index(drop=True)
opponent_prob_df = opponent_prob_df.groupby('name').sum()


# 가능한 모든 조합 계산
def get_combinations(df, num_cards):
    return list(combinations(df.index, num_cards))

my_remain_cards = 5 - len(my_hand) - len(table_cards)
my_combinations = get_combinations(deck_df, my_remain_cards)

# 모든 가능한 조합과 테이블의 카드 합치기
possible_df = pd.concat([table_df, deck_df])
possible_combinations = [list(combination) + list(possible_df.index) for combination in my_combinations]

# 가능한 모든 조합의 승률 계산
score_df = pd.DataFrame({'combination': possible_combinations})
score_df['score'] = score_df['combination'].apply(lambda x: calculate_score(x))

# 상대방이 가질 수 있는 각 패의 확률을 곱함
for card in opponent_prob_df.index:
    if card in possible_df.index:
        score_df['score'] *= opponent_prob_df.loc[card, 'prob']

# 모든 조합의 승률 합
my_prob = score_df['score'].sum()

# 최종 결과 출력
print(f"내 카드= {my_hand}")
print(f"테이블 카드= {table_cards}")
print(opponent_prob_df.sort_values('prob', ascending=False))
print(f"내가 이길 가능성= {my_prob * 100:.2f}%")
