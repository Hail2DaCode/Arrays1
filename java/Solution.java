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
}