# Use recurssion
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        decoded_str = ''
        bracket_num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                repeat_num = 0
                while s[i].isdigit():
                    repeat_num = repeat_num * 10 + int(s[i])
                    i += 1
                tmp = ''
                bracket_num = 1
                i += 1

                while bracket_num > 0:
                    if s[i] == ']': bracket_num -= 1
                    elif s[i] == '[': bracket_num += 1

                    if bracket_num > 0: 
                        tmp += s[i]
                        i += 1

                decoded_str += self.decodeString(tmp) * repeat_num
            else:
                decoded_str += s[i]
            
            i += 1
            
        return decoded_str

# Use stack
class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(['', 1])

        num = ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                tmp_s, k = stack.pop()
                stack[-1][0] += tmp_s * k
            else:
                stack[-1][0] += c

        return stack[0][0]




        
        
if __name__ == '__main__':
    s = Solution()
    #                     01234567
    # print(s.decodeString("3[a2[c]]"))
    # print(s.decodeString("100[leetcode]"))
    print(s.decodeString("3[a]2[bc]"))

