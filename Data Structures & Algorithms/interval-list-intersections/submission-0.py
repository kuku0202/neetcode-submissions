class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            first, second = firstList[i], secondList[j]
            # res.append(first, second)
            overlap = []
            if first[0] < second[0]:
                if first[1] < second[0]:
                    i += 1
                    continue
                else:
                    if first[1] < second[1]:
                        overlap = [second[0], first[1]]
                        i += 1
                    else:
                        overlap = [second[0], second[1]]
                        j += 1
            else:
                if first[0] > second[1]:
                    j += 1
                    continue
                else:
                    if first[1] < second[1]:
                        overlap = [first[0], first[1]]
                        i += 1
                    else:
                        overlap = [first[0], second[1]]
                        j += 1
            res.append(overlap)
        return res
    
