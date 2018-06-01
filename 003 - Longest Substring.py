'''
Date - 31/05/2018
@author - Purvak 
Timestamp - 13:08

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        track = []
        count = 0
        count_track = [0]
        count_track.append(1)
        
        if len(s) == 0:
            return 0
        if len(s)== 1:
            return 1
        
        for i in range(len(s)):
            if (i>0 and s[i] == s[i-1]):
                count_track.append(count)
                track = []
                track.append(s[i])
                count= 1
                
            elif s[i] in track:
                count_track.append(count)
                count = count - track.index(s[i]) -1 
                index = track.index(s[i])
                track = track [index+1:]
                track.append(s[i])
                count = count+1
            else:
                count = count +1
                track.append(s[i])
        
        count_track.append(count)

        return max(count_track)





'''
def longsub(s):
    track = []
    count = 0
    count_track = []
    for i in range(len(s)):
        if s[i] in track:
            print("S[I]", s[i])
            print("Track in if:", track)
            count_track.append(count)
            print('count track', count)
            count =0
            track = []
            print("Track in if:", track)
            
        else:
            print("S[I] in else", s[i])            
            count = count +1
            track.append(s[i])
            print("Track in else:", track)            
            

    return max(count_track)

ans = longsub("abcab") 
print ("ANSSSS",ans)
     
'''
                
        

