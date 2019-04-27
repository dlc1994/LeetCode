#leetcode 34 medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]: return [-1, -1]
        if len(nums)==1 and nums[0]==target: return [0, 0]
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                i = j = mid
                while i>0 and nums[i-1]==target: i-=1
                while j<len(nums)-1 and nums[j+1]==target: j+=1
                return [i, j]
            if nums[mid] > target: high = mid-1
            else: low = mid+1
        return [-1, -1]
            
        