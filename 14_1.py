class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        i = 0 
        while True: 
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    print(sets)

                    result += sets.pop()
                    i+=1
                    print(result)
                else: 
                    break

            except Exception as e:
                break
        return result

a = Solution()
a.longestCommonPrefix(["flower","flow","flight"])
