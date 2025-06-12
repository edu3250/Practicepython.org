class Solution:
    def  list_that_ten (self,nums):
        less_that_10 = []
        for num in nums:
            if num < 5:
                less_that_10.append (num)
        return less_that_10
           

    
sol = Solution ()
print (sol.list_that_ten ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))





    




# Nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]# 