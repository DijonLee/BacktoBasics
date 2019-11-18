class Solution(object):
    def defangIPaddr(self, address):
        DFaddress = ""
        for ea in address:
            if ea == ".":
                DFaddress+="[.]"
            else:
                DFaddress+=ea
        return DFaddress
            
        """
        :type address: str
        :rtype: str
        """
        
