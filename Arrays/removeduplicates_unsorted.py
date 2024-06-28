from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]):
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
        
        print(list(visited))
        
if __name__ == "__main__":
    Sol = Solution()
    Sol.removeDuplicates([1, 4, 6, 7, 4, 9, 1])