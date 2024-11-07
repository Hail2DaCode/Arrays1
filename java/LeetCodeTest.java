import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
public class LeetCodeTest {
    public static void main(String[] args) {
        Solution solution = new Solution();
		TreeNode node1 = new TreeNode(1);
		TreeNode node2 = new TreeNode(2);
		node1.left = node2;
		TreeNode node4 = new TreeNode(1);
		TreeNode node5 = new TreeNode(2);
		//TreeNode node6 = new TreeNode(3);
		//node4.left = node5;
		node4.right = node5;
		//node6.right = node2;
		boolean result1 = solution.isSameTree(node1, node4);
		System.out.println(result1);
    }
}

