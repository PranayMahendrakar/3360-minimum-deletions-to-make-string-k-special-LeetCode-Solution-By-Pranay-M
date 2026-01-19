class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        freq = Counter(word)
        counts = sorted(freq.values())
        n = len(counts)
        result = float('inf')
        for i in range(n):
            min_freq = counts[i]
            deletions = 0
            for j in range(i):
                deletions += counts[j]
            for j in range(i, n):
                if counts[j] > min_freq + k:
                    deletions += counts[j] - (min_freq + k)
            result = min(result, deletions)
        return result