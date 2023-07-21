class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lengths = [1] * n  # Length of longest increasing subsequence ending at each index
        counts = [1] * n   # Count of longest increasing subsequences ending at each index

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        max_length = max(lengths)
        result = 0

        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]
        return result

s= Solution()                

# Example usage:
nums = [1, 3, 5, 4, 7]
# Output: 2 (Two longest increasing subsequences: [1, 3, 4, 7] and [1, 3, 5, 7])
print(s.findNumberOfLIS(nums))