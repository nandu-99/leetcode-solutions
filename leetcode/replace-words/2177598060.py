class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        roots = set(dictionary)
        res = []
        for word in sentence.split(" "):
            repla = word 
            for i in range(1, len(word)+1):
                pre = word[:i]
                if pre in roots:
                    repla = pre 
                    break 
            res.append(repla)
        return " ".join(res)