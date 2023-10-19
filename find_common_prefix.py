# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class CommonPrefix:
    def __init__(self) -> None:
        pass

    # Approach-1
    """
    def find_common_prefix(self, item_list: list[str]) -> str:
        min_item = min(item_list, key=len)
        
        match_prefix = ""
        
        for index_val, i in enumerate(min_item):
            for j in item_list:
                if i!=j[index_val]:
                    return match_prefix
                
            match_prefix+=i
        return match_prefix        
    """
    
    # Approach-2
    """
    def find_common_prefix(self, item_list: list[str]) -> str:
        min_item = min(item_list, key=len)
        
        match_prefix = ""
        
        for i in range(len(min_item)):
            for j in item_list:
                if min_item[i]!=j[i]:
                    return match_prefix
                
            match_prefix+=min_item[i]
        return match_prefix  
    """

    # Approch-3 (reffered from kiran)
    def find_common_prefix(self, item_list: list[str]) -> str:
        min_item = min(item_list, key=len)
        
        match_prefix = ""
        
        for i in range(len(min_item)):
            if not all(min_item[i] ==j[i] for j in item_list):
                    return match_prefix
                
            match_prefix+=min_item[i]
        
        return match_prefix  
                    

obj1 = CommonPrefix()
result_val = obj1.find_common_prefix(('door','doocs','doaogg', 'door'))
print(result_val)
