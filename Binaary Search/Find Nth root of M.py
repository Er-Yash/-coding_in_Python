class Solution:
	def NthRoot(self, n, m):
		# Code here
		l=1
		r=m
		while(l<=r):
		    b=(l+r)//2
		    if(b**n==m):
		        return b
		    elif(b**n>m):
		        r=b-1
		    elif(b**n<m):
		        l=b+1
	    return -1
