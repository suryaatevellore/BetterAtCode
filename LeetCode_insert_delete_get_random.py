class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_map = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index_map:
            print("Insert: Value already present in array")
            return False
        self.randomList.append(val)
        self.index_map[val] = len(self.randomList) - 1
        print(f"Insert : {self.randomList} {self.index_map}")
        return True
            
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index_map:
            print("Remove: Value not present")
            return False
        
        last_element, to_remove = -1, self.index_map.get(val)
        print(f"List pre swap : {self.randomList}")
        last_element, idx = self.randomList[-1], self.index_map[val]
        self.randomList[idx], self.index_map[last_element] = last_element, idx
        print(f"List post swap : {self.randomList}")
        self.randomList.pop()
        del self.index_map[val]
        print(f"Remove : {self.randomList} {self.index_map}")
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        # random_index = randint(0, self.index_counter-1)
        # print(f"Generated random index is {random_index}")
        random_element = choice(self.randomList)
        print(f"Random element is {random_element}")
        return random_element
