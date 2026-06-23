class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        special_sep = "#"
        for st in strs:
            length = str(len(st))
            encode_st = length + special_sep + st
            result += encode_st
        return result
        

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            hash_idx = s.find('#', i)
            if hash_idx == -1:
                break
            
       
            length = int(s[i:hash_idx])
        
        
            i = hash_idx + 1
        

            end_idx = i + length
            segment = s[i:end_idx]
        

            result.append(segment)
        
            i = end_idx
        
        return result
            
                
            


            


        
