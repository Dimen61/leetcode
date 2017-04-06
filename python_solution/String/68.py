# This problem is testing the implement ability.
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []
        res_lst = []

        for i in range(len(words)):
            line.append(words[i])
            if len(' '.join(line)) > maxWidth: # Construct a formatted line
                space_num = maxWidth - (total_length - len(words[i]))
                line.pop()
                if len(line) >= 2:
                    each_space_num = space_num / (len(line)-1)
                    left_space_num = space_num % (len(line)-1)
                    formatted_line = line[0]
                    for j in range(len(line)-1):
                        if left_space_num > 0:
                            left_space_num -= 1
                            formatted_line += ' ' * (each_space_num+1) + line[j+1]
                        else:
                            formatted_line += ' ' * each_space_num + line[j+1]
                else:
                    formatted_line = line[0] + ' ' * space_num
                    
                res_lst.append(formatted_line)
                line = [words[i]]
                
        # Construct the last formatted line
        space_num = maxWidth - total_length - (len(line)-1)
        formatted_line = ' '.join(line) + ' ' * space_num
        res_lst.append(formatted_line)
        return res_lst


# More concise solution          
class Solution2(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        add_words = []
        res_lst = []
        words_length = 0
        
        for word in words:
            if len(add_words) + len(word) + words_length > maxWidth:
                for i in range(maxWidth-words_length):
                    add_words[i % (len(add_words)-1 or 1)] += ' '
                res_lst.append(''.join(add_words))
                add_words = []
                words_length = 0
                
            add_words.append(word)
            words_length += len(word)
            
        res_lst.append(' '.join(add_words).ljust(maxWidth))
        return res_lst
            
a = Solution()
print(a.fullJustify(['What', 'must', 'be', 'shall', 'be.'], 12))
