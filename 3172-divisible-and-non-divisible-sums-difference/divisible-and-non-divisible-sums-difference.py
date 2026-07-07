class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div=0
        non_div=0
        for i in range(1,n+1):
            if i%m==0:
                div+=i
            else:
                non_div+=i
        return non_div -div
        