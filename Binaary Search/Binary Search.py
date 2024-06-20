def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s,e=0,len(nums)-1
        while s<=e:
          m=(s+e)//2
          if nums[m]==target:
            return m
          elif nums[m]<target:
            s=m+1
          else :
            e=m-1
        return -1
