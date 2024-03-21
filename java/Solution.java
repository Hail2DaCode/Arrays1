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
}