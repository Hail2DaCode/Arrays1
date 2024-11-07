import random
import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
class RandNode:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
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
    def containsNearbyDuplicates(self, nums, k):
        data = {}
        for i in range(len(nums)):
            try:
                data[nums[i]]
            except:
                data[nums[i]] = i
            else:
                num = abs(data[nums[i]] - i)
                if(num <= k):
                    return True
                else:
                    data[nums[i]] = i
        return False
    def longestConsecutive1(self, nums):
        max = nums[0]
        for i in range(1,len(nums),1):
            if nums[i] > max:
                max = nums[i]
        count_array = [0] * (max + 1)
        for num in nums:
            count_array[num] += 1
        for i in range(1, max + 1):
            count_array[i] += count_array[i-1]
        sort_nums = [0] * len(nums)
        for i in range(len(nums) - 1, - 1, -1):
            sort_nums[count_array[nums[i]] - 1] = nums[i]
            count_array[nums[i]] -= 1
        sequence = []
        count = 1
        for i in range(0, len(sort_nums) - 1, 1):
            if sort_nums[i + 1] == sort_nums[i]:
                continue
            elif sort_nums[i + 1] - 1 == sort_nums[i]:
                count += 1
            else:
                sequence.append(count)
                count = 1
        sequence.append(count)
        max = sequence[0]
        for num in sequence:
            if num > max:
                max = num
        return max
    def longestConsecutive2(self, nums):
        data = {}
        min_array = []
        min_number = 0
        matches = 0
        count_array = []
        count = 1
        for num in nums:
            data[num] = 0
        for num in nums:
            if data.get(num + 1) != None or data.get(num - 1) != None:
                data[num] = 1
        for key in data:
            if data[key] == 1 and data.get(key - 1, "No") == "No":
                print("This is the " +str(key))
                min_number += 1
                min_array.append(key)
            elif data[key] == 1:
                matches += 1
        if min_number > 0:
            index = 0
            for i in range(matches + min_number):
                if data.get(min_array[index] + count) != None:
                            count += 1
                else:
                            count_array.append(count)
                            count = 1
                            if index < len(min_array):
                                index += 1
                            else:
                                break
            count_array.append(count)
            high = count_array[0]
            for num in count_array:
                if num > high:
                    high = num
            return high
        else:
            return 1
    def isPalindrome(self, s):
        data = {}
        word = ""
        for i in range(65, 91):
            data[chr(i)] = chr(i + 32) 
        for letter in s:
            if ord(letter) >= 48 and ord(letter) <= 57:
                word += letter
            elif ord(letter) >= 65 and ord(letter) <= 90:
                word += data[letter]
            elif ord(letter) >= 97 and ord(letter) <= 122:
                word += letter
            else:
                continue
        iterator = len(word) - 1
        for letter in word:
            if letter != word[iterator]:
                return False
            iterator -= 1
        return True
    def isSubsequence(self, s, t):
        iterator = 0
        for letter in t:
            if s[iterator] == letter:
                iterator += 1
        if iterator != len(s):
            return False
        return True
    def twoSumII(self, numbers, target):
        index = 0
        sum = 0
        result = []
        for i in range(len(numbers), 0, -1):
            if target >= numbers[i-1]:
                index = i + 1
                print(index)
                break
        if index == 2:
            result = [1,2]
        else:
            for i in range(1,index):
                for j in range(i+1,index):
                    sum = numbers[i-1] + numbers[j-1]
                    print(sum)
                    if sum == target:
                        result.append(i)
                        result.append(j)
        return result
    def maxArea(self, height):
        area = 1
        for i in range(len(height)):
            for j in range(len(height) - 1,i, -1):
                max_height = 1 
                if height[j] > height[i]:
                    max_height = height[i]
                else:
                    max_height = height[j]
                length = j - i
                product = max_height * length
                if product > area:
                    area = product
        return area
    def threeSum(self, nums):
        result = []
        count = 0
        skip = False
        zero = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                next = []
                for k in range(j + 1, len(nums)):
                    if ((nums[i] + nums[j] + nums[k]) == 0):
                        if nums[i] == 0 and nums[j] == 0 and nums[k] ==0:
                            zero.append(nums[i])
                            zero.append(nums[j])
                            zero.append(nums[k])
                            continue
                        if count > 0:
                            data = {}
                            data[nums[i]] = True
                            data[nums[j]] = True
                            data[nums[k]] = True
                            for array in result:
                                stop = 0
                                try:
                                    data[array[0]]
                                except:
                                    pass
                                else:
                                    stop += 1
                                try:
                                    data[array[1]]
                                except:
                                    pass
                                else:
                                    stop += 1
                                try:
                                    data[array[2]]  
                                except:
                                    pass
                                else:
                                    stop += 1
                                if stop == 3:
                                    skip = True
                                    break
                        if not skip:
                            next.append(nums[i])
                            next.append(nums[j])
                            next.append(nums[k])
                            result.append(next)
                            count += 1
                        skip = False
        if len(zero) > 1:
            result.append(zero)
        return result
    def threeSum2(self, nums):
        result = []
        count = 0
        skip = False
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                next = []
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if count > 0:
                            for array in result:
                                stop = 0
                                if nums[i] == array[0] or nums[i] == array[1] or nums[i] == array[2]:
                                    stop += 1
                                if nums[j] == array[0] or nums[j] == array[1] or nums[j] == array[2]:
                                    stop += 1
                                if nums[k] == array[0] or nums[k] == array[1] or nums[k] == array[2]:
                                    stop += 1
                                if stop == 3:
                                    skip = True
                                    break
                        if not skip:
                            next.append(nums[i])
                            next.append(nums[j])
                            next.append(nums[k])
                            result.append(next)
                            count += 1
                        skip = False
        return result
    def hasCycle(self, head):
        current = head
        data = {}
        while(current.next != None or data.get(current) != None):
            data[current] = current.data
            if data.get(current.next) != None:
                return True
            current = current.next
        return False
    def addTwoNumbers(self, l1, l2):
        current = l1.head
        string1 = ""
        while(current != None):
            string1 = str(current.data) + string1
            current = current.next
        first_num = int(string1)
        string1 = ""
        current = l2.head
        while(current != None):
            string1 = str(current.data) + string1
            current = current.next
        second_num = int(string1)
        sum = first_num + second_num
        string1 = str(sum)
        link_list = LinkedList()
        for i in range(len(string1)):
            #nodei = Node(int(string1[i]))
            if i == 0:
                link_list.head = Node(int(string1[i]))
            else:
                old_head = link_list.head
                link_list.head = Node(int(string1[i]))
                link_list.head.next = old_head
        return link_list
    def mergeTwoLists(self, list1, list2):
        current1 = list1
        current2 = list2
        new_head = None
        if current1.data == None or current2.data == None:
            if current2.data != None:
                return list2
        else:
            if current2.data < current1.data:
                new_head = current2
                while current2.next != None and current2.next.data < current1.data:
                    current2 = current2.next
                head2 = current2.next
                current2.next = current1
                current2 = head2
            while(current1.next != None):
                while(current2 != None and current2.data <= current1.next.data):
                    head1 = current1.next
                    head2 = current2.next
                    current1.next = current2
                    current2.next = head1
                    current2 = head2
                current1 = current1.next
            if current2 != None and current2.data > current1.data:
                current1.next = current2
        if new_head != None:
            return new_head
        return list1
    def copyRandomList(self, head):
        node_array = []
        index_array = []
        current = head
        while current != None:
            node = RandNode(current.val)
            node_array.append(node)
            current2 = head
            count = 0
            if current.next == None:
                node_array.append(None)
            while current2 != None:
                if current2 == current.random:
                    index_array.append(count)
                    break
                count += 1
                if current2.next == None:
                    index_array.append(count)
                current2 = current2.next
            current = current.next
        for i in range(len(node_array)-1):
            node_array[i].next = node_array[i+1]
            node_array[i].random = node_array[index_array[i]]
        return node_array[0]
    def reverseBetween(self, head, left, right):
        array = [None] * (right-left+1)
        position = 1
        current = head
        index = len(array) - 1
        while current != None:
            if position >= left and position <= right:
                array[index] = current.val
                index -= 1
                print(f'index: {current.val}')
            position += 1
            current = current.next
        position = 1
        index = 0
        current = head
        while current != None:
            if position >= left and position <= right:
                current.val = array[index]
                index += 1
            position += 1
            current = current.next
        return head
    def reverseBetween2(self, head, left, right):
        current = head
        position = 1
        index = right - left
        current2 = None
        leftNode = None
        while current != None:
            if position >= left and position <= right:
                if position == left:
                    leftNode = ListNode(current.val, current.next)
                count = index
                current2 = leftNode
                print(f'current2 val = {current2.val}')
                while count > 0:
                    current2 = current2.next
                    count -= 1
                current.val = current2.val
                index -= 1
            position += 1
            current = current.next
        return head
    def reverseKGroup(self, head, k):
        current1 = head
        length = 0
        while current1 != None:
            length += 1
            current1 = current.next
        cycles = length // k
        current4 = head
        count = k - 1
        switches = k // 2
        beforeCurrent2 = None
        beforeCurrent1 = current3
        for i in range(cycles):
            current3 = current4
            current1 = current3
            current2 = current1
            for j in range(switches):
                #beforeCurrent1 = current3
                for k in range(count):
                    if count == count - 1:
                        beforeCurrent2 = current2
                        if j == 0:
                            current4 = current2.next.next
                    current2 = current2.next
                tempNext2 = current2.next
                tempNext1 = current1.next
                if current1.next == current2:
                    current2.next = current1
                    current1.next = tempNext2
                    if beforeCurrent1 != current1:
                        beforeCurrent1.next = current2
                else:
                    if beforeCurrent1 != current1:
                        beforeCurrent1.next = current2
                    current2.next = current1.next
                    beforeCurrent2.next = current1
                    current1.next = tempNext2
                current1 = tempNext1
                count -= 1
                if switches == 0:
                    continue
                else:
                    current2 = current3
                    beforeCurrent1 = beforeCurrent1.next
    #Binary Trees
    def maxDepth(self, root):
        if root == None:
            return 0
        lDepth = Solution.maxDepth(Solution,root.left)
        rDepth = Solution.maxDepth(Solution,root.right)

        if lDepth >= rDepth:
            return lDepth + 1
        else:
            return rDepth + 1
    def maxDepth2(self, root):
        if not root:
            return 0
        depth = 0
        q = []
        q.append(root)
        q.append(None)

        while q:
            curr = q.pop(0)
            if curr is None:
                depth += 1
                if q:
                    q.append(None)
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return depth
    def maxDepth3(self, root):
        if root is None:
            return 0
        q = [root]
        h = 0
        while q:
            size = len(q)
            for _ in range(size):
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            h += 1
        return h
    def isSameTree(self, p, q):
        if p.val != q.val:
            return False
        arr_p = [p]
        arr_q = [q]
        while arr_p:
            node_p = arr_p.pop(0)
            node_q = arr_q.pop(0)
            if not node_p.left:
                if node_q.left:
                    print("1st")
                    return False
            else:
                if not node_q.left:
                    print("2nd")
                    return False
                elif node_q.left.val != node_p.left.val:
                    print("3rd")
                    return False
                else:
                    arr_p.append(node_p.left)
                    arr_q.append(node_q.left)
            if not node_p.right:
                if node_q.right:
                    print("4th")
                    return False
            else:
                if not node_q.right:
                    print("5th")
                    return False
                elif node_q.right.val != node_p.right.val:
                    print("6th")
                    return False
                else:
                    arr_p.append(node_p.right)
                    arr_q.append(node_q.right)
        return True
    def invertTree(self, root):
        if root is None:
            return 0
        q = [root]
        while q:
            curr = q.pop(0)
            if curr.left and curr.right:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                q.append(curr.left)
                q.append(curr.right)
            else:
                if curr.left:
                    curr.right = curr.left
                    curr.left = None
                    q.append(curr.right)
                if curr.right:
                    curr.left = curr.right
                    curr.right = None
                    q.append(curr.left)
        return root
            

            

                

            


node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
solution = Solution()
result1 = solution.invertTree(node1)
print(result1.val)
print(result1.left.val)
print(result1.right.val)
print(result1.left.left.val)
print(result1.left.right.val)
print(result1.right.left.val)
print(result1.right.right.val)



                




                


                




        

    


            

               





       



          

        




       

                


        
            






                                        
                             


         


                





                








            


           
         

        
        

    




                    

    
        
                


                




        
                
            


            


            


            




                    
                










    


            
            
            





        





            
                    



        
            






    





            

        
        
                






