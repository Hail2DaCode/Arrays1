import java.util.HashMap;
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
}