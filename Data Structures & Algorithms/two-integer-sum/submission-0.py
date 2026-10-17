class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=len(nums)
        # for i in range(x):
        #     for j in range(i+1,x):
        #         if nums[i]+nums[j]== target:
        #             return [i,j]

        for i, v in enumerate(nums):
            for  j, w in enumerate(nums[i+1:]):
                if v+w==target:
                    return [i,j+i+1]


        