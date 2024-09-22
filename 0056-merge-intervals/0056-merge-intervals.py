class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last = merged[-1]
            current = intervals[i]

            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged