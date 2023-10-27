class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        average = 0
        suma = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if s[i] in vowels:
                suma = suma + 1
            if i == k-1:
                sumMayor = suma
            else:
                if i >= k:
                    if s[i-k] in vowels:
                        suma = suma - 1
                    if suma > sumMayor:
                        sumMayor = suma
        return sumMayor  
