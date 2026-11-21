class Solution:
    def interpret(self, command: str) -> str:
        i = 0 
        s = []
        n = len(command)
        while i<n:
            if command[i]=="G":
                s.append("G")
                i+=1 
            elif command[i]=="(" and command[i+1]==")":
                s.append("o")
                i+=2 
            elif command[i]=="(" and command[i+1]=="a":
                s.append("al")
                i+=4 
        return "".join(s)