class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Solution:
    # Constructor method (optional, used here for demonstration)
    def __init__(self, name):
        self.name = name  # 'self.name' is an instance variable storing the name of the instance

    # Method to find two indices such that the numbers at these indices add up to the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Initialize an empty dictionary to store numbers and their indices

        # Iterate over the list 'nums' with both index 'i' and value 'n'
        for i, n in enumerate(nums):
            diff = target - n  # Calculate the difference needed to reach the target
            
            # Check if the difference is already in the dictionary
            if diff in prevMap:
                # If it is, return the indices of the two numbers that add up to the target
                return [prevMap[diff], i]
            
            # Otherwise, store the current number 'n' and its index in the dictionary
            prevMap[n] = i

#~~~~ practicing typing it out

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int];
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i        

# given an array of integers nums and an integer target, return the indices 
# i and j such that nums[i] + nums[j] == target and i != j. 
# return the smallest index first.

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prevMap= {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        prevMap = {}
        for i, n enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
    prevMap = {}
    for i, n enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i