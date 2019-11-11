#https://leetcode.com/problems/implement-strstr/


class Solution(object):
    def strStr(self, haystack, needle):
        print("Searching for", needle, "in", haystack)
        if haystack and not needle:
            return 0
        if not haystack and needle:
            return -1
        if not haystack and not needle:
            return 0
        if haystack == needle:
            return 0
            
        occurance = float("inf") #set index to infinity
        for i in range(len(haystack)-(len(needle)-1)): 
            if haystack[i:i+len(needle)] == needle: # if needle found in substring
                occurance = (min(occurance,i))  #update index
        if occurance < float("inf"):
            return occurance
        else:
            return -1
        
