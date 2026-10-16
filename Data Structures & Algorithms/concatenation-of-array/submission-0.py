class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # l=[]
        # for i in range(2*n):
        #     if i<=(n-1):
        #         l.append(nums[i])
        #     else:
        #         l.append(nums[i-n])
        # return l
        return [nums[i%n] for i in range(2*n)]