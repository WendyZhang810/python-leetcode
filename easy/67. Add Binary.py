"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total=int(a)+int(b)
        str_total=str(total)
        m,result=0,''
        for i in range(len(str_total)):
            m=total%10
            total=int(total/10)
            if m>=2:
                total+=1
                m-=2
            result += str(m)
        if total==1: result+='1'
        return result[::-1]