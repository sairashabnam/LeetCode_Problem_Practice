class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        i = 0
        while i < length:
        # Check if the current plot (flowerbed[i]) is empty and its neighbors are also empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i==length-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1  # Plant a flower
                count += 1
            if count >= n:
                return True

            i += 1
        return False


s= Solution()
# Example usage:
flowerbed = [1, 0, 0, 0, 1]
n = 1
print(s.canPlaceFlowers(flowerbed, n))  # Output: True

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(s.canPlaceFlowers(flowerbed, n))  # Output: False