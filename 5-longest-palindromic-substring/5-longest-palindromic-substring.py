class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 0. base case
        if len(s) == 1:
            return s
        # 1. define max_str, and set up the nested loop
        max_str = ""
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                # if the ith element == jth element, get the substring and see if its palindromic
                if s[i] == s[j]:
                    # get the substring
                    sub = s[i:j+1]
                    # only if the substring len is > max_str length we want to reverse
                    if len(sub) > len(max_str):
                        if sub == sub[::-1]:
                            max_str = sub
        # if there were no palindromes, return s[0]
        if len(max_str) == 0:
            return s[0]
        return max_str

 
