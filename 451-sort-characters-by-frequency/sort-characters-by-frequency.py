from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        print(counter)
        sorted_el=sorted(counter.items(),key=lambda x:x[1],reverse=True)
        return "".join(value*freq  for value,freq in sorted_el)