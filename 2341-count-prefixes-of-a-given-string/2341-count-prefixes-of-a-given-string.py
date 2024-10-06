class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        output = 0 # count prefix 

        # create a model answer list to show the prefix 
        prefix_list = []
        # go through each letter in s
        for i in range(len(s)):
            # first element can be added to prefix_list directly:
            if i == 0:
                prefix_list.append(s[i])
            else:
                # create a target for adding letters in the prefix 
                target = s[i]
                prefix_list.append(prefix_list[i-1]+target) # combine target with previous index in prefix_list
        # print(prefix_list)
        
        # count the number of prefix in words list 
        # loop through each element in words list:
        for word in words:
            # try to find word in prefix_list:
            if word in prefix_list:
                output += 1
        
        return output 
                
