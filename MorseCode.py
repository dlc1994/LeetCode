# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: MorseCode.py
@time: 2018/7/31 14:53
'''
words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
    #44ms
        table=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict_morse = {}
        count_diff = {}
        for i in range(26):
            dict_morse[chr(ord('a')+i)] = table[i]
        for word in words:
            temp = ""
            for letter in word:
                temp = temp + dict_morse[letter]
            if temp not in count_diff:
                count_diff[temp] = 0
            else:
                count_diff[temp] += 1
        return len(count_diff.keys())

        # morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # transformation = []
        # for word in words:
        #     temp = []
        #     for char in word:
        #         temp.append(morse[ord(char)-97])
        #     transformation.append(''.join(temp))
        # return len(set(transformation))

    #60ms
        # table=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # count_diff = {}
        # for word in words:
        #     temp = ""
        #     for letter in word:
        #         temp = temp + table[ord(letter)-ord("a")]
        #     if temp not in count_diff:
        #         count_diff[temp] = 0
        #     else:
        #         count_diff[temp] += 1
        # return len(count_diff.keys())

s = Solution
print(s.uniqueMorseRepresentations(s, words))