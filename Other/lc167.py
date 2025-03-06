class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 10:
            for i in range(len(numbers)-1):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1,j+1]
        else:
            for i in range(len(numbers)-1):
                id = self.find(i+1,numbers,target - numbers[i]):
                if id != -1:
                    return [i+1,id+1]
    def find(self,start,arr,target):
        left = start
        right = len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid-1
            else:
                left = mid +1
        return -1