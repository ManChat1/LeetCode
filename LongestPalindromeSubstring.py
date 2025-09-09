class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s[::-1] == s:
            return s
        else:
            longest = ""
            for i in range(len(s)):
                # Checking for odd length palindromes:
                l_odd = i
                r_odd = i
                while l_odd > -1 and r_odd < len(s) and s[l_odd] == s[r_odd]:
                    l_odd -= 1
                    r_odd += 1
                potential = s[l_odd+1:r_odd]
                if len(potential) > len(longest):
                    longest = potential
                # Checking for even legnth palindromes:
                l_even = i
                r_even = i+1
                while l_even > -1 and r_even < len(s) and s[l_even] == s[r_even]:
                    l_even -= 1
                    r_even += 1
                potential = s[l_even+1:r_even]
                if len(potential) > len(longest):
                    longest = potential
        return longest