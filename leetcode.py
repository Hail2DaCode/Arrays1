class Solution:
    def merge(self, nums1, m:int, nums2, n:int):
        for num in range(m, len(nums1)):
            nums1[num] = (nums2[num-m])
            i = num
            while(nums1[i] < nums1[i-1]):
                temp = nums1[i-1]
                nums1[i-1] = nums1[i]
                nums1[i] = temp
                i = i - 1
                if (i == 0):
                    break
        for num in nums1:
            print(num)
    def removeElement(self, nums, val):
        count = 0
        for num in range(len(nums)-1, -1, -1):
            if nums[num] == val:
                count = count + 1
                i = num
                while(i < len(nums)-1):
                    temp = nums[i+1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                    i = i + 1
        #print(count)
        k = len(nums) - count
        return k
    def removeElementBetter(self, nums, val):
        count = 0
        for num, e in reversed(list(enumerate(nums))):
            print(num)
            if nums[num] == val:
                count += 1
                i = num
                while(i < len(nums)-1):
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                    i = i + 1
        k = len(nums) - count
        return k
    def removeDuplicates(self, nums):
        k = len(nums)
        for num in range(len(nums)-1, 0, -1):
            if nums[num] == nums[num-1]:
                txt = "index: {}"
                print(txt.format(num))
                k = k - 1
                i = num
                while (i < len(nums)-1):
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                    i = i + 1
        return k
    def removeDuplicateMedium(self, nums):
        k = len(nums)
        for num in range(len(nums)-1, 1, -1):
            if nums[num] == nums[num-1] and nums[num] == nums[num-2]:
                k = k - 1
                i = num
                for i in range(i,len(nums)-1, 1):
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
        return k
    def majorityElement(self, nums):
        majority = None
        count = 0
        length = None
        if len(nums) % 2 == 0:
            majority = len(nums)/2 + 1
            length = len(nums)/2 - 1
        else:
            majority = len(nums)/2 + 0.5
            length = len(nums)//2
            print(length)
        for i in range(0,length,1):
            temp = nums[i]
            for j in range(len(nums) - 1, i-1, -1):
                if nums[j] == temp:
                    count += 1
            if count == majority:
                return temp
    def rotate(self, nums, k):
        for i in range(k-1,-1,-1):
            temp = nums[i]
            nums[i] = nums[len(nums)-k+i]
            nums[len(nums) - k + i] = temp
        l = k
        for i in range(len(nums)-k, len(nums), 1):
            for j in range(i, l, -1):
                temp = nums[j - 1]
                nums[j-1] = nums[j]
                nums[j] = temp
            l = l + 1
    def rotate2(self, nums, k):
        for i in range(k-1,-1,-1):
            temp = nums[i]
            nums[i] = nums[len(nums)-k+i]
            nums[len(nums)-k+i] = temp
        for i in range(len(nums)-k +1, len(nums), 1):
            for j in range(i, len(nums) - k, -1):
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp
        for i in range(len(nums)-k, len(nums), 1):
            for j in range(i, k, -1):
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp



    





            

        
        
                

solution = Solution
list1 = [1,2,3,4,5,6,7]
solution.rotate2(solution, list1, 1)
for i in list1:
    print(i)
