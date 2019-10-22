#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 
# a,b,c,d -->
  #a,b,c,d
  #a,c,d,b,
  #b,d,a,c,
  #d,c,b,a,
  #c,a,d,b,
  
  
  #HashMap
  #Time O(n), Space O(n)
def checkPerm1(str1,str2):

#Base Error Cases
if len(str1) == 0 or len(str2) ==0:
  return False
if len(str1) != len(str2)
  return False
  
  #Loop into Map
  map = {}
for i in range (len(str1)):
  if str1[i] not in map:
    map[str1[i]]
  if str[2] not in map:
    map[str2[i]]
  elif str1[i] in map:
    map[str1[i]] +=1
    elif str2[i] in map
      map[str2[i]] -=1
  for k in map:
  if map[k] !=0:
    return False
  else:
    return True
  
  #Sort and Compare
  #O(logn)? and O(n)
  def checkPerm2(str1,str2):
  str1 = str1.sort()
  str2 = str2.sort()
  if str1 == str2:
    return True
  else: 
    return False
    
    
  
  
  #Bit Manipulation
