class Solution:
    def reverseWords(self, s: str) -> str:
        salida = newW = ""
        words = 0
        for i in range(len(s)):
            if s[i].isspace() != True:
                newW += s[i]
            else:
                if len(newW) > 0:
                    if words == 0:
                        salida = newW + salida
                    else:
                        salida = newW + " " + salida
                    newW = ""
                    words = words + 1 
        salida = newW + " " + salida
        return salida.strip()
