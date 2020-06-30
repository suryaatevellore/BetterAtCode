from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        # Create the count array
        for _, num in enumerate(nums):
            count[num]+=1

        pos = 0
        for index, item in enumerate(count):
            for _ in range(item):
                nums[pos] = index
                pos+=1

        print(nums)


