'''

Date - 2/06/2018
@author - Purvak 
Timestamp - 00:08



'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(len(str(x)) == 1):
            return x
        
        y=x
        flag=0
        if(x < 0):
            y = -x
            flag =1
        j=0
        ans = 0
        for i in range(len(str(y)), 0 , -1):
            element = y//(10**(i-1))
            y = y%(10**(i-1))
            ans+= element*(10**j)
            j=j+1
        
        
        if (str(ans)[0] == '0'):
            ans = str(ans)[1:] 
        
        if (abs(ans) > 2147483647):
            return 0
        
        if(flag == 1):
            return -ans
        else:
            return ans