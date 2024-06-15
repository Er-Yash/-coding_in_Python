def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        arr3=arr1+arr2
        arr3.sort()
        j=0
        for i in range(len(arr3)-1):
            if arr3[i]!=arr3[i+1]:
                arr3[j]=arr3[i]
                j+=1
        arr3[j]=arr3[-1]
        j+=1
        arr3=arr3[:j]
        return arr3
                
