class Solution(object):


    def valid(self, list, start, end):
        while(start < end):
            if list[start] != list[end] :
                return False
            start +=1
            end -= 1
        return True;

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        left, right = 0, len(s_list) -1
        while(left < right):
            if list[left] != list[right]:
                if self.valid(list, left + 1, right):
                    return True
                if self.valid(list, left, right - 1):
                    return True
            else:
                left +=1
                right -= 1

        return True
