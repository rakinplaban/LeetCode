from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        pct_25 = (len(arr)*25)//100
        new_dict = Counter(arr)
        res = 0
        for i in new_dict:
            if new_dict[i] > pct_25:
                res = i
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.findSpecialInteger([5668,5668,5668,5668,22011]))