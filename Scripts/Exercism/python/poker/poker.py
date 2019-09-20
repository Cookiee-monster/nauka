from operator import itemgetter


FIGURES_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
    }

STRAIGHT_FLUSH = 1
FOUR_OF_KIND = 2
FULL_HOUSE = 3
FLUSH = 4
STRAIGHT = 5
THREE = 6
TWO_PAIRS = 7
PAIR = 8
HIGHEST_CARD = 9


def count_set_of_cards(set_of_cards, figures):
    count_cards = [figures.count(card) for card in set_of_cards]
    figures = sorted([(number, counter) for number, counter in zip(set_of_cards, count_cards)],
                     key=itemgetter(1, 0), reverse=True)

    return count_cards, figures


def ace_role(figures):
    if max(figures[1:]) == 5:
        figures[0] = 1
    return sorted(figures, reverse=True)


def best_hands(hands):

    if len(hands) == 1:
        return hands
    else:
        best_hand = [hands[0]]
        score_of_best_hand = score_the_seq(best_hand[0])
        for hand in hands[1:]:
            score_of_hand = score_the_seq(hand)

            if score_of_best_hand[0] == score_of_hand[0]:
                if score_of_hand[1] == score_of_best_hand[1]:
                    best_hand += [hand]
                else:
                    continue_search = True
                    for card_in_hand, card_in_best_hand in zip(score_of_hand[1], score_of_best_hand[1]):
                        if card_in_hand[0] > card_in_best_hand[0]:
                            if continue_search:
                                best_hand = [hand]
                                score_of_best_hand = score_the_seq(best_hand[0])
                                continue_search = False
                        elif card_in_hand[0] < card_in_best_hand[0]:
                            break
            elif score_of_hand[0] < score_of_best_hand[0]:
                    best_hand = [hand]

        return best_hand


def score_the_seq(hand):
    suite = [x[-1] for x in hand.split(" ")]
    figures = sorted([FIGURES_VALUE[x[:-1]] for x in hand.split(" ")], reverse=True)

    if figures.count(14) == 1:
        figures = ace_role(figures)

    set_of_cards = set(figures)
    count_cards, figures = count_set_of_cards(set_of_cards, figures)
    if len(set(suite)) == 1:
        if sum(set_of_cards)/5 == figures[2][0]:
            return STRAIGHT_FLUSH, figures
        else:
            return FLUSH, figures
    else:

        if len(set_of_cards) == 2:
            if sorted(count_cards, reverse=True) == [4, 1]:
                return FOUR_OF_KIND, figures
            else:
                return FULL_HOUSE, figures
        elif len(set_of_cards) == 3:
            if sorted(count_cards, reverse=True) == [3, 1, 1]:
                return THREE, figures
            else:
                return TWO_PAIRS, figures
        elif len(set_of_cards) == 4:
            return PAIR, figures
        else:
            if max(set_of_cards) - min(set_of_cards) == 4:
                return STRAIGHT, figures
            else:
                return HIGHEST_CARD, figures
