class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        a = 0
        newStr = str()  
        while (i < len(word1)) or (j < len(word2)):
            if i == len(word1):
                if j < len(word2):
                    newStr = newStr + word2[j]
                    a = a+1
                    j = j+1
            else:
                if j == len(word2):
                    if i < len(word1):
                        newStr = newStr + word1[i]
                        a = a+1
                        i = i+1
                else:
                    if a % 2 == 0:
                        if i < len(word1):
                            newStr = newStr + word1[i]
                            a = a+1
                            i = i+1
                    else:
                        if j < len(word2):
                            newStr = newStr + word2[j]
                            a = a+1
                            j = j+1

        return newStr       