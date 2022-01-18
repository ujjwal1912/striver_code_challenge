def merge(self, arr, l, m, r):
        n1, n2 = m-l+1, r-m
        L, R = [0]*n1, [0]*n2
        for i in range(n1):
            L[i] = arr[l+i]
        for i in range(n2):
            R[i] = arr[m+1+i]
        i, j, k = 0, 0, l
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
                k+=1
            else:
                arr[k]=R[j]
                j+=1
                k+=1
        while i<n1:
            arr[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=R[j]
            j+=1
            k+=1
        
    def merge_sort(self,arr, l, r):
        if l<r:
            m = l+(r-l)//2
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m+1, r)
            self.merge(arr, l, m, r)
