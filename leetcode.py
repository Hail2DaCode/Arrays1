import random
import math
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
    #trapping rain water

    def romanToInt(self, s):
        number = 0
        data = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)):
            number = number + data[s[i]]
            if i != len(s) - 1 and s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    number -= 2
            elif i != len(s) - 1 and s[i] == "X":
                if s[i+1] =="L" or s[i+1] == "C":
                    number -= 20
            elif i != len(s) - 1 and s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    number -= 200
        return number
    def intToRoman(self, num):
        roman = ""
        data = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        array = [1,5,10,50,100,500,1000,5000]
        for i in range(len(array) -1, -1, -1):
            if num >= array[i]:
                count = num // array[i]
                remainder = num % array[i]
                if count == 4:
                    if roman != "" and roman[-1] == "D" and num >= 400:
                        newRoman = ""
                        for k in range(len(roman) - 1):
                            newRoman += roman[k]
                        newRoman += "CM"
                        roman = newRoman
                    elif num >= 400:
                        roman += "CD"
                    elif roman != "" and roman[-1] == "L" and num >= 40:
                        newRoman = ""
                        for k in range(len(roman) - 1):
                            newRoman += roman[k]
                        newRoman += "XC"
                        roman = newRoman
                    elif num >= 40:
                        roman += "XL"
                    elif roman != "" and roman[-1] == "V" and num == 4:
                        newRoman = ""
                        for k in range(len(roman) - 1):
                            newRoman += roman[k]
                        newRoman += "IX"
                        roman = newRoman
                    elif num == 4:
                        roman += "IV"
                else:
                    for j in range(count):
                        roman += data[array[i]]
                num = remainder
        return roman
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
            elif count > 0 and s[i] == " ":
                break
        return count
    def longestCommonPrefix(self, strs):
        prefix = ""
        word = None
        for i in range(len(strs)):
            if i == 0:
                word = strs[i]
            if len(word) > len(strs[i]):
                word = strs[i]
                #print(word)
        for i in range(len(word)):
            count = 0
            for j in range(len(strs)):
                if word[i] == strs[j][i]:
                    count += 1
                if count == len(strs) and j == len(strs) - 1:
                    prefix += word[i]
                elif count < len(strs) and j == len(strs) -1:
                    return prefix
        return prefix
    def reverseWords(self, s):
        word = ""
        i = len(s) - 1
        while (i >= 0):
            array = []
            while i >= 0 and s[i] != " ":
                array.append(s[i])
                i -= 1
            for k in range(len(array) - 1, -1, -1):
                word += array[k]
            if i != len(s) - 1 and s[i + 1] != " ":
                word += " "
            i -= 1
        return word
    def convert(self, s, numRows):
        word = ""
        mainArray = [""] * numRows
        count = 0
        down = True
        for i in range(len(s)):
            if down:
                mainArray[count] += s[i]
                count += 1
                if count == numRows - 1:
                    down = False
            elif not down:
                mainArray[count] += s[i]
                count -= 1
                if count == 0:
                    down = True
        for j in range(len(mainArray)):
            word += mainArray[j]
        return word
    def strStr(self, haystack, needle):
        count = 0
        index = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[count]:
                if(count == 0):
                    index = i
                count += 1
            else:
                index = -1
                count = 0
            if count == len(needle):
                break
        return index
    #HashMaps Part of Top 150
    def canConstruct(self, ransomNote, magazine):
        hashMap = {}
        for i in magazine:
            try:
                hashMap[i]
            except:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for c in ransomNote:
            try:
                hashMap[c]
            except:
                return False
            else:
                if hashMap[c] > 0:
                    hashMap[c] -= 1
                    continue
                else:
                    return False
        return True
    def isIsomorphic(self, s, t):
        hashMap = {}
        hashMap2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            try:
                hashMap[i]
            except:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for c in t:
            try:
                hashMap2[c]
            except:
                hashMap2[c] = 1
            else:
                hashMap2[c] += 1
        for j in range(len(s)):
            if hashMap[s[j]] != hashMap2[t[j]]:
                return False
        return True
    def wordPattern(self, pattern, s):
        word = ""
        count = 0
        hash = {}
        for i in range(len(s)):
            if s[i] == " " or i == len(s) - 1:
                if i == len(s) - 1:
                    word += s[i]
                try:
                    hash[pattern[count]]
                except:
                    for key, value in hash.items():
                        if value == word and key != pattern[count]:
                            return False
                    hash[pattern[count]] = word
                    count += 1
                    word = ""
                else:
                    for key,value in hash.items():
                        if value == word and key != pattern[count]:
                            return False
                    if hash[pattern[count]] != word:
                        return False
                    else:
                        count += 1
                        word = ""
            else:
                word += s[i]
        for j in range(len(pattern)):
            word += hash[pattern[j]]
            if j == len(pattern) - 1:
                break
            word += " "
        if word != s:
            return False
        return True
    def isAnagram(self, s, t):
        data = {}
        for letter in s:
            try:
                data[letter]
            except:
                data[letter] = 1
            else:
                data[letter] += 1
        for letter in t:
            try:
                data[letter]
            except:
                return False
            else:
                data[letter] -= 1
        for value in data.values():
            if value != 0:
                return False
        return True
    def groupAnagrams(self, strs):
        arrayFinal = []
        arrayNext = strs
        while(len(arrayNext) > 0):
            currentFinal = []
            currentNext = []
            for word in arrayNext:
                data = {}
                for letter in arrayNext[0]:
                    try:
                        data[letter]
                    except:
                        data[letter] = 1
                    else:
                        data[letter] += 1
                cancel = False
                for letter2 in word:
                    try:
                        data[letter2]
                    except:
                        cancel = True
                        break
                    else:
                        #print(word)
                        data[letter2] -= 1
                for value in data.values():
                    if value != 0:
                        cancel = True
                        break
                if cancel:
                    currentNext.append(word)
                else:
                    currentFinal.append(word)
            arrayFinal.append(currentFinal)
            #print(currentNext)
            arrayNext = currentNext
        return arrayFinal
    def twoSum(self, nums, target):
        array = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    array.append(i)
                    array.append(j)
                    break
            if len(array) > 0:
                break
        return array
    # Think of a way to write it without quadratic
    # time complexity
    def isHappy(self, n):
        data = {}
        while(n != 1):
            str_n = f'{n}'
            array = []
            total = 0
            for letter in str_n:
                number = int(letter)
                array.append(number)
            for num in array:
                total += num**2
            try:
                data[total]
            except:
                data[total] = 1
            else:
                data[total] += 1
            finally:
                if data[total] > 1:
                    return False
            n = total
        return True
    #This is a recursion algo for isHappy that is
    #just for fun!
    def isHappyRecursion(self, n, data):
        if n == 1:
            return True
        str_n = f'{n}'
        array = []
        total = 0
        for letter in str_n:
            number = int(letter)
            array.append(number)
        for num in array:
            total += num**2
        try:
            data[total]
        except:
            data[total] = 1
        else:
            data[total] += 1
        finally:
            if data[total] > 1:
                return False
        n = total
        print(total)
        return self.isHappyRecursion(self, n, data)
        

    




                    

    
        
                


                




        
                
            


            


            


            




                    
                










    


            
            
            





        





            
                    



        
            






    





            

        
        
                

solution = Solution
number = 19
number2 = 2
dict = {}
result1 = solution.isHappyRecursion(solution, number, dict)
print(result1)
result2 = solution.isHappyRecursion(solution, number2, dict)
print(result2)

