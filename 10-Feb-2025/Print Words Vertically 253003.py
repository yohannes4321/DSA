# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = list(s.split())
        print(words)
        max_length_of_word = 0
        for word in words:
            max_length_of_word = max(len(word), max_length_of_word)


        print(max_length_of_word)
        for index in range(max_length_of_word):
            current_line = ""
            for word in words:
                if index >= len(word):
                    current_line +=" "
                elif index < len(word):

                    current_line += word[index]
            current_line=current_line.rstrip()
            print(current_line)

            res.append(current_line)
        return res
