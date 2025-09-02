class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        str_x = str(x)
        for i in range(len(str_x)/2):
            if(str_x[i] != str_x[len(str_x)-i-1]):
                return False
        return True
