from typing import List

class Solution:
    def find_eds(self, cut_nums):
        pass

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return 
        nums = sorted(nums)
        all_eds = {nums[0]: [nums[0]]}
        for index, num in enumerate(nums):
            print(f"Checking for num {num}")
            all_eds[num]=[]
            temp_eds=[[num]]
            for ele in nums[0:index]:
                print(f"Checking {ele} for {num}")
                if num % ele == 0:
                    temp_eds.append(all_eds[ele] + [num])
            print(f"Status of temp_eds for {num} is {temp_eds}")
            # breakpoint()
            all_eds[num] = max(temp_eds, key=len)
            print(f"all_eds for {num} is {all_eds[num]}")
        
        print(all_eds)
        # all_eds = {k:sorted(list(set(v))) for k, v in all_eds.items()}

        # print(max(list(all_eds.values()), key=len))
