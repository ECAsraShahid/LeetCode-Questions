class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        var=s.split()
        return len(var[-1])
