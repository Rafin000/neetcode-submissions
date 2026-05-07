class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen.keys():
                seen[sorted_word].append(word)
            else:
                seen[sorted_word]=[word]
        
        for values in seen.values():
           result.append(values)
        
        return result