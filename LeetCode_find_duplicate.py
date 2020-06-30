from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(f"{i}, {j}")
                if nums[i]^nums[j] == 0:
                    return nums[i]
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         occurence_to_num_map = {}
#         for i in nums:
#            occurence_to_num_map[i] = occurence_to_num_map.get(i, 0) + 1

#         duplicate = [k for k,v in occurence_to_num_map.items() if v>1]
#         if not duplicate:
#           return 
#         else:
#           return duplicate[0]


if __name__ == "__main__":
    s = Solution()
    x = s.findDuplicate([1, 3, 4, 2, 2])
    print(x)
