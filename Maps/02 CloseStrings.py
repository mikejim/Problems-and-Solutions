class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        listValues1 = (sorted(Counter(word1).values()))
        listValues2 = (sorted(Counter(word2).values()))

        set1 = set(word1)
        set2 = set(word2)
        if set1 == set2:
            if len(word1) == len(word2):
                if listValues1 == listValues2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

