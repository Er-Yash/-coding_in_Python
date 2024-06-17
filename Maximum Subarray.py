class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=0
        maxi=-sys.maxsize-1

        for i in range(len(nums)):
          sums+=nums[i]
          if sums>maxi:
            maxi=sums
          if sums<0:
            sums=0
        return maxi
        
