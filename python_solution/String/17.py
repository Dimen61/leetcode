class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        phone_map = {'1': '@',
               '2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'
               }
        res_lst = []

        def deep_first_search(depth, s):
            if depth >= length: 
                if s: res_lst.append(s)
                return

            for c in phone_map[digits[depth]]:
                deep_first_search(depth+1, s+c)

        deep_first_search(0, '')
        return res_lst

        
a = Solution()
print(a.letterCombinations('23'))
print(a.letterCombinations(''))
