'''
Date - 31/05/2018
@author - Purvak 
Timestamp - 14:08

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        
        nums1 = sorted(nums1)
        ln = len(nums1)
        if(ln%2==0):
            median = (nums1[ln//2 -1]+nums1[ln//2])/2
        elif(ln==1):
            return float(nums1[0])
        else:
            median = float(nums1[ln//2])
        return median