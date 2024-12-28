class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels=0
        hash_set=set()
        hash_set={'a','e','i','o','u'}
        max_value=0
   
        for i  in range(k):
            if s[i] in hash_set:
                max_vowels+=1
                print("max_vowels",max_vowels)
        #when you work on the first case separtely you must count it 
        max_value=max(max_value,max_vowels)
        left=0
        for i in range(k,len(s)):
            if s[i] in hash_set:
                max_vowels+=1
            # for deacrseasing 
            if s[left] in hash_set:
                max_vowels -=1
            left +=1
            max_value=max(max_value,max_vowels)
       
        return max_value
            
        