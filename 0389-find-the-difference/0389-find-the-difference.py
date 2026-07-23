class Solution(object):
    def findTheDifference(self, s, t):

        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        for ch in s:
            count[ch] -= 1

        for ch in count:
            if count[ch] == 1:
                return ch