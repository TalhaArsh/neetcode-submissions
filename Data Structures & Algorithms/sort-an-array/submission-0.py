class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            arrLeft, arrRight = arr[L: M+1] , arr[M+1 : R+1]
            i,j,k = L, 0, 0 

            while j< len(arrLeft) and k < len(arrRight):
                if arrLeft[j] <= arrRight[k]:
                    arr[i] = arrLeft[j]
                    j += 1
                else:
                    arr[i] = arrRight[k]
                    k += 1
                i += 1
            while j< len(arrLeft):
                arr[i] = arrLeft[j]
                j += 1
                i += 1
            while k< len(arrRight):
                arr[i] = arrRight[k]
                k += 1
                i += 1
            
            

        def mergeSort(arr,l,r):
            if l == r:
                return arr

            mid = (l + r) //2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, mid, r)
            
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
            
        