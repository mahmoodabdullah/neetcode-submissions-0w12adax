class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = "".join(sorted(s1))

        length = len(s1)

        for i in range(len(s2)):
            if "".join(sorted(s2[i:i+length])) == s1:
                return True
        return False

            
            

        