class Solution:
    def reverseVowels(self, s: str) -> str:
        newStr = vowelsFound =  ""
        for i in range(len(s)):
            if s[i] in "AaEeIiOoUu":
                vowelsFound += s[i]                
        j = len(vowelsFound)
        for i in range(len(s)):
            if s[i] in "AaEeIiOoUu":
                newStr += vowelsFound[j-1]                
                j = j-1
            else:
                newStr += s[i]
        return newStr     
 
