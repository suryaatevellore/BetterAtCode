from typing import List
from itertools import permutations

class Solution:
    def find_factorial(self, n):
        if n == 1:
            return n 
        return n * self.find_factorial(n-1)

    def char_at_pos(self, all_first_indices, n, k):
        if n == 1:
            return str(all_first_indices[k])
        if k==0:
            k = 1
        total_number_of_permutations = self.find_factorial(n)
        number_per_first_index = total_number_of_permutations // n
        pos_of_first_index = (k) // number_per_first_index
        offset_into_first_index = (k) % number_per_first_index
        first_index = all_first_indices[pos_of_first_index]
        # all_first_indices[0], all_first_indices[pos_of_first_index] = all_first_indices[pos_of_first_index], all_first_indices[0]
        remaining_indices = [i for i in all_first_indices if i!=first_index]
        print(remaining_indices)
        return str(first_index) + self.char_at_pos(remaining_indices, n-1, offset_into_first_index)

    def getPermutation(self, n: int, k: int) -> str:
        all_first_indices = [i for i in range(1, n+1)]
        
        print(self.char_at_pos(all_first_indices, n, k))

if __name__ == "__main__":
    s = Solution()
     
    s.getPermutation(4, 9)
    s.getPermutation(3,3)
    s.getPermutation(2, 1)
