class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        chars = set()
        str_list = list(s)
        str_len = len(s)
        max_substr = 0
        while j < str_len:
            if str_list[j] in chars:
                chars.remove(str_list[i])
                i += 1
            else:
                chars.add(str_list[j])
                max_substr = max(max_substr, len(chars))
                j += 1

        return max_substr

