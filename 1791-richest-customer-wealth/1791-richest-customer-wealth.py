class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
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
         """   

        # set constraint for the while loop 
        i = 0 
        j = 0

        # create a list to store total money in each account:
        each_account = []

        counter = 0 # counter for storing money in each account

        # loop through accounts
        while i < len(accounts):
            
            # access elements of each account
            if j < len(accounts[i]):
                counter += accounts[i][j] # add money to counter
                j+=1 # next element
            else: 
                each_account.append(counter)
                i +=1 # move on to next account
                j = 0 # reset element to first element of next account
                counter = 0 # reset counter
        

        # find maximum in each_account
        max_account =  max(each_account)

        return max_account
        
