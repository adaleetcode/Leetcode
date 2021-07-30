class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        stack = []
        for i, n in enumerate(nums):
            nums_left = N - i
            while stack and stack[-1] > n and nums_left > k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack