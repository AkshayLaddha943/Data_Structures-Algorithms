# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


def mergearray(interval):
    L = interval.sort()
    
    # for i in range(len(interval)):
    #     print(interval[i][1])
        
if __name__=="__main__":
    mergearray([[1,3],[2,6],[8,10],[15,18]])