'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"

'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result='1'
        i=1
        while i<n:
            i += 1
            element=''
            count=1
            res=''
            for index in result:
                if element=='':
                    element=index
                elif element==index:
                    count+=1
                else:
                    res+=str(count)+element
                    element = index
                    count=1

            res += str(count) + element

            result=res


        return result