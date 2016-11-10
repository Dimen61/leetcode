class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ip_addrs = []
        
        def is_valid_addr(s):
            """
            whether a valid part of ip address.
            
            :type s: str
            :rtype: bool
            """
            if len(s) > 1 and s[0] == '0': return False
            return 0 <= int(s) <= 255
            
        def dfs(num, s, ip_addr):
            """
            :type num: int
            :type s: str
            :type ip_addr: str
            :rtype void
            """
            if num >= 4 and not s:
                ip_addrs.append(ip_addr[1:]) # For "dfs(num+1, s[1:], ip_addr + '.' + s[0])" 
                return
            elif not s or num >= 4: return
        
            rest_num = 3 - num
            
            if rest_num*3 >= len(s)-1:
                dfs(num+1, s[1:], ip_addr+'.'+s[0])
            if len(s) >= 2 and is_valid_addr(s[:2]) and rest_num*3 >= len(s)-2:
                dfs(num+1, s[2:], ip_addr+'.'+s[:2])
            if len(s) >= 3 and is_valid_addr(s[:3]) and rest_num*3 >= len(s)-3:
                dfs(num+1, s[3:], ip_addr+'.'+s[:3])
        
        dfs(0, s, '')
        return ip_addrs


a = Solution()
print(a.restoreIpAddresses('25525511135'))
print(a.restoreIpAddresses("010010"))