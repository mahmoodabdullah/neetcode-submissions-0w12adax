class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                counts = {}
                
                if len(s) != len(t):
                        return False

                for char in s:
                        if char in counts:
                                counts[char] += 1
                        else:
                                counts[char] = 1
                for char in t:
                        if char not in counts:
                                return False
                                
                        counts[char] -= 1

                        if counts[char] < 0:
                                return False
                return True



        