'''
Date - 29/05/2018
@author - Purvak 
Timestamp - 20:44

'''


'''
class Solution:
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i!=j):
                    if(nums[i]+nums[j]==target):
                        return i,j
    

    def twoSumE(nums,target):
        for index, element in enumerate(nums):
            for ind, ele in enumerate(nums):
                if(index!=ind):
                    if(element+ele == target):
                        return index, ind

    def twoSumM(nums,target):
        num = nums
        for i in num:
            print('i:',i)
            for j in nums:
                print('j:',j)
                print("Index i:", num.index(i) )
                print("Index j:", num.index(j) )
                if(num.index(i)!=nums.index(j)):
                    print('inside if 1')
                    if(int(i)+int(j)==target):
                        return nums.index(i),nums.index(j)


    x,y = twoSumE([3,3],6)
    print(x,y)

'''
def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

x,y = twoSum([3,3],6)    
print(x)
print(y)