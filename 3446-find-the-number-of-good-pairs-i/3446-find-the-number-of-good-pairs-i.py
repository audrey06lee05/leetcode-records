class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        count = 0 

        for num2 in nums2:
            target = num2*k
            for num1 in nums1:
                if num1%target == 0:
                    count += 1
        
        return count 
