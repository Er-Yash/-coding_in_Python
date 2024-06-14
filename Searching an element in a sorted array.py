def searchInSorted(self,arr, N, K):
        #linear search
        for i in range(0,N):
            if arr[i]==K:
                return 1
        return -1
         
        #binary search
        # l=0
        # e=N-1
        # while l<=e:
        #     m=(l+e)//2
        #     if arr[m]==K:
        #         return 1
        #     elif arr[m]<K:
        #         l=m+1
        #     else:
        #         h=m-1
        # return -1
