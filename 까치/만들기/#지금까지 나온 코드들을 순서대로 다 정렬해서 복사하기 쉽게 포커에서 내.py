from collections import Counter
from typing import List, Tuple
import random
import itertools
from itertools import combinations
import collections

RANKS = [str(n) for n in range(2, 11)] + list('JQKA')
SUITS = '♠ ♡ ♢ ♣'.split()

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]


def create_deck() -> List[Card]:
    return [Card(rank, suit) for rank in RANKS for suit in SUITS]


def check_pairs_trips_quads(cards: List[Card]) -> Counter:
    counter = Counter(card.rank for card in cards)
    return Counter({rank: count for rank, count in counter.items() if count >= 2})

def check_flush_draw(cards: List[Card]) -> bool:
    return any(cards.count(card) == 3 for card in cards)

def check_straight_draw(cards: List[Card]) -> bool:
    ranks = {card.rank for card in cards}
    if len(ranks) < 4:
        return False
    if 'A' in ranks:
        ranks.add('1')
    ranks = sorted((int(rank) if rank.isdigit() else 10 if rank == 'T' else 11 if rank == 'J' else 12 if rank == 'Q' else 13 if rank == 'K' else 14 for rank in ranks))
    for i in range(len(ranks) - 3):
        if ranks[i] + 1 == ranks[i + 1] and ranks[i + 1] + 1 == ranks[i + 2] and ranks[i + 2] + 1 == ranks[i + 3]:
            return True
    return False

def get_deck() -> List[Card]:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '♠ ♡ ♢ ♣'.split()
    return [Card(r, s) for s in suits for r in ranks]

def get_possible_hands(my_cards: List[Card], table_cards: List[Card]) -> List[List[Card]]:
    possible_hands = []
    for i in range(len(table_cards)):
        for j in range(i + 1, len(table_cards)):
            possible_hand = my_cards + [table_cards[i], table_cards[j]]
            possible_hands.append(possible_hand)
    return possible_hands

card_ranks = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

# 필요한 패 판별 함수
def get_hand_rank(cards):
    ranks = sorted([card_ranks[card.rank] for card in cards], reverse=True)
    if len(set(card.suit for card in cards)) == 1:
        if ranks == [14, 13, 12, 11, 10]:
            return (9, )  # Royal Flush
        if ranks[0] - ranks[-1] == 4:
            return (8, ranks[-1])  # Straight Flush
    counter = collections.Counter(ranks)
    for rank, count in counter.most_common():
        if count == 4:
            return (7, rank)  # Four of a Kind
        if count == 3:
            for rank2, count2 in counter.most_common():
                if count2 == 2:
                    return (6, rank, rank2)  # Full House
            return (3, rank)  # Three of a Kind
        if count == 2:
            for rank2, count2 in counter.most_common():
                if count2 == 2 and rank != rank2:
                    return (2, max(rank, rank2), min(rank, rank2), counter.most_common()[-1][0])  # Two Pair
            return (1, rank, counter.most_common()[-1][0], counter.most_common()[-2][0])  # One Pair
    if ranks == [14, 5, 4, 3, 2]:
        return (5, 5)  # Straight (A, 2, 3, 4, 5)
    if ranks[0] - ranks[-1] == 4:
        return (5, ranks[-1])  # Straight
    return (4, )  # High Card

# 나머지 카드를 계산하는 함수
def remove_cards(my_cards, table_cards, remove_list):
    all_cards = my_cards + table_cards
    for card in remove_list:
        all_cards.remove(card)
        if card in my_cards:
            my_cards.remove(card)
        elif card in table_cards:
            table_cards.remove(card)
    return all_cards

# 필요한 패 조합을 만드는 함수
def get_possible_hands(my_cards, table_cards):
    possible_hands = []
    for i in range(len(table_cards)):
        for j in range(i + 1, len(table_cards)):
            possible_hand = my_cards + [table_cards[i], table_cards[j]]
            possible_hands.append(possible_hand)
    for i in range(3, len(table_cards) + 1):
        for board in itertools.combinations(table_cards, i):
            possible_hand = my_cards + list(board)
            possible_hands.append(possible_hand)
    return possible_hands

def remove_cards(remaining_cards, cards_to_remove):
    return [card for card in remaining_cards if card not in cards_to_remove]

def get_probabilities(hand, board):
    possible_hands = combinations(hand + board, 5)
    counts = {rank: 0 for rank in RANKS}
    for possible_hand in possible_hands:
        rank = get_hand_rank(possible_hand)
        counts[rank] += 1
    probabilities = {rank: count/len(list(possible_hands)) for rank, count in counts.items()}
    return probabilities

def get_pair_rank(ranks):
    """Return the rank of the pair, or None if there is no pair."""
    for rank in ranks:
        if ranks.count(rank) == 2:
            return rank
    return None

def get_two_pair_ranks(ranks):
    """Return a tuple of the two pair ranks, or None if there is no two pair."""
    pair1_rank = get_pair_rank(ranks)
    if pair1_rank is not None:
        pair2_rank = get_pair_rank(list(reversed(ranks)))
        if pair2_rank is not None and pair2_rank != pair1_rank:
            return pair1_rank, pair2_rank
    return None

def get_three_of_a_kind_rank(ranks):
    """Return the rank of the three of a kind, or None if there is no three of a kind."""
    for rank in ranks:
        if ranks.count(rank) == 3:
            return rank
    return None

