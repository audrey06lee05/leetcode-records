class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        # find max number in nums
        max_num = max(nums)

        # create a list as the model answer
        model = []

        for i in range(1,max_num+1):
            model.append(i)
        model.append(max_num)

        # compare model answer with nums
        if nums == model:
            return True
        else:
            return False