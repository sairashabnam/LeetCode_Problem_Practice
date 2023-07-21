class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # Sort by end time

        end_time = intervals[0][1]
        removal_count = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < end_time:
                # Overlapping interval found, remove the one with the larger end time
                removal_count += 1
            else:
                # No overlap, update end_time
                end_time = end

        return removal_count


s = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(s.eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(s.eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(s.eraseOverlapIntervals(intervals))
