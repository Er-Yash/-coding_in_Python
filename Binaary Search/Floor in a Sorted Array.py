 def findFloor(self,A,N,X):
        #Your code here
        i=0
        e=N-1
        ans=-1
        while i<=e:
            m=(i+e)//2
            if A[m]==X:
                return m
            elif A[m]<X:
                i=m+1
                ans=m
                
            else:
                e=m-1
        return ans
