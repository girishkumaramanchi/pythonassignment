class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort(reverse=False)
        print(strs)
        l = len(strs)
        res = ""
        if l > 0:
            str1 = strs[0]
            str2 = strs[l - 1]
            print(str1, str2)
            n1 = len(str1)
            n2 = len(str2)
            i = j = 0
            while i <= n1 - 1 and j <= n2 - 1:
                print(i, j)
                if str1[i] == str2[j]:
                    res += str1[i]
                    i += 1
                    j += 1
                else:
                    break
        return res


strs = ["flower", "flow", "car"]
out = Solution().longestCommonPrefix(strs)
print(out)