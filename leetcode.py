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
    def rotate3(self, nums, k):
        hash = {}
        for i in range(len(nums)):
            hash[i] = nums[i]
        for i in range(len(nums)):
            count = i
            for j in range(k):
                count += 1
                if count == len(nums):
                    count = 0    
            #print(count)
            nums[count] = hash[i]
            """ count = i + k
            if count >= len(nums):
                count = count - len(nums)
                print(count)
                nums[count] = hash[i]
            else:
                nums[count] = hash[i] """
    def maxProfit(self, prices):
        low = prices[0]
        lowDay = 0
        for i in range(1, len(prices), 1):
            if low > prices[i]:
                low = prices[i]
                lowDay = i
        high = low
        for i in range(lowDay, len(prices), 1):
            if high < prices[i]:
                high = prices[i]
        return high - low
    def maxProfitMedium(self, prices):
        profit  = 0
        i = 0
        while( i < len(prices) - 1):
            #print("start")
            low = prices[i]
            if low < prices[i+1]:
                high = prices[i+1]
                i = i + 1
                while i < len(prices) - 1 and high < prices[i+1]:
                    high = prices[i+1]
                    #print(i)
                    i = i + 1
                profit = profit + (high - low)
                #print(i)
            #print(i)
            if i == len(prices) - 1:
                break
            i = i + 1
        return profit



        
            






    





            

        
        
                

solution = Solution
prices = [1,2,3,4,5]
prices2 = [7,1,5,3,6,4]
prices3 = [7,6,4,3,1]
print(solution.maxProfitMedium(solution,prices3))