def get_straight_rank(ranks):
    """Return the rank of the highest card in the straight, or None if there is no straight."""
    for i in range(len(ranks) - 4):
        if ranks[i] - ranks[i+4] == 4:
            return ranks[i]
    return None

def get_flush_rank(suits, ranks):
    """Return the rank of the highest card in the flush, or None if there is no flush."""
    for suit in SUITS:
        if suits.count(suit) >= 5:
            flush_ranks = [rank for rank, suit in zip(ranks, suits) if suit == suit]
            flush_ranks.sort(reverse=True)
            return flush_ranks[0]
    return None

def get_full_house_ranks(ranks):
    """Return a tuple of the three of a kind rank and pair rank in the full house, or None if there is no full house."""
    three_of_a_kind_rank = get_three_of_a_kind_rank(ranks)
    if three_of_a_kind_rank is not None:
        remaining_ranks = [rank for rank in ranks if rank != three_of_a_kind_rank]
        pair_rank = get_pair_rank(remaining_ranks)
        if pair_rank is not None:
            return three_of_a_kind_rank, pair_rank
    return None

def get_four_of_a_kind_rank(ranks):
    """Return the rank of the four of a kind, or None if there is no four of a kind."""
    for rank in ranks:
        if ranks.count(rank) == 4:
            return rank
    return None

def get_straight_flush_rank(suits, ranks):
    """Return the rank of the highest card in the straight flush, or None if there is no straight flush."""
    for suit in SUITS:
        suit_ranks = [rank for rank, suit in zip(ranks, suits) if suit == suit]
        if len(suit_ranks) >= 5:
            straight_rank = get_straight_rank(suit_ranks)
            if straight_rank is not None:
                return straight_rank
    return None

def get_hand_rank(cards):
    """Return the rank of the hand, along with any additional data necessary to compare it to other hands."""
    suits = [card.suit for card in cards]
    ranks = sorted([card_ranks[card.rank] for card in cards], reverse=True)
    
    if len(set(card.suit for card in cards)) == 1:
        if ranks == [14, 13, 12, 11, 10]:
            return 9  # Royal flush
        elif all(ranks[i] - ranks[i+1] == 1 for i in range(4)):
            return 8  # Straight flush
        else:
            return 5  # Flush
    elif len(set(ranks)) == 2:
        if ranks.count(ranks[0]) in (1, 4):
            return 7  # Four of a kind
        else:
            return 6  # Full house
    elif len(set(ranks)) == 3:
        if ranks.count(ranks[0]) in (1, 3):
            return 4  # Three of a kind
        else:
            return 3  # Two pair
    elif len(set(ranks)) == 4:
        return 2  # One pair
    elif ranks == [14, 5, 4, 3, 2]:
        return 1  # A-5 straight
    elif all(ranks[i] - ranks[i+1] == 1 for i in range(4)):
        return 0  # Regular straight
    else:
        return -1  # High card


# 확률을 계산하는 함수
def find_outs(my_cards, table_cards):
    all_cards = my_cards + table_cards
    remaining_cards = list(set(card_ranks) - set([card.rank + card.suit for card in all_cards]))
    remaining_cards_counts = Counter([card[0] for card in remaining_cards])
    outs = 0
    hand_rank = get_hand_rank(all_cards)
    if hand_rank == 1: # High Card
        outs = remaining_cards_counts[my_cards[0].rank] + remaining_cards_counts[my_cards[1].rank]
    elif hand_rank == 2: # One Pair
        rank = get_pair_rank(all_cards)
        outs = remaining_cards_counts[rank]
    elif hand_rank == 3: # Two Pair
        ranks = get_two_pair_ranks(all_cards)
        for rank in ranks:
            outs += remaining_cards_counts[rank]
        outs += remaining_cards_counts.most_common()[-1][1] # kicker
    elif hand_rank == 4: # Three of a Kind
        rank = get_three_of_a_kind_rank(all_cards)
        outs = remaining_cards_counts[rank]
    elif hand_rank == 5: # Straight
        outs = 4
    elif hand_rank == 6: # Flush
        outs = len(remaining_cards) - len(set([card.suit for card in all_cards]))
    elif hand_rank == 7: # Full House
        rank = get_three_of_a_kind_rank(all_cards)
        outs = remaining_cards_counts[rank]
    elif hand_rank == 8: # Four of a Kind
        rank = get_four_of_a_kind_rank(all_cards)
        outs = remaining_cards_counts[rank]
    elif hand_rank == 9: # Straight Flush or Royal Flush
        outs = 0
    return round(100 * outs / len(remaining_cards), 2)

# 실행 부분
if __name__ == '__main__':
    # 카드 섞기
    random.shuffle(deck)

    # 카드 나눠주기
    my_cards = [Card('Q', '♠'), Card('4', '♠')]
    table_cards = [Card('K', '♢'), Card('K', '♣'), Card('4', '♡'), Card('3', '♠'), Card('3', '♣')]

    # 카드 출력
    print("나의 패: " + " ".join(map(str, my_cards)))
    print("공유 카드: " + " ".join(map(str, table_cards)))

    # 아웃 계산
    print("확률은 " + str(find_outs(my_cards, table_cards)) + "% 입니다.")
