#leetcode 33 medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0: return -1
        
        #find the smallest index
        low, high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid +1
            else: high = mid
        small = low
        low, high = 0, len(nums)-1
        if target <= nums[high]:
            low = small
        else:
            high = small-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target: high = mid-1
            else: low = mid+1
        return -1