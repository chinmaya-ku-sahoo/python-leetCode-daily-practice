
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List

#My soluion : 76 ms
"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list = []
        list_len = len(nums)
        
        for index1 in range(list_len):
            for index2 in range(list_len):
                if index1 == index2:
                    continue
                value1 = nums[index1]
                value2 = nums[index2]
                if target == (value1 + value2):
                    result_list.extend([index1, index2])
                    return result_list
        return result_list"""

#Soulution from CHATGPT: 46 ms

"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], index]
            num_indices[num] = index
        
        # If no solution is found, you can return an empty list or handle it as needed.
        return []"""
        