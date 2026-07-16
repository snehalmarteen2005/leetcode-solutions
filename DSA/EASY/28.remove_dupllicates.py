class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0
        while x<len(nums)-1:
            if nums[x]==nums[x+1]:
                nums.pop(x+1)
            else:
                x=x+1
        print(len(nums))
