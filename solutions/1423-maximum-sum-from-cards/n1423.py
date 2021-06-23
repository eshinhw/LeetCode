from typing import List

"""
Sliding Window Technique

Basic understanding of dynamic programming


"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k == 1:
            return max(cardPoints[0], cardPoints[-1])

        if len(cardPoints) == k:
            return sum(cardPoints)

        left_idx = 0
        right_idx = len(cardPoints) - k

        current_sum = sum(cardPoints[right_idx:])
        max_sum = current_sum

        while (right_idx<len(cardPoints)):

            current_sum = current_sum + cardPoints[left_idx] - cardPoints[right_idx]

            if current_sum > max_sum:
                max_sum = current_sum

            left_idx += 1
            right_idx += 1

        return max_sum



sol = Solution()

print(sol.maxScore([100,40,17,9,73,75], 3))
