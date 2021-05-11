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

        left_sum = 0
        right_sum = sum(cardPoints[k+1:])



        return total_sum


sol = Solution()

print(sol.maxScore([100,40,17,9,73,75], 3))