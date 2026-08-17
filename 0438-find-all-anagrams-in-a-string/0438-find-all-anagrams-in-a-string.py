class Solution:
    def findAnagrams(self, s, p):
        result = []
        p_count = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        window = {}
        left = 0
        right = 0
        while right < len(s):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if right - left + 1 > len(p):
                remove = s[left]
                window[remove] -= 1
                if window[remove] == 0:
                    del window[remove]
                left += 1
            if window == p_count:
                result.append(left)
            right += 1
        return result