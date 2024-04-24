class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) <2:
            return words
        uniq=set(words[0])
        list_t=[]
        for  letter in uniq:
            n=min(word.count(letter) for word in words)
            if n:
                list_t+=[letter]*n
        return list_t