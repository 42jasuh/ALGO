class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the numbers we've seen so far and their indices
        num_to_index = {}
        
        # Iterate through the array
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the current number and the complement
                return [num_to_index[complement], index]
            
            # If not found, add the current number and its index to the dictionary
            num_to_index[num] = index        