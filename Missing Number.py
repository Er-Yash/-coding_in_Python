class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l=len(nums)+1
        # s=(l*(l+1))/2
        # S=0
        # for i in range(0,l):
        #   S=S+nums[i]
        # return s-S
        res=0
        for i in range(len(nums)+1):
          res^=i
        for n in nums:
          res^=n
        return res

        
