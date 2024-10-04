class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # create a list to store the sum of each element
        sum_list = []

        # use a for loop to go through each index of nums
        for i in range(len(nums)):
            # first element can be added to sum_list directly 
            if i == 0:
                sum_list.append(nums[i])
            # other elements:
            else:
                j = i
                target = 0 # use target to store each sum
                
                # use while loop to make sure j go backwards of each element for the summation until index 0 (inclusive)
                while j >= 0:
                    target += nums[j] # add each element to target
                    j -= 1 # go 1 index backwards
                sum_list.append(target) # add target to sum_list

        return sum_list
                    
