class Solution(object):
    def firstUniqChar(self, s):
        map = {} # Going to declare a map to keep track of all strings that are visited and their index
        for i in range(len(s)): #Loop through the string
            char = s[i]
            
            #If character of the stirng is not in map then add it with its index
            if char not in map: 
                map[char] = i  # char: index
            #If the character of the string is already in the map then we will nullify it, we dont care about repeated
            elif char in map: 
                map[char] = float("inf") 
                
        #Now we will pick the element with the lowest index, looping through the hashmap and getting the min, and setting first to MAX to ensure we dont accidently pick a element
        first = float("inf") # 
        for key,value in map.iteritems():
            first = min(first,value)
        if first > len(s):
            return -1
        else:
            return first
            
            
            
                       
        #https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
