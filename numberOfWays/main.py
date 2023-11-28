# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat,plant = 0 , 0
        answer = 1
        for i in range(len(corridor)):
            if(corridor[i]=='S'):
                seat += 1
            if seat == 2 and i+1<len(corridor):
                count_P = 0
                while(i<len(corridor) and corridor[i]=='P'):
                    count_P +=1
                    i = i+1
                if(i==len(corridor)):
                    break
                answer = ((count_P+1) * seat) % (10**9+7)
                seat = 0
                i -= 1

        return answer



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out = Solution()
    print(out.numberOfWays('SSPPSPSSSPPPSS'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
