class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        candidate=None
        for i in nums:
          if c==0:
            candidate=i
          c+=(1 if i==candidate else -1)
        return candidate

         

         
        
