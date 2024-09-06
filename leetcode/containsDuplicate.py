# given an integer array nums, return true if any value appears 
# more than once in the array, otherwise return false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False