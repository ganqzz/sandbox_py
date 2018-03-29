class YatzyScoreSheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def _score_set(self, hand, set_size):
        scores = [0]  # identity
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * count)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

