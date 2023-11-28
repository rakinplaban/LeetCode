# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        obj_num = Counter(corridor)
        if obj_num['S'] % 2 != 0 or obj_num['S']==0:
            return 0
        if obj_num['S']%2==0 and obj_num['P']==0:
            return int(obj_num['S']/2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out = Solution()
    print(out.numberOfWays('SSSS'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
