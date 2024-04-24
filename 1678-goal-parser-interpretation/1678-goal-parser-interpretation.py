class Solution:
    def interpret(self, command: str) -> str:
        list_t=[]
        for i in range(len(command)):
            if command[i]=="G":
                list_t.append('G')
            elif command[i]=='(' and i+1 <len(command) and command[i+1]==")":
                list_t.append('o')
            elif command[i]=='(' and i+1 <len(command) and command[i+3]==")":
                list_t.append('al')
        return ''.join(list_t)
            