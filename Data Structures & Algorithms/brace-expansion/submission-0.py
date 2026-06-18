class Solution:
    def expand(self, s: str) -> List[str]:
        
        def store_option(startpos, option):
            if s[startpos] != '{':
                option.append(s[startpos])
            else:
                startpos += 1
                while s[startpos] != '}':
                    if s[startpos] != ',':
                        option.append(s[startpos])
                    startpos += 1
            return option, startpos + 1
        

        def find_word(startpos):
            if startpos == len(s):
                return [""]
            
            option = []
            option, nextpos = store_option(startpos, option)
            words = find_word(nextpos)

            res = []
            for c in option:
                for w in words:
                    res.append(c + w)
            
            return res
        
        return find_word(0)
