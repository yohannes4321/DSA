# class Solution:
#     def maskPII(self, s: str) -> str:
#         if list(s.split("@")):
#             val=list(s.split("@"))
#             word=val[0]
#             for i in range(len(word)):
#                 if i !=0 and i!=len(word)-1 :
#                     list_t.append(word[i])
#                 else:
#                     list_t.append("*")
#             list_t=list_t.append('@')
#             list_=list_t.append(val[1])
#         else:
#             s=lists.split("(")
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name,domain=s.split("@")
            name=name.lower()
            domain=domain.lower()
            name=name[0]+"*****"+name[-1]
            return name+"@"+domain  
        else:
            gg=""
            for x in s:
                if x.isdigit():
                    gg+=x
            l=len(gg)
            if l>10:
                return "+"+"*"*(l-10)+"-***-***-"+gg[-4:]
            return "***-***-"+gg[-4:]


                
