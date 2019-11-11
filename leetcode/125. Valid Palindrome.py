import re #regex module

class Solution(object):
    def isPalindrome(self, string1):
        if not string1 or len(string1) == 0: #base case
            return True
        
        workableStr = re.sub(r'\W+', '', string1) # Get rid of all non alphanumeric
        workableStr = re.sub(r'\s+'', '', workableStr, flags=re.UNICODE) # get rid of spacing
        
        #If EVEN (e.g abba)
        if len(workableStr)%2 == 0:
            leftHalf = workableStr[0:(len(workableStr)/2)].lower()            #Get top half
            rightHalf = ''.join(reversed(workableStr[len(workableStr)/2:len(workableStr)])).lower() # Get bottom half
            if leftHalf == rightHalf: #Check if theyre equal
                return True
            else:
                return False
        else:
            #IF ODD ("abbcbba")  *can have at most 1 different
            leftHalf = workableStr[0:int(math.floor(len(workableStr)/2))].lower() #Get top half
            rightHalf = ''.join(reversed(workableStr[len(leftHalf)+1:(len(workableStr))])).lower() #get bottom half
            if leftHalf == rightHalf: # check if theyre equal
                return True
            else:
                return False
            #https://leetcode.com/problems/valid-palindrome/
