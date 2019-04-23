class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ""
        i = 0
        while num > 0:
            while i < len(nums) and num >= nums[i]:
                num = num - nums[i]
                res += syms[i]
            i += 1
        return res

s = Solution()
print(s.intToRoman(1994))