class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()
        # ans = money - (prices[0] + prices[1])
        # return ans if ans>=0 else money
        min1 = min2 = money
        for p in prices:
            if p < min1:
                if min2>min1:
                    min2 = min1
                min1 = p
            elif p>=min1 and p<min2:
                min2 = p
        ans = money-(min1+min2)
        return ans if ans>=0 else money
