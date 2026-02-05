class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        maxL = max(len(w) for w in wordDict)

        @lru_cache(None)
        def dp(i):
            if i == n:  # Found a valid way to break words
                return True

            for j in range(i, min(i+maxL, n)):  # O(N * L)
                word = s[i:j+1]  # O(L)
                if word in wordSet and dp(j+1):
                    return True
            return False

        return dp(0)