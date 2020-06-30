from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 
        numbers = {}
        for i in nums:
            numbers[i] = numbers.get(i, 0) + 1

        single_number = [k for k, v in numbers.items() if v == 1]

        return single_number[0]


if __name__ == "__main__":
    nums = [0,1,0,1,0,1,99]
    print(Solution().singleNumber(nums))
