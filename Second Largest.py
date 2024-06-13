import sys
class Solution:
	def print2largest(self,arr, n):
		# code here
		if n<2:
		    return -1
		first=arr[0]
		second=-sys.maxsize
		for i in range(1,n):
		    if arr[i]>first:
		        second=first
		        first=arr[i]
		    elif arr[i]>second and arr[i]!=first:
		        second=arr[i]
		return second if second!=-sys.maxsize else -1
