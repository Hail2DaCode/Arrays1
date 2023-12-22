import java.util.ArrayList;

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
        int[] nums = {1,1,2};
        System.out.println(String.format("k is %d", solution.removeDuplicates(nums)));
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
        int[] nums2 = {1,1,1,2,2,3};
        System.out.println(String.format("k is %d", solution.removeDuplicatesMedium(nums2)));
        for (int i = 0; i < nums2.length; i++) {
            System.out.println(nums2[i]);
        }
        int[] nums3 = {0,0,1,1,1,2,3,3};
        System.out.println(String.format("k is %d", solution.removeDuplicatesMedium(nums3)));
        for (int i = 0; i < nums3.length; i++) {
            System.out.println(nums3[i]);
        }
}
}