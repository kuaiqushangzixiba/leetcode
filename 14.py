class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_l = len(strs[0])
        for word in strs:
            min_l = min(min_l, len(word))
            
        common = strs[0][:min_l]
        # print common
        
        
        for index, item in enumerate(strs):
            i = 0
            while(i < min_l and item[i] == common[i]):
                i += 1
                
            min_l = min(min_l, i)
            common = common[:min_l]
            
        return common


#methond2 
for i in range(len(strs[0])):
    for string in strs[1:]:
        if i > len(string) or strs[0][i] != string[i]:
            return strs[0][:i]


return ""


