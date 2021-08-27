class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [0]*len(strs)
        an = []
        sort_strings = []
        for i in strs :
            element = tuple(sorted(i))
            sort_strings.append(element)
       
        d = {}
        
        for i in range(len(strs)) :
            
            if sort_strings[i] in d : 
                d[sort_strings[i]].append(strs[i])
            else :
                d[sort_strings[i]] = [strs[i]]
        return d.values()
