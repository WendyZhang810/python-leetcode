'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        i=0
        j=len(s)-1
        while j>=i+1:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].capitalize()==s[j].capitalize():
                i+=1
                j-=1
            else:
                return False
        return True