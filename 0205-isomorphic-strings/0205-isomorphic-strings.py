class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in mapping:
                if mapping[a] != b:
                    return False
            else:
                if b in used:
                    return False

                mapping[a] = b
                used.add(b)

        return True
        