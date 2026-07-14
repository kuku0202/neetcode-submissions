class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:                        # real overlap (touching counts)
                res.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:   # whoever ENDS first is used up
                i += 1
            else:
                j += 1
        return res
    
