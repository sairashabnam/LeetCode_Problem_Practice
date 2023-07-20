class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # If the stack is empty or the current asteroid is moving right (positive)
            # or the top of the stack is moving left (negative), just push the asteroid
            #to the stack.
            if not stack or asteroid > 0 or (stack[-1] < 0 and asteroid > 0):
                stack.append(asteroid)
            else:
                # Asteroids are moving towards each other, handle collisions.
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    # The current asteroid destroys the one in the stack.
                    stack.pop()  
                # No asteroids to collide with or they are moving left.
                if not stack or stack[-1] < 0:  
                    stack.append(asteroid)
                # Both asteroids have the same size, destroy both
                elif stack[-1] == abs(asteroid):  
                    stack.pop()

        return stack
