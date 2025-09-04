class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack = []
        my_parentheses = {
            '(' : ')',
            '{' : '}', 
            '[' : ']'
        }
        for c in s:
            if c in ['(', '{', '[']:
                my_stack.append(c)

            if c in [')', '}', ']']:
                if len(my_stack) > 0:
                    p = my_stack.pop()

                    if my_parentheses[p] != c:
                        return False
                # if closed parentheses are added first
                else:
                    return False

        # check open parentheses in my_parentheses
        for paren in ['(', '{', '[']:
            if paren in my_stack:
                return False

        return True

                
            
            
        
