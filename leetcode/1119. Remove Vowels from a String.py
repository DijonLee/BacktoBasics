class Solution(object):
    def removeVowels(self, S):
        newString = ""
        map = {"a","e","i","o","u","A","E","I","O","U"}
        for s in S:
            if s not in map:
                newString+= s
        return newString
           
    
