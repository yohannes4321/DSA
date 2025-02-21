class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map={}
        for path in paths:
            path = path.split()
 
            for values in path[1:]:
                string = str(path[0])
                print(values)                
                key  = ""
                i = 0
                while i < len(values):
                    if values[i] == "(":
                        string+= "/" + values[:i]
                        i+=1
                        while i < len(values) and i != ")":
                            key+=values[i]
                            i+=1
                    i+=1
                if key not in map:
                    map[key] = [string]
                else:
                    map[key].append(string)
        liste = []
        for key,values in map.items():
            if len(values) > 1:
                liste.append(values)
        return liste

        