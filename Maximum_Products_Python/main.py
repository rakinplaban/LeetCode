class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        

if __name__ == '__main__':
    s = Solution()
    print(s.maxProductDifference([5,6,2,7,4]))
    print(s.maxProductDifference([4,2,5,9,7,4,8]))
    print(s.maxProductDifference([1,5,4,5]))
    print(s.maxProductDifference([1,2,4,5,6]))
    print(s.maxProductDifference([6,2,1,5,4]))
    print(s.maxProductDifference([6,2,1,5,4,3]))
    print(s.maxProductDifference([6,2,1,5,4,3,7]))
    print(s.maxProductDifference([6,2,1,5,4,3,7,8]))
    print(s.maxProductDifference([6,2,1,5,4,3,7,8,9]))
    print(s.maxProductDifference([6,2,1,5,4,3,7,8,9,10]))
    print(s.maxProductDifference([10,10,10,10]))