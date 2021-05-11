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

        sum_list = []

        left_idx = 0
        right_idx = len(cardPoints) - k

        left_sum = 0
        right_sum = sum(cardPoints[right_idx:])
        total_sum = left_sum + right_sum

        sum_list.append(total_sum)

        while (right_idx<len(cardPoints)):

            left_sum += cardPoints[left_idx]
            right_sum -= cardPoints[right_idx]
            total_sum = left_sum + right_sum
            sum_list.append(total_sum)
            left_idx += 1
            right_idx += 1

        return max(sum_list)


sol = Solution()

print(sol.maxScore([100,40,17,9,73,75], 3))
