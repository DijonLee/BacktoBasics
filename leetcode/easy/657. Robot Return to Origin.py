class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for each in moves:
            if each == "U":
                    y+=1
            if each == "D":
                    y-=1
            if each == "L":
                    x-=1
            if each == "R":
                    x+=1
        if x ==0 and y ==0:
            return True
        else:
            return False
        """
        :type moves: str
        :rtype: bool
        """
        
        
        #https://leetcode.com/problems/robot-return-to-origin/
