import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i = m; i < nums1.length; i++) {
            nums1[i] = nums2[i-m];
            //System.out.print(nums1[i]);
        }
        int j = nums1.length - 1;
        while(j>0) {
            if (nums1[j] < nums1[j-1]) {
                int temp = nums1[j-1];
                nums1[j-1] = nums1[j];
                nums1[j] = temp;
            }
            j = j - 1;
        }
        for (int num: nums1) {
            System.out.println(num);
        }
    }
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for(int i = nums.length - 1; i >= 0; i--) {
            if(nums[i] == val) {
                count += 1;
                int j = i;
                while(j < nums.length - 1) {
                    int temp = nums[j+1];
                    nums[j + 1] = nums[j];
                    nums[j] = temp;
                    j +=1;
                }
            }
        }
        int k = nums.length - count;
        return k;
    }
    public int removeDuplicates(int[] nums) {
        int k = nums.length;
        for(int i = nums.length - 1; i > 0; i--) {
            if(nums[i] == nums[i-1]) {
                k -= 1;
                for(int j = i; j < nums.length - 1; j++) {
                    int temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        return k;
    }
    public int removeDuplicatesMedium(int[] nums) {
        int k = nums.length;
        for(int i = nums.length - 1; i > 1; i--) {
            if(nums[i] == nums[i-1] && nums[i] == nums[i-2]) {
                k -=1;
                for(int j = i; j < nums.length - 1; j++) {
                    int temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        return k;
    }
    public int majorityElement(int[] nums) {
        int majority;
        int count = 0;
        int length;
        if(nums.length % 2 == 0) {
            majority = nums.length/2 + 1;
            length = nums.length/2 -1;
        }
        else{
            majority = nums.length/2 + 1;
            length = nums.length/2;
        }
        for(int i = 0; i < length; i++) {
            int temp = nums[i];
            for(int j = nums.length - 1; j>= i; j--) {
                if(nums[j] == temp) {
                    count += 1;
                }
            }
            if(count == majority) {
                return temp;
            }
        }
        return count;
    }
    public void rotate(int[] nums, int k) {
        int l = k;
        for(int i = k - 1; i >= 0; i--) {
            int temp = nums[i];
            nums[i] = nums[nums.length - k + i];
            nums[nums.length - k + i] = temp;
        }
        for(int i = nums.length - k; i < nums.length; i++) {
            int j = i;
            while(j > l) {
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
                j--;
            }
            l++;
        }
    }
    public void rotate2(int[] nums, int k) {
        for(int i = k - 1; i >= 0; i--) {
            int temp = nums[i];
            nums[i] = nums[nums.length - k + i];
            nums[nums.length - k + i] = temp;
        }
        for (int i = nums.length - k +1; i < nums.length; i++) {
            for(int j = i; j > nums.length - k; j--) {
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
            }
        }
        for(int i = nums.length - k; i < nums.length; i++) {
            for(int j = i; j > k; j--) {
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
            }
        }
    }
    public void rotate3(int[] nums, int k) {
        HashMap<Integer,Integer> hash = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            hash.put(i, nums[i]);
        }
        for(int i = 0; i < nums.length; i++) {
            int count = i;
            for(int j = 0; j < k; j++) {
                count += 1;
                if(count == nums.length) {
                    count = 0;
                }
            }
            nums[count] = hash.get(i);
        }
    }
    public int maxProfit(int[] prices) {
        int low = prices[0];
        int lowDay = 0;
        for(int i = 1; i < prices.length; i++) {
            if(low > prices[i]) {
                low = prices[i];
                lowDay = i;
            }
        }
        int high = low;
        for(int i = lowDay + 1; i < prices.length; i++) {
            if(high < prices[i] ) {
                high = prices[i];
            }
        }
        return high - low;
    }
    public int maxProfitMedium(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int low = prices[i];
            if (low < prices[i + 1]) {
                int high = prices[i + 1];
                i++;
                while(i < prices.length - 1 && high < prices[i + 1] ) {
                    high = prices[i + 1];
                    i++;
                }
                profit = profit + (high - low);
            }
        }
        return profit;
    }
    public boolean canJump(int[] nums) {
        for(int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 0 && nums[i+1] != 0) {
                System.out.println("First Branch");
                int jump = 2;
                for(int j = i - 1; j >= 0; j--) {
                    if(nums[j] >= jump) {
                        System.out.println("here");
                        break;
                    }
                    if (j == 0 && nums[j] < jump) {
                        return false;
                    }
                    jump += 1;
                }
            }
            if (nums[i] == 0 && nums[i+1] == 0) {
                System.out.println("Second Branch");
                int j = i;
                int jump = 1;
                while (j < nums.length && nums[j] == 0) {
                    jump += 1;
                    if ( j == nums.length - 1) {
                        jump -= 1;
                    }
                    j += 1;
                }
                for(int k = i - 1; k >= 0; k--) {
                    if(nums[k] >= jump) {
                        break;
                    }
                    if( k == 0 && nums[k] < jump) {
                        return false;
                    }
                    jump += 1;
                }
            }
        }
        return true;
    }
    public int jump2(int[] nums) {
        int end = nums.length - 1;
        int solution = end;
        for(int j = nums[0]; j > 0; j--) {
            int steps = 0;
            int i = 0;
            int sum = 0;
            while(i < end) {
                if (nums[i] == 0) {
                    break;
                }
                if(i == 0) {
                    sum += j;
                    steps += 1;
                    i = i + j;
                    continue;
                }
                else {
                    sum += nums[i];
                    steps += 1;
                    i = i + nums[i];
                }
                if(sum >= end && steps < solution) {
                    solution = steps;
                }
            }
        }
        return solution;
    }
    public int hIndex(int[] nums) {
        int papers = nums.length;
        for(int i = papers; i > 0; i--) {
            int citations = 0;
            for(int j = 0; j < papers; j++) {
                if(nums[j] >= i) {
                    citations += 1;
                }
            }
            if(citations >= i) {
                return i;
            }
        }
        return 0;
    }
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int count = 0;
        int[] answer = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0 && count == 0) {
                count += 1;
                continue;
            }
            else if (nums[i] == 0 && count == 1) {
                count += 1;
                product = 0;
                break;
            }
            else {
                product *= nums[i];
            }
        }
        for (int j = 0; j < nums.length; j++) {
            if (count == 1 && nums[j] != 0) {
                answer[j] = 0;
            }
            else if (count == 1 && nums[j] == 0) {
                answer[j] = product;
            }
            else if (nums[j] == 0) {
                answer[j] = product;
            }
            else {
                int result = (int)(product * (Math.pow(nums[j], -1)));
                answer[j] = result;
                //System.out.println(answer[j]);
            }
        }
        return answer;

    }
    public int canCompleteCircuit(int[] gas, int[] cost) {
        for (int i = 0; i < gas.length; i++) {
            int tank = 0;
            int j = i;
            for (int count = 0; count <= gas.length; count++) {
                if (count == gas.length) {
                    return i;
                }
                tank = tank + gas[j] - cost[j];
                if (tank < 0) {
                    break;
                }
                if (j == gas.length - 1) {
                    j = -1;
                }
                j += 1;
            }
        }
        return -1;
    }
    public int candy(int[] ratings) {
        int candies = 0;
        for(int i = 0; i <= ratings.length - 1; i++) {
            int count = 1;
            if (i <= ratings.length - 2 && ratings[i]< ratings[i + 1]) {
                int j = i;
                while(j <= ratings.length - 2 && ratings[j] < ratings[j + 1]) {
                    count += 1;
                    j += 1;
                }
                for (int c = count; c > 0; c--) {
                    candies += c;
                }
                if (j == ratings.length - 1) {
                    break;
                }
                else if (j == ratings.length - 2) {
                    i = j;
                }
                else {
                    i = j + 1;
                }
            }
            else if (i <= ratings.length - 2 && ratings[i] > ratings[i + 1]) {
                int j = i;
                while(j <= ratings.length - 2 && ratings[j] > ratings[j + 1]) {
                    count += 1;
                    j += 1;
                }
                for ( int c = count; c > 0; c--) {
                    candies += c;
                }
                if (j == ratings.length - 1) {
                    break;
                }
                else if (j == ratings.length - 2) {
                    i = j;
                }
                else {
                    i = j + 1;
                }
            }
            else if (i <= ratings.length - 2 && ratings[i] == ratings[i + 1] && ratings[i] == ratings[i - 1]) {
                candies += count;
            }
            else if (i == 0 && ratings[i] == ratings[i + 1]) {
                candies += count;
            }
            else if (i == ratings.length - 1 && ratings[i] > ratings[i - 1]) {
                count += 1;
                candies += count;
            }
            else if (i == ratings.length - 1 && ratings[i] <= ratings[i - 1]) {
                candies += count;
            }
        }
        return candies;
    }
    public int romanToInt(String s) {
        Integer number = 0;
        HashMap<String, Integer> data = new HashMap<>();
        data.put("I", 1);
        data.put("V", 5);
        data.put("X", 10);
        data.put("L", 50);
        data.put("C", 100);
        data.put("D", 500);
        data.put("M", 1000);
        char[] characters = s.toCharArray();
        String[] charArray = new String[characters.length];
        for (int i = 0; i < characters.length; i++) {
            charArray[i] = Character.toString(characters[i]);
        }
        for(int i = 0; i < charArray.length; i++) {
            number = number + data.get(charArray[i]);
            if (i != charArray.length - 1 && charArray[i].equals("I")) {
                if (charArray[i+1].equals("V") || charArray[i+ 1].equals("X")) {
                    number -= 2;
                }
            }
            else if (i != charArray.length - 1 && charArray[i].equals("X")) {
                    if (charArray[i + 1].equals("L") || charArray[i + 1].equals("C")) {
                        number -= 20;
                    }
                }
            else if (i != charArray.length - 1 && charArray[i].equals("C")) {
                if (charArray[i+1].equals("D") || charArray[i+1].equals("M")) {
                    number -= 200;
                }
            }
        }
        return number.intValue();
    }
    public String intToRoman(int num) {
        String roman = "";
        HashMap<Integer, String> data = new HashMap<>();
        data.put(1,"I");
        data.put(5, "V");
        data.put(10, "X");
        data.put(50, "L");
        data.put(100, "C");
        data.put(500, "D");
        data.put(1000, "M");
        int[] array = {1,5,10,50,100,500,1000,5000};
        for(int i = array.length - 1; i >= 0; i--) {
            if(num >= array[i]) {
                int count = num / array[i];
                int remainder = num % array[i];
                if (count == 4) {
                    if (!roman.equals("") && roman.charAt(roman.length() - 1) == 'D' && num >= 400) {
                        String newRoman = "";
                        for(int k = 0; k < roman.length() - 1; k++) {
                            newRoman += roman.charAt(k);
                        }
                        newRoman += "CM";
                        roman = newRoman;
                    }
                    else if (num >= 400) {
                        roman += "CD";
                    }
                    else if (!roman.equals("") && roman.charAt(roman.length() - 1) == 'L' && num >= 40) {
                        String newRoman = "";
                        for (int k = 0; k < roman.length() - 1; k++) {
                            newRoman += roman.charAt(k);
                        }
                        newRoman += "XC";
                        roman = newRoman;
                    }
                    else if (num >= 40) {
                        roman += "XL";
                    }
                    else if (!roman.equals("") && roman.charAt(roman.length() - 1) == 'V' && num == 4) {
                        String newRoman = "";
                        for (int k = 0; k < roman.length() - 1; k++) {
                            newRoman += roman.charAt(k);
                        }
                        newRoman += "IX";
                        roman = newRoman;
                    }
                    else if (num == 4) {
                        roman += "IV";
                    }
                }
                else {
                    for (int j = 0; j < count; j++) {
                        roman += data.get(array[i]);
                    }
                }
                num = remainder;
            }
        }
        return roman;
    }
    public int lengthOfLastWord(String s) {
        int count = 0;
        for(int i = s.length() - 1; i >= 0; i--) {
            if(s.charAt(i) != ' ' ) {
                count += 1;
            }
            else if (count > 0  && s.charAt(i) == ' ') {
                break;
            }
        }
        return count;
    }
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        String word = null;
        for (int i = 0; i < strs.length; i++) {
            if (i == 0) {
                word = strs[i];
            }
            else if (word.length() > strs[i].length()) {
                word = strs[i];
                
            }
        }
        for (int i = 0; i < word.length(); i++) {
            int count = 0;
            for (int j = 0; j < strs.length; j++) {
                if (word.charAt(i) == strs[j].charAt(i)) {
                    count += 1;
                }
                if (count == strs.length && j == strs.length - 1) {
                    prefix += word.charAt(i);
                }
                else if (count < strs.length && j == strs.length - 1) {
                    return prefix;
                }
            }
        }
        return prefix;
    }
    public String reverseWords(String s) {
        String word = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            char[] array = new char[s.length()];
            while( i >= 0 && s.charAt(i) != ' ') {
                array[i] = s.charAt(i);
                i -= 1;
            }
            for (int j = 0; j < array.length; j++) {
                if (array[j] != '\u0000') {
                    word += array[j];
                }
            }
            if (i != s.length() - 1 && s.charAt(i + 1) != ' ') {
                word += ' ';
            }
        }
        return word;
    }
    public String convert(String s, int numRows) {
        String word = "";
        String[] mainArray = new String[numRows];
        for (int i = 0; i < mainArray.length; i++) {
            mainArray[i] = "";
        }
        int count = 0;
        boolean down = true;
        for (int i = 0; i < s.length(); i++) {
            if (down) {
                mainArray[count] += s.charAt(i);
                count += 1;
                if (count == numRows - 1) {
                    down = false;
                }
            }
            else if (!down) {
                mainArray[count] += s.charAt(i);
                count -= 1;
                if (count == 0) {
                    down = true;
                }
            }
        }
        for (int j = 0; j < mainArray.length; j++) {
            word += mainArray[j];
        }
        return word;
    }
    public int strStr(String haystack, String needle) {
        int count = 0;
        int index = -1;
        for (int i = 0; i < haystack.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(count)) {
                if (count == 0) {
                    index = i;
                }
                count += 1;
            }
            else {
                index = -1;
                count = 0;
            }
            if (count == needle.length()) {
                break;
            }
        }
        return index;
    }
    // HashMaps
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> data = new HashMap<>();
        for(int i = 0; i < magazine.length(); i++) {
            char c = magazine.charAt(i);
            if (data.get(c) == null) {
                data.put(c, 1);
                //System.out.println(data.get(c));
            }
            else {
                data.put(c, data.get(c) + 1);
            }
        }
        for (int j = 0; j < ransomNote.length(); j++) {
            char c = ransomNote.charAt(j);
            if(data.get(c) == null) {
                return false;
            }
            else {
                if (data.get(c) > 0) {
                    data.put(c, data.get(c) - 1);
                    continue;
                }
                else {
                    return false;
                }
            }
        }
        //data.forEach((key, value) -> System.out.println(key + " : " + value));
        return true;
    }
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Integer> data1 = new HashMap<>();
        HashMap<Character, Integer> data2 = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            char letter1 = s.charAt(i);
            char letter2 = t.charAt(i);
            if (data1.get(letter1) == null) {
                data1.put(letter1, 1);
            }
            else {
                data1.put(letter1, data1.get(letter1) + 1);
            }
            if (data2.get(letter2) == null) {
                data2.put(letter2, 1);
            }
            else {
                data2.put(letter2, data2.get(letter2) + 1);
            }
        }
        for (int j = 0; j < s.length(); j++) {
            char letter1 = s.charAt(j);
            char letter2 = t.charAt(j);
            if (data1.get(letter1) != data2.get(letter2)) {
                return false;
            }
        }
        return true;
    }
    public boolean wordPattern(String pattern, String s) {
        String word = "";
        int count = 0;
        HashMap<Character, String> data = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == ' ' || i == s.length() - 1) {
                if(i == s.length() - 1) {
                    word += s.charAt(i);
                }
                if (data.get(pattern.charAt(count)) == null) {
                    for(Map.Entry<Character, String> entry : data.entrySet()) {
                        if (entry.getValue().equals(word) && entry.getKey() != pattern.charAt(count)) {
                            return false;
                        }
                    }
                    data.put(pattern.charAt(count), word);
                    count += 1;
                    word = "";
                }
                else {
                    for(Map.Entry<Character, String> entry : data.entrySet()) {
                        if (entry.getValue().equals(word) && entry.getKey() != pattern.charAt(count)) {
                            return false;
                        }
                    }
                    if(!data.get(pattern.charAt(count)).equals(word)) {
                        return false;
                    }
                    else {
               count += 1;
                        word = "";
                    }
                }
            }
            else {
                word += s.charAt(i);
            }
        }
        for(int j = 0; j < pattern.length(); j++) {
            word += data.get(pattern.charAt(j));
            if(j == pattern.length() - 1) {
                break;
            }
            word += ' ';
        }
        if (!word.equals(s)) {
            return false;
        }
        return true;
    }
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> data = new HashMap<>();
        for(int i = 0; i < s.length(); i ++) {
            char c = s.charAt(i);
            if (data.get(c) == null) {
                data.put(c,1);
            }
            else {
                data.put(c, data.get(c) + 1);
            }
        }
        for(int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            if (data.get(c) == null) {
                return false;
            }
            else {
                data.put(c, data.get(c) - 1);
            }
        }
        for(Integer value : data.values()) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    } 
    public List<List<String>> groupAnagrams(String[] strs) {
	List<String> arrayNext = new ArrayList<String>();
	for(int i = 0; i < strs.length; i++) {
		arrayNext.add(strs[i]);
	}
	List<List<String>> arrayFinal = new ArrayList<>();
	while(arrayNext.size() > 0) {
		List<String> currentFinal = new ArrayList<String>();
		List<String> currentNext = new ArrayList<String>();
		for (String word : arrayNext) {
			HashMap<Character, Integer> data = new HashMap<>();
			String firstWord = arrayNext.get(0);
			for(int i = 0; i < firstWord.length(); i++) {
				char letter = firstWord.charAt(i);
				if (data.get(letter) == null) {
					data.put(letter, 1);
				}
				else { 
					data.put(letter, data.get(letter) + 1);
				}
			}	
			boolean cancel = false;
			for (int j = 0; j < word.length(); j++) {
				char letter = word.charAt(j);
				if(data.get(letter) == null) {
					cancel = true;
					break;
				}
				else {
					data.put(letter, data.get(letter) - 1);
				}
			}
			for (Integer value : data.values()) {
				if(value != 0) {
					cancel = true;
					break;
				}
			}
			if(cancel) {
				currentNext.add(word);
			}
			else {
				currentFinal.add(word);
			}
		}
		arrayFinal.add(currentFinal);
		arrayNext = currentNext;
	}
	return arrayFinal;				
    }
    public int[] twoSum(int[] nums, int target) {
	    int solution[] = new int[2];
	    for(int i = 0; i < nums.length - 1; i++) {
		    for(int j = i + 1; j < nums.length; j++) {
			    if(nums[i] + nums[j] == target) {
				    solution[0] = i;
				    solution[1] = j;
				    break;
			    }
			}
		    if(solution[0] != 0 && solution[1] != 0) {
			   break;
		    }
	    }
	    return solution;
    }
    public boolean isHappy(int n) {
	    HashMap<Integer, Integer> data = new HashMap<>();
	    while(n != 1) {
		    String word = String.valueOf(n);
		    int[] array = new int[word.length()];
		    int total = 0;
		    for(int i = 0; i < word.length(); i++) {
			    char letter = word.charAt(i);
			    int number = letter - '0';
			    array[i] = number;
		    }
		    for(int num : array) {
			    total += num * num;
		    }
		    if(data.get(total) == null) {
			    data.put(total,1);
		    }
		    else{
			    data.put(total, data.get(total) + 1);
		    }
		    if(data.get(total) > 1) {
			    return false;
		    }
		    n = total;
	    }
	    return true;
    }
    public boolean isHappyRecursion(int n, HashMap<Integer, Integer> data) {
	if(n == 1) {
		return true;
	}
	String word = String.valueOf(n);
	int[] array = new int[word.length()];
	int total = 0;
	for(int i = 0; i < word.length(); i++) {
		char letter = word.charAt(i);
		int number = letter - '0';
		array[i] = number;
	}
	for(int num : array) {
		total += num * num;
	}
	
    	if(data.get(total) == null) {
    		data.put(total,1);
	}
		    	
    	else{
	    data.put(total, data.get(total) + 1);
	}

    	if(data.get(total) > 1) {
	    return false;
	}
	n = total;
	return this.isHappyRecursion(n, data);
    }
    public boolean containsNearbyDuplicates(int[] nums, int k) {
	    HashMap<Integer, Integer> data = new HashMap<>();
	    for(int i = 0; i < nums.length; i++) {
		    if(data.get(nums[i]) == null) {
			    data.put(nums[i], i);
		    }
		    else{
			    int num = Math.abs(data.get(nums[i]) - i);
			    if(num <= k) {
				    return true;
			    }
			    else{
				    data.put(nums[i], i);
			    }
		    }
	    }
	    return false;
    }
    public int longestConsecutive2(int[] nums) {
	    HashMap<Integer, Boolean> data = new HashMap<>();
	    int[] minArray = new int[nums.length];
	    int minNumber = 0;
	    int matches = 0;
	    int count = 1;
	    for (int num : nums) {
		    data.put(num,false);
	    }
	    for (int num : nums) {
		    if (data.get(num + 1) != null || data.get(num - 1) != null) {
			    data.put(num, true);
		    }
	    }
	    for (int key : data.keySet()) {
		    if (data.get(key) && data.get(key - 1) == null) {
			    minArray[minNumber] = key;
			    minNumber += 1;
		    }
		    else if (data.get(key)) {
			    matches += 1;
		    }
	    }
	    int[] countArray = new int[minNumber];
	    if (minNumber > 0) {
		    int index = 0;
		    for (int i = 0; i < matches + minNumber; i++) {
			    if (data.get(minArray[index] + count) != null) {
				    count += 1;
				    if (i == matches + minNumber - 1) {
					    countArray[index] = count;
				    }
			    }
			    else {
				    countArray[index] = count;
				    count = 1;
				    if (index < minNumber) {
					    index += 1;
				    }
				    else {
					    break;
				    }
			    }
		    }
		    int max = countArray[0];
		    for (int num : countArray) {
			    if (num > max) {
				    max = num;
			    }
		    }
		    return max;
	    }
	    else {
		    return 1;
	    }


		    
			    
    }
    public boolean isPalindrome(String s) {
	    HashMap<Character, Character> data = new HashMap<>();
	    String word = "";
	    for (int i = 65; i < 91; i++) {
		    data.put((char) i, (char)(i + 32));
	    }
	    for (int i = 0; i < s.length(); i++) {
		    if ( (int) s.charAt(i) >= 48 && (int) s.charAt(i) <= 57) {
			    word += s.charAt(i);
		    }
		    else if ( (int) s.charAt(i) >= 65 && (int) s.charAt(i) <= 90) {
			    word += data.get(s.charAt(i));
		    }
		    else if ( (int) s.charAt(i) >= 97 && (int) s.charAt(i) <= 122) {
			    word += s.charAt(i);
		    }
		    else {
			    continue;
		    }
	    }
	    for (int i = 0; i < word.length(); i++) {
		    if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
			    return false;
		    }
	    }
	    return true;

		     
			   

		    
    }
    public boolean isSubsequence(String s, String t) {
	    int iterator = 0;
	    for (int i = 0; i < t.length(); i++) {
		    if (s.charAt(iterator) == t.charAt(i)) {
			    iterator += 1;
		    }
	    }
	    if (iterator != s.length()) {
		   return false;
	    }
	    return true; 
    }
    public int[] twoSumII(int[] numbers, int target) {
	    int index = 0;
	    int sum = 0;
	    int[] result = new int[2];
	    for (int i = numbers.length; i > 0; i--) {
		    if (target >= numbers[i-1]) {
			    index = i + 1;
			    break;
		    }
	    }
	    if (index == 2) {
		    result[0] = 1;
		    result[1] = 2;
	    }
	    else {
		    for (int i = 1; i < index; i++) {
			    for (int j = i + 1; j < index; j++) {
				    sum = numbers[i-1] + numbers[j-1];
				    if (sum == target) {
					    result[0] = i;
					    result[1] = j;
				    }
			    }
		    }
	    }
	    return result;
    }
    public int maxArea(int[] height) {
	    int area = 1;
	    int maxHeight;
	    int length;
	    int product;
	    for(int i = 0; i < height.length; i++) {
		    for(int j = height.length-1; j > i; j--) {
			    if(height[j] > height[i]) {
				    maxHeight = height[i];
			    }
			    else {
				    maxHeight = height[j];
			    }
			    length = j - i;
			    product = maxHeight * length;
			    if (product > area) {
				    area = product;
			    }
		    }
	    }
	    return area;
    }
    public List<int[]> threeSum(int[] nums) {
	    List<int[]> result = new ArrayList<int[]>();
	    int count = 0;
	    boolean skip = false;
	    boolean zero = false;
	    for (int i = 0; i < nums.length - 2; i++) {
		    for (int j = i + 1; j < nums.length - 1; j++) {
			    int[] next = new int[3];
			    for (int k = j + 1; k < nums.length; k++) {
				  if (nums[i] + nums[j] + nums[k] == 0) {
					if (nums[i] == 0 && nums[j] == 0 && nums[k] ==0) {
						zero = true;
						continue;
					}
					if (count > 0) {
						HashMap<Integer, Boolean> data = new HashMap<>();
						data.put(nums[i], true);
						data.put(nums[j], true);
						data.put(nums[k], true);
						for(int[] array : result) {
							System.out.println("It works");
							int stop = 0;
							if(data.get(array[0]) != null) {
								stop += 1;
							}
							if(data.get(array[1]) != null) {
								stop += 1;
							}
							if(data.get(array[2]) != null) {
								stop += 1;
							}
							if(stop == 3) {
								skip = true;
								System.out.print("stop");
								break;
							}
						}
					}
					if(!skip) {
						next[0] = nums[i];
						next[2] = nums[k];
						result.add(next);
						count += 1;
					}
					skip = false;
				  }
			    }
		    }
	    }
	    if(zero) {
		    int[] zeroArray = new int[3];
		    result.add(zeroArray);
	    }
	    return result;
    }
    public List<int[]> threeSum2(int[] nums) {
	    List<int[]> result = new ArrayList<int[]>();
	    int count = 0;
	    boolean skip = false;
	    for(int i = 0; i < nums.length - 2; i++) {
		    for(int j = i + 1; j < nums.length - 1; j++) {
			    int[] next = new int[3];
			    for(int k = j + 1; k < nums.length; k++) {
				    if(nums[i] + nums[j] + nums[k] == 0) {
					    if(count > 0) {
						    for(int[] array : result) {
							    int stop = 0;
							    if(nums[i] == array[0] || nums[i] == array[1] ||  nums[i] == array[2]) {
								    stop += 1;
								    }
							    if(nums[j] == array[0] || nums[j] == array[1] ||  nums[j] == array[2]) {
								    stop += 1;
								    }
							    if(nums[k] == array[0] || nums[k] == array[1] ||  nums[k] == array[2]) {
								    stop += 1;
								    }
							    if(stop == 3) {
								    skip = true;
								    break;
							    }
						    }
					    }
					    if(!skip) {
						    next[0] = nums[i];
						    next[1] = nums[j];
						    next[2] = nums[k];
						    result.add(next);
						    count += 1;
					    }
					    skip = false;
				    }
			    }
		    }
	    }
	    return result;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	   ListNode current = l1;
	    String word = "";
	    while(current != null) {
		    word = (char)(current.val + '0') + word;
		    current = current.next;
	    }
	    int firstNum = Integer.parseInt(word);
	    word = "";
	    current = l2;
	    while(current != null) {
		    word = (char)(current.val + '0') + word;
		    current = current.next;
	    }
	    int secondNum = Integer.parseInt(word);
	    int sum = firstNum + secondNum;
	    word = String.valueOf(sum);
	    ListNode linkList = new ListNode();
	    for(int i = 0; i < word.length(); i++) {
		    if(i == 0) {
			    linkList.val = word.charAt(i) - '0';
		    }
		    else {
			    ListNode newNode = new ListNode(word.charAt(i) - '0', linkList);
			    linkList = newNode;
		    }
	    }
	    return linkList;
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
	    ListNode current1 = list1;
	    ListNode current2 = list2;
	    ListNode newHead = new ListNode();
	    if (current1 == null || current2 == null) {
		    if (current2 != null) {
			    return list2;
		    }
	    }
	    else {
		    if (current2.val < current1.val) {
			    newHead = current2;
			    System.out.print("Have a new head to list");
			    while (current2.next != null && current2.next.val < current1.val) {
				    current2 = current2.next;
			    }
			    ListNode head2 = current2.next;
			    current2.next = current1;
			    current2 = head2;
		    }
		    while (current1.next != null) {
			    while (current2 != null && current2.val <= current1.next.val) {
				    ListNode head1 = current1.next;
				    ListNode head2 = current2.next;
				    current1.next = current2;
				    current2.next = head1;
				    current2 = head2;
				    System.out.println("In the main loop");
			    }
			    System.out.println("In the outer of the main loop");
			    current1 = current1.next;
		    }
		    if (current2 != null && current2.val > current1.val) {
			    current1.next = current2;
		    }
	    }
	    if (newHead.next != null) {
		    return newHead;
	    }
	    return list1;
    }
    public RandomNode copyRandomList(RandomNode head) {
	    int length = 1;
	    RandomNode current = head;
	    while (current != null) {
		    length += 1;
		    current = current.next;
	    }
	    current = head;
	    RandomNode[] nodeArray = new RandomNode[length];
	    int[] indexArray = new int[length];
	    int index = 0;
	    while (current != null) {
		    RandomNode node = new RandomNode(current.val);
		    nodeArray[index] = node;
		    RandomNode current2 = head;
		    int count = 0;
		    if (current.next == null) {
			    nodeArray[index + 1] = null;
		    }
		    while (current2 != null) {
			    if (current2 == current.random) {
				    indexArray[index] = count;
				    break;
			    }
			    count += 1;
			    if (current2.next == null) {
				    indexArray[index] = count;
			    }
			    current2 = current2.next;
		    }
		    current = current.next;
		    index += 1;
	    }
	    for (int i = 0; i < nodeArray.length - 1; i++) {
		    nodeArray[i].next = nodeArray[i+1];
		    nodeArray[i].random = nodeArray[indexArray[i]];
	    }
	    return nodeArray[0];
    }
    public ListNode reverseBetween(ListNode head, int left, int right) {
	    int[] array = new int[right-left+1];
	    int position = 1;
	    ListNode current = head;
	    int index = array.length - 1;
	    while(current != null) {
		    if(position >= left && position <= right) {
			    array[index] = current.val;
			    index -= 1;
		    }
		    position += 1;
		    current = current.next;
	    }
	    position = 1;
	    index = 0;
	    current = head;
	    while(current != null) {
		    if(position >= left && position <= right) {
			    current.val = array[index];
			    index += 1;
		    }
		    position += 1;
		    current = current.next;
	    }
	    return head;
    }
    public ListNode reverseBetween2(ListNode head, int left, int right) {
	    ListNode current = head;
	    int position = 1;
	    int index = right - left;
	    ListNode current2;
	    ListNode leftNode = new ListNode(0);
	    while(current != null) {
		    if(position >= left && position <= right) {
			    if(position == left) {
				    leftNode.val = current.val;
				    leftNode.next = current.next;
			    }
			    int count = index;
			    current2 = leftNode;
			    System.out.printf("current2 val = %d \n", current2.val);
			    while(count > 0) {
				    current2 = current2.next;
				    count -= 1;
			    }
			    current.val = current2.val;
			    index -= 1;
		    }
		    position += 1;
		    current = current.next;
	    }
	    return head;
    }
    public ListNode reverseKGroup(ListNode root) {
        return root;
    }
    //Binary Trees
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int lDepth = maxDepth(root.left);
        int rDepth = maxDepth(root.right);
        if (lDepth >= rDepth) {
            return lDepth + 1;
        }
        else {
            return rDepth + 1;
        }
    }
    public int maxDepth2(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int depth = 0;
        ArrayList <TreeNode> q = new ArrayList<TreeNode>();
        q.add(root);
        q.add(null);
        while (!q.isEmpty()) {
            TreeNode curr = q.remove(0);
            if (curr == null) {
                depth += 1;
                if (!q.isEmpty()) {
                    q.add(null);
                }
            }
            else {
                if (curr.left != null) {
                    q.add(curr.left);
                }
                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
        }
        return depth;
    }
    public int maxDepth3(TreeNode root) {
        if (root == null) {
            return 0;
        }
        ArrayList<TreeNode> q = new ArrayList<TreeNode>();
        q.add(root);
        int h = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode temp = q.remove(0);
                if (temp.left != null) {
                    q.add(temp.left);
                }
                if (temp.right != null) {
                    q.add(temp.right);
                }
            }
            h += 1;
        }
        return h;
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p.val != q.val) {
            return false;
        }
        ArrayList<TreeNode> arrayP = new ArrayList<TreeNode>();
        ArrayList<TreeNode> arrayQ = new ArrayList<TreeNode>();
        arrayP.add(p);
        arrayQ.add(q);
        while (!arrayP.isEmpty()) {
            TreeNode nodeP = arrayP.remove(0);
            TreeNode nodeQ = arrayQ.remove(0);
            if (nodeP.left == null) {
                if (nodeQ.left != null) {
                    System.out.println("1st");
                    return false;
                }
            }
            else {
                if (nodeQ.left == null) {
                    System.out.println("2nd");
                    return false;
                }
                else if (nodeQ.left.val != nodeP.left.val) {
                    System.out.println("3rd");
                    return false;
                }
                else {
                    arrayP.add(nodeP.left);
                    arrayQ.add(nodeQ.left);
                }
            }
            if (nodeP.right == null) {
                if (nodeQ.right != null) {
                    System.out.println("4th");
                    return false;
                }
            }
            else {
                if (nodeQ.right == null) {
                    System.out.println("5th");
                    return false;
                }
                else if (nodeQ.right.val != nodeP.right.val) {
                    System.out.println("6th");
                    return false;
                }
                else {
                    arrayP.add(nodeP.right);
                    arrayQ.add(nodeQ.right);
                }
            }
        }
        return true;
    }
    





		    


			     
			    





}

							

							
				
				  
			    
		    
	    
	   
    

    
    


					



			    


    


		     



	





