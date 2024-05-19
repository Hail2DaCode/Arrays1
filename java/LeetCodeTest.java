import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

public class LeetCodeTest {
    public static void main(String[] args) {
        /* LeetCode leetCodeApp = new LeetCode();
        ListNode head1 = new ListNode(1);
        head1.addNode(head1, 2);
        head1.addNode(head1, 4);
        //head1.addFront(head1, 3);
        //ListNode.display(head1.addFront(head1,0));
        ListNode.display(head1);
        ListNode head2 = new ListNode(0);
        head2.addNode(head2, 0).addNode(head2, 0);
        ListNode.display(head2);
        //ListNode merged = new ListNode();
        ListNode.mergeTwoLists(head1, head2);
        Solution solution = new Solution();
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int[] nums3 = {1};
        int[] nums4 = {};
        int[] nums5 = {0};
        int[] nums6 = {1};
        int[] nums7 = {3,2,2,3};
        solution.merge(nums1,3,nums2,3);
        solution.merge(nums3,1,nums4,0);
        solution.merge(nums5,0,nums6,1); */
        Solution solution = new Solution();
	int[] arr1 = {-1,0,1,2,-1,-4};
	int[] arr2 = {0,1,1};
	int[] arr3 = {0,0,0};
	int[] arr4 = {-2,0,2,0,4,-4,2,-2,4,4,-4,6,0};
	List<int[]> result1 = solution.threeSum(arr1);
	List<int[]> result2 = solution.threeSum(arr2);
	List<int[]> result3 = solution.threeSum(arr3);
	List<int[]> result4 = solution.threeSum(arr4);
	System.out.println(result1);
	for(int[] arr : result1) {
		System.out.printf("result1: %d, %d, %d", arr[0], arr[1], arr[2]);
		System.out.print("\n");
	}
	for(int[] arr : result2) {
		System.out.printf("result2: %d, %d, %d", arr[0], arr[1], arr[2]);
		System.out.print("\n");
	}
	for(int[] arr : result3) {
		System.out.printf("result3: %d, %d, %d", arr[0], arr[1], arr[2]);
		System.out.print("\n");
	}
	for(int[] arr : result4) {
		System.out.printf("result4: %d, %d, %d", arr[0], arr[1], arr[2]);
		System.out.print("\n");
	}

		





	}
    }
