class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = [None]*len(candies)
        may = candies[0]
        for i in range(len(candies)):
            if candies[i] > may:
                may = candies[i]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= may:
                x[i] = True
            else:
                x[i] = False
        return x
