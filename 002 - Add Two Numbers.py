'''
Date - 30/05/2018
@author - Purvak 
Timestamp - 20:44


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry =0
        temp =0 
        result = None
        while l1!= None or l2!=None or carry == 1: 
            if l1!= None:
                temp+=l1.val
                l1= l1.next
                
            if l2!= None:
                temp+=l2.val
                l2= l2.next
            
            temp+=carry
            carry = temp // 10
            value = temp % 10
            temp = 0
            if result is None:
                result = ListNode(value)
                result_end = result
            
            else:
                result_end.next = ListNode(value)
                result_end = result_end.next
            
            
            
        return result   
            
  
       