class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # method 1: 
        # nums1[:]=nums1[0:m]
        # nums1.extend(nums2)
        # nums1.sort()
        
        
        # method 2:
        
        
        new = nums1[:m] 
        nums1[:] = []
        

        pin1 = 0 
        pin2 = 0
        
        while pin1 < m and pin2 < n: 
            if new[pin1] < nums2[pin2]:
                nums1.append(new[pin1])
                pin1 = pin1 + 1
                
            else: 
                nums1.append(nums2[pin2])
                pin2 = pin2 + 1
                
        print("the nums1 in the end:  ",nums1)
        print("the new in the end:  ",new)
        print("the nums2 in the end:  ",nums2)
        
        # then fill the nums1:
        # check the remaining element in nums1 and nums2
        
        if pin1 == m:
            print("List new is empty")
        else:
            print("remaining elements are in new and after:",pin1)
            
        if pin2 == n:
            print("List nums2 is empty")
        else:
            print("remaining elements are in nums2 and after:", pin2)
            
            
            
        if pin1 < m:
            nums1[pin1+pin2:] = new[pin1:]
            
        if pin2 < n:
            nums1[pin1+pin2:] = nums2[pin2:]