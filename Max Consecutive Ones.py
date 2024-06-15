class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        r=0
        for i in nums :
          if i:
            c+=1
            r=max(c,r)
          else:
            c=0
        return max(c,r)
           
           
        
