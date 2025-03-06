import random
class RandomizedSet:
    
    def __init__(self):
        self.arr = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if not val in self.dic:
            self.arr.append(val)
            self.dic[val] = len(self.arr)-1
            return True
        
        return False


    def remove(self, val: int) -> bool:
        # bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        if not val in self.dic: return False
         # Get the index of the element to be removed
        index = self.dic[val]
        # Get the last element in the array
        last_element = self.arr[-1]
        # Replace the element to be removed with the last element
        self.arr[index] = last_element
        # Update the index of the last element in the hash map
        self.dic[last_element] = index
        # Remove the last element from the array and the element from the hash map
        self.arr.pop()
        del self.dic[val]
        return True


    def getRandom(self) -> int:
        #int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
        return random.choice(self.arr)
