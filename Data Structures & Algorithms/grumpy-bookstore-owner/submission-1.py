class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0
        grumpy_list = []
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
            else:
                grumpy_list.append((customers[i], i))
        res = 0
        cur = 0
        left = 0
        for i in range(len(grumpy_list)):
            cur += grumpy_list[i][0]
            while grumpy_list[i][1] - grumpy_list[left][1] + 1 > minutes:
                    cur -= grumpy_list[left][0]
                    left += 1
            res = max(res, cur)
        print(base)
        print(res)
        return base + res