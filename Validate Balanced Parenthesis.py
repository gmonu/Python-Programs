class Solution:
    def isValid(self, s):
        open_brac = ['(', '{', '[']
        close_brac = [')', '}', ']']
        
        stack = []
        
        for i in s:
            if i in open_brac:
                stack.append(i)
                
            elif i in close_brac:
                pos = close_brac.index(i)
                if ((len(stack) > 0) and (stack[len(stack) - 1] == open_brac[pos])):
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
            
# Driver Program.
s = "()(){(())"
print(Solution().isValid(s))
