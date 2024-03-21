import random
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
            i = i + 1
        return profit
    def canJump(self, nums):
        for i in range(len(nums) - 1):
            print(i)
            if nums[i] == 0 and nums[i + 1] != 0:
                print("First Branch")
                jump = 2
                for j in range(i-1,-1,-1):
                    if nums[j] >= jump:
                        print("here")
                        break
                    if j == 0 and nums[j] < jump:
                        return False
                    jump = jump + 1
            if nums[i] == 0 and nums[i+1] == 0:
                j = i
                jump = 1
                while j < len(nums) and nums[j] == 0:
                    jump += 1
                    if j == len(nums) - 1:
                        jump -= 1
                    j += 1
                for k in range(i-1,-1,-1):
                    if nums[k] >= jump:
                        break
                    if k == 0 and nums[k] < jump:
                        return False
                    jump = jump + 1
        return True
    def jump2(self, nums):
        #think in terms of sums!
        end = len(nums) - 1
        solution = end
        for j in range(nums[0], 0, -1):
            steps = 0
            i = 0
            sum = 0
            while(i < end):
                if (nums[i] == 0):
                    break
                if (i == 0):
                    sum += j
                    steps += 1
                    i = i + j
                else:
                    sum += nums[i]
                    steps += 1
                    i = i + nums[i]
                if (sum >= end and steps < solution):
                    #print(solution)
                    solution = steps
        return solution
    def h_Index(self, nums):
        papers = len(nums)
        for i in range(papers, 0, -1):
            citations = 0
            #print(i)
            for j in range(papers):
                #print(nums[j])
                if nums[j] >= i:
                    citations += 1
            if citations >= i:
                return i
        return "No citations"
    class RandomizedSet:
        def __init__(self, arr = []):
            self.set = arr
        
        def insert(self, val):
            for i in self.set:
                if i == val:
                    return False
            self.set[len(self.set)] = val
            return True

        def remove(self, val):
            for i in range(len(self.set)):
                if self.set[i] == val:
                    for j in range(i,len(self.set) - 1,1):
                        temp = self.set[j]
                        self.set[j] = self.set[j+1]
                        self.set[j+1] = temp
                    self.set.pop()
                    return True
            return False
        def getRandom(self):
            random.choice(self.set)
        #380 on LeetCode is tough; come back later
    def productExceptSelf(self, nums):
        product = 1
        count = 0
        answer = []
        for i in nums:
            if i == 0 and count == 0:
                count += 1
                continue
            if i == 0 and count == 1:
                count += 1
                product = 0
                break
            product *= i
        print(product)
        for j in range(len(nums)):
            if count == 1 and nums[j] != 0:
                answer.append(0)
            elif count == 1 and nums[j] == 0:
                answer.append(product)
            elif nums[j] == 0:
                answer.append(product)
            else:
                result = product * int((nums[j] ** (-1)))
                answer.append(result)
        return answer
    def canCompleteCircuit(self, gas, cost):
        for i in range(len(gas)):
            tank = 0
            count = 0
            j = i
            while(count < len(gas)):
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                if j == len(gas) - 1:
                    j = -1
                j += 1
                count += 1
                if count == len(gas):
                    return i
        return -1
    """ [1,5,4,3,2,1]: candies [1,5,4,3,2,1]
    [1,5,4,6,2,3]  candies [1,2,1,2,1]
    [1,5,5,5,4,6]
    [1,2,3,4,5,4]
    [5,4,3,2,1,4,5,5,5]
    [1,1,1,2]
    [5,4,3,2,2,2,4] """
    def candy(self, ratings):
        i = 0
        candies = 0
        while i <= len(ratings) - 1:
            count = 1
            if i <= len(ratings) - 2 and ratings[i] < ratings[i + 1]:
                j = i
                while j <= len(ratings) - 2 and ratings[j] < ratings[j+1]:
                    count += 1
                    j += 1
                for c in range(count, 0, -1):
                    candies += c
                if j == len(ratings) - 1:
                    break
                elif j == len(ratings) - 2:
                    i = j
                else:
                    i = j + 1
            elif i <= len(ratings) - 2 and ratings[i] > ratings[i + 1]:
                j = i
                while j <= len(ratings) - 2 and ratings[j] > ratings[j + 1]:
                    count += 1
                    j += 1
                for c in range(count, 0, -1):
                    candies += c
                if j == len(ratings) - 1:
                    break
                elif j == len(ratings) - 2:
                    i = j
                else:
                    i = j + 1
            elif i <= len(ratings) - 2 and ratings[i]  == ratings[i + 1] and ratings[i] == ratings[i-1]:
                candies += count
            elif i == 0 and ratings[i] == ratings[i + 1]:
                candies += count 
            elif i == len(ratings) - 1 and ratings[i] > ratings[i-1]:
                count += 1
                candies += count
            elif i == len(ratings) - 1 and ratings[i] <= ratings[i-1]:
                candies += count
            i += 1
        return candies





    


            
            
            





        





            
                    



        
            






    





            

        
        
                

solution = Solution
ratings = [1,0,2]
ratings2 = [1,2,2]
result = solution.candy(solution, ratings)
result2 = solution.candy(solution, ratings2)
print(result)
print(result2)
