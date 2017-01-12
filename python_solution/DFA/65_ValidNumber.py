class Solution(object):
    def isNumber(self, s):
        """
        DFA

        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s: return False

        DFA = dict(A={}, B={}, C={}, D={}, E={}, F={}, G={}, H={})
        DFA['A'].update(zip(['+', '-'], ['G']*2))        
        DFA['A'].update(zip(list('0123456789'), ['B']*10))
        DFA['A'].update(zip(['.'], ['E']))
        DFA['B'].update(zip(list('0123456789'), ['B']*10))
        DFA['B'].update(zip(['.'], ['C']))
        DFA['B'].update(zip(['e'], ['D']))
        DFA['C'].update(zip(list('0123456789'), ['C']*10))
        DFA['C'].update(zip(['e'], ['D']))
        DFA['D'].update(zip(list('0123456789'), ['F']*10))
        DFA['D'].update(zip(['+', '-'], ['H']*2))
        DFA['E'].update(zip(list('0123456789'), ['C']*10))
        DFA['F'].update(zip(list('0123456789'), ['F']*10))
        DFA['G'].update(zip(list('0123456789'), ['B']*10))
        DFA['G'].update(zip(['.'], ['E']))
        DFA['H'].update(zip(list('0123456789'), ['F']*10))

        state = 'A'
        for c in s:
            state = DFA[state].get(c, None)
            if not state:
                return False
        return state not in ('E', 'D', 'H')