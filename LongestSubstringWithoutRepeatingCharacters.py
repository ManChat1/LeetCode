class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        if s == "":
            return 0
        left = maxlen = 0
        chars = set()
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            if len(chars) > maxlen:
                maxlen = len(chars)
        return maxlen
