class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict = {"a":1,"b":2,...}
        start = -1 #起始位置
        #如果是空字符串的话, 返回值是1  ,  所以 start应该是-1开始
        max = 0 # 最大长度
        d = {} # 保存字母的字典
        # "abbcabcbb"
        for i in range(len(s)):
            #s[i] in d ..
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]]= i
                if i - start > max:
                    max= i - start
            print('i: ',i,end="  ")
            print('s[i]: ',s[i],end="  ")
            print("dsi: ",d[s[i]],end=" ")
            print('start: ',start,end="  ")
            print('max: ',max,end="  ")
            print('d: ',d,)

        return max

            # d = {"a":1,}        
            #s[i] not in d ..

a = Solution()
a.lengthOfLongestSubstring("abbcabcbb")

 