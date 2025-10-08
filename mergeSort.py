class Sort : 
    def merger_sort(self,Arr): 
        #creating a base case   
        if len(Arr) <= 1 :
            return Arr 
        
        #Splitting the elements if the array  
        mid = len(Arr)//2 
        left_Arr = self.merger_sort(Arr[:mid])
        right_Arr =self.merger_sort(Arr[mid:])
        return self.merge(left_Arr,right_Arr)
    
    def merge(self , left , right): 
        result = []
        i = j = 0 
        while i < len(left)  and j < len(right) : 
            if left[i] < right [j]:
                result.append(left[i])
                i+=1
            else :
                result.append(right[j])
                j+=1 
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result 

arr = [ 14,5,6,7,9,0]
sort = Sort()
print(sort.merger_sort(arr))