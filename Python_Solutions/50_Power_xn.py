
class Solution:
    #Solution 1:
    # def myPow(self, x: float, n: int) -> float:
    #     return x ** n
    
    #Solution 2:
    # def myPow(self, x: float, n: int) -> float:
    #     # Base case: If n is 0, any number raised to the power 0 is 1.
    #     if n == 0:
    #         return 1

    #     # If n is negative, convert it to a positive power and take the reciprocal of the result.
    #     if n < 0:
    #         x = 1 / x
    #         n = -n

    #     result = 1
    #     while n > 0:
    #         # If n is odd, multiply the result by x.
    #         if n % 2 != 0:
    #             result *= x
    #         # Square x and reduce n by half.
    #         x *= x
    #         n //= 2

    #     return result

    #Solution 3:
    def myPow(self, x: float, n: int) -> float:
        # Base case: If n is 0, any number raised to the power 0 is 1.
        if n == 0:
            return 1

        # If n is negative, convert it to a positive power and take the reciprocal of the result.
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            # Check the rightmost bit of n (if it's 1)
            if n & 1:
                result *= x
            # Square x and divide n by 2 (right shift the bits)
            x *= x
            n >>= 1

        return result
    
s = Solution()

# Now, let's use the function to calculate some examples!
print(s.myPow(2, 3))  # Output: 8
print(s.myPow(3, 4))  # Output: 81
print(s.myPow(5, 0))  # Output: 1
print(s.myPow(2, -3)) # Output: 0.125