'''
Date - 1/06/2018
@author - Purvak 
Timestamp - 23:44

Different approaches considered by me.

first line - (2n -2) 

Middle line ??

last line (2n-2)
'''

'''
Using direction

def (s, n):
	
	ls = [[0] for i in range(n)]
	direction = "down"
	row = 0

	for i in range(len(s)):
		if(direction == "down"):
			ls.append

'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        ans = ""
        "Finding pattern between elements we get a step_size of 2n-2"
        step_size = 2*numRows - 2
        
        for i in range(numRows):
            for j in range(i,len(s),step_size):
                ans+= s[j]
                "Checking for diagonal element. Logic of j+step_size-2*i by @kamyu104"
                if(0<i<numRows-1 and j+step_size - 2*i < len(s) ):
                    ans+= s[j+step_size - 2*i]
        
        return ans
