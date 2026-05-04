class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum()).lower()
        reversed_text = clean_text[::-1]

        if clean_text == reversed_text:
            return True
        else:
            return False
        