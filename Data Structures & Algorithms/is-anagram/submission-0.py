class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=[i for i in s]
        tl=[i for i in t]

        sl.sort()
        tl.sort()

        return sl==tl