import numpy as np
import pandas as pd


# 카드 모양
suits = ['S', 'H', 'D', 'C']
# 카드 순위
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# 카드 덱 생성
deck = [rank + suit for suit in suits for rank in ranks]

# 카드 이름과 점수
card_names = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# 카드 모델링
cards = [(n, s) for n in range(2, 15) for s in ['H', 'D', 'S', 'C']]
card_df = pd.DataFrame(cards, columns=['number', 'suit'])
card_df['number'] = card_df['number'].replace({11: 'J', 12: 'Q', 13: 'K', 14: 'A'})
card_df['name'] = card_df['number'].astype(str) + card_df['suit']
card_df = card_df.set_index('name')

# 상대방의 패 입력
opponent_hand = ['7H', '8C']

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

#s1 = input('내카드1 = ')
#s2 = input('내카드2 = ')

#t1 = input('테이블카드1 = ')
#t2 = input('테이블카드2 = ')
#t3 = input('테이블카드3 = ')

# 내 패와 테이블의 카드 입력
my_hand = [ '2D', '4H' ]#39,40로 테이블카드을 입력하게 만듦
table_cards = [ '3S' , '5S', '7S' ]

# 덱에서 내 패와 테이블의 카드 제거
my_df = card_df.loc[my_hand]
table_df = card_df.loc[table_cards]
deck_df = card_df.drop(my_hand + table_cards)

# 'name' 열을 인덱스로 설정
card_df.set_index('name', inplace=True)

# 손패에 있는 카드 정보를 추출
my_df = card_df.loc[my_hand]


my_df = card_df.loc[my_hand, :]

card_df = pd.DataFrame({'value': card_values}, index=card_names)
card_df.reset_index(inplace=True)  # 인덱스를 열로 변경
card_df.rename(columns={'index': 'name'}, inplace=True)  # 열 이름 변경
card_df.set_index('name', inplace=True)  # 'name' 열을 인덱스로 지정


print(card_df)


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
print(f"My hand: {my_hand}")
print(f"Table cards: {table_cards}")
print(opponent_prob_df.sort_values('prob', ascending=False))
print(f"My winning probability: {my_prob * 100:.2f}%")
