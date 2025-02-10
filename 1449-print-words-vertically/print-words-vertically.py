class Solution:
    def printVertically(self, s: str) -> List[str]:
        list_t=[]
        str_t=""
        value=list(s.split())
        max_value=0
        for i in value:
            max_value=max(max_value,len(i))

        for index in range (max_value):
            # use index as outer loop
            str_t=""
            for word in value:
                if index>=len(word):
                    str_t+=" "
                else:
                    str_t+=word[index]
            str_t=str_t.rstrip()
            list_t.append(str_t)
        return list_t
        

