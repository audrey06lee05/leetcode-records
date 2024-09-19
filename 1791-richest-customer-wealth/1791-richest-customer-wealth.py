class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # create a list to store total money in each account:
        each_account = []

        # loop through the bank accounts in the bank 
        for account in accounts:
            # create a counter for sum of money / reset counter
            count = 0

            # loop thourgh the money in each account 
            for money in account:

                # add money to count
                count += money
                
                # add count to each_account
                each_account.append(count)
        
        # find maximum in each_account
        max_account =  max(each_account)

        return max_account
            
