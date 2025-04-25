from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        output = []

        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                output.append(word)
        
        return output
