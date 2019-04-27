#leetcode 29 medium

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend<0) is (divisor<0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend>=divisor:
            y = 1
            x = divisor
            while dividend>(x<<1):
                x <<= 1
                y <<= 1
            dividend -= x
            res += y
        # print(sign, dividend, divisor, res, y)
        if not sign: res = -res
        return min(max(-2147483648, res), 2147483647)
            
        