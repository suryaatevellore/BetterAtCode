from typing import List
import random

class Solution:
    def create_index_array(self):
        self.index_arr[0] = self.w[0]
        for i in range(1, len(self.w)):
            self.index_arr[i] = (self.index_arr[i-1] + self.w[i])
        self.total_sum = self.index_arr[-1]
        print(f"total sum is {self.total_sum}")

    def find_binary_search(self, random_index, start, end):
        while(start < end):
            mid = start + end //2
            if self.index_arr[mid] < random_index:
                start = mid + 1
            elif self.index_arr[mid] > random_index:
                end = mid - 1
            elif self.index_arr[mid] == random_index:
                return mid
        return start

    def __init__(self, w: List[int]):
        self.w = w
        self.index_arr = [0]*len(self.w)
        self.total_sum = 0

    def pickElement(self) ->int:
        # pick a random element within w's indexes
        random_element = random.randint(0, self.total_sum)
        print(f"Random element is {random_element}")
        random_index = self.find_binary_search(random_element,0,len(self.index_arr))
        print(f"random index is {random_index}")
        return random_index

    def pickIndex(self) -> int:
        if not self.w:
            return 0
        self.create_index_array()
        return self.pickElement()
