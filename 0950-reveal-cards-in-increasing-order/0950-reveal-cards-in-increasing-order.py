class Solution(object):
        def deckRevealedIncreasing(self, deck):
            d = []
            for x in sorted(deck)[::-1]:
                d = [x] + d[-1:] + d[:-1]
            return d
        