class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    
        # go through each element until the third last element (inclusive)

        for i in range(0,len(arr)-2):
            a = i + 1 #index after i
            b = a + 1 # index after a
        
            # check if they are odds
            if (arr[i]%2 != 0) and (arr[a]%2!=0) and (arr[b]%2!=0):
                return True
        
                