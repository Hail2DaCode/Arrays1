import java.util.ArrayList;
public class LeetCode {
    // public int removeDuplicates(int[] nums) {
    //     for (int number: nums) {
    //         int copy = nums
    //     }
    // }
    
    public boolean checkTags(String word) {
        char[] myArray = new char[word.length()];
        word.getChars(0, word.length(), myArray, 0);
        //Tag coolTag = new Tag();
        for (int i = 0; i < myArray.length; i++) {
            if (myArray[i] == ' ' && myArray[i-1] != ',') {
                return false;
            }
        }
        ArrayList<Tag> listArray = new ArrayList<Tag>();
        String newString = "";
        for (int i = 0; i < myArray.length; i++) {
            newString += myArray[i];
            if (myArray[i] ==  ',' || i == myArray.length - 1) {
                newString = newString.replace(',' , ' ');
                newString = newString.trim();
                Tag newTag = new Tag(newString);
                listArray.add(newTag);
                newString = "";
                continue;
            }
            
        }
        return true;
    }
    //26. Remove Duplicates From Sorted Array
    public int removeDuplicates(int[] nums) {
        int k = nums.length;
        for(int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1]) {
                k = k -1;
                nums[i] = nums[i] * -1;
                int j = i;
                while(j < nums.length - 1) {
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j+1] = temp;
                j = j + 1;
            }
            }   
        }
        System.out.println(k);
        return k;
    }
    // 27. Remove Element
    public int removeElement(int[] nums, int val) {
        int k = nums.length;
        for(int i = nums.length - 1; i >= 0; i--) {
            if(nums[i] == val) {
                k -= 1;
                int j = i;
                while(j < nums.length - 1) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j+1] = temp;
                    j = j + 1;
                }
            }
        }
        System.out.println(k);
        return k;
    }
    //69. Sqrt(x)
    public int mySqrt(int x) {
        int a = 0;
        while(a * a < x) {
            a+=1;
            if(a * a > x) {
                a -= 1;
                break;
            }
        }
        System.out.println(a);
        return a;
    }
    //21. Merge Two Sorted Lists

    
}
