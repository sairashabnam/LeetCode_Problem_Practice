from math import ceil

class Solution:
    # def can_reach_office(self, dist, hour, speed):
    #     total_time = sum([(d + speed - 1) // speed for d in dist[:-1]]) + dist[-1] / speed
    #     return total_time <= hour

    # def min_speed_to_reach_office(self, dist, hour):
    #     left = 1  # Minimum possible speed is 1 km/h
    #     right = 10**7  # Maximum possible speed is 10^7 km/h (as mentioned in the problem)

    #     while left < right:
    #         mid = (left + right) // 2

    #         if self.can_reach_office(dist, hour, mid):
    #             right = mid
    #         else:
    #             left = mid + 1

    #     return left if self.can_reach_office(dist, hour, left) else -1


    def min_speed_to_reach_office(self, dist: list[int], hour: float) -> int:
        if len(dist) >= hour + 1: 
            return -1
        left,right = 1, ceil(max(max(dist),dist[-1]/(1 if hour.is_integer() else hour-int(hour))))
        right_2 = ceil(max(max(dist),dist[-1]/(1 if hour.is_integer() else hour-int(hour))))
        print(right_2)

        while left<right:
            mid=(left+right)//2
            if sum([ceil(i/mid) for i in dist[:-1]])+(dist[-1]/mid) <= hour :
                right=mid
            else:
                left=mid+1
        return left



s = Solution()
# Test cases
print(s.min_speed_to_reach_office([1, 3, 2], 6.0))  # Example test case
# print(s.min_speed_to_reach_office([1, 3, 2], 2.7))
# print(s.min_speed_to_reach_office([1, 3, 2], 1.5))
