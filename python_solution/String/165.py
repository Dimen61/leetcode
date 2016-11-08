class Solution(object):
    def compareVersion(self, version1, version2):
        """
        Using direct acess table method instead of complex logic
        operations.

        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_lst = version1.split('.')
        v2_lst = version2.split('.')

        table = [-1, 1]
        while v1_lst and v2_lst:
            v1_value, v2_value = int(v1_lst[0]), int(v2_lst[0])
            if v1_value != v2_value:
                return table[v1_value > v2_value]
            v1_lst = v1_lst[1:]
            v2_lst = v2_lst[1:]

        if not v1_lst and not v2_lst:
            return 0
        elif sum(map(int, v1_lst+v2_lst)) == 0:
            return 0
        else:
            return table[not v2_lst]


a = Solution()
print(a.compareVersion('01', '1'))