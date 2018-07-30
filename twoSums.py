# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: twoSums.py
@time: 2018/7/30 10:24
'''
nums = [3, 2, 4]
target = 6


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     if nums.index(target-nums[i])
        #         for j in range(len(nums)):
        #             if (nums[i]+nums[j] == target) & (i != j):
        #                 return [i, j]

        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if (nums.index(target - nums[i])) != i:
                    return [i, nums.index(target - nums[i])]

        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in dict:
                return [dict[(target-nums[i])], i]
            else:
                dict[nums[i]]=i

        hash_table={}
        for i, value in enumerate (nums):
            if target-value in hash_table:
                return hash_table[target-value], i
            hash_table[value]=i



s = Solution
print(s.twoSum(s, nums, target))