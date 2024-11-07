import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
public class LeetCodeTest {
    public static void main(String[] args) {
        Solution solution = new Solution();
		TreeNode node1 = new TreeNode(4);
		TreeNode node2 = new TreeNode(2);
		TreeNode node3 = new TreeNode(7);
		TreeNode node4 = new TreeNode(1);
		TreeNode node5 = new TreeNode(3);
		TreeNode node6 = new TreeNode(6);
		TreeNode node7 = new TreeNode(9);
		node1.left = node2;
		node1.right = node3;
		node2.left = node4;
		node2.right = node5;
		node3.left = node6;
		node3.right = node7;
		//TreeNode result1 = solution.invertTree(node1);
		ArrayList<TreeNode> test = new ArrayList<TreeNode>();
		test.add(node1);
		while (!test.isEmpty()) {
			TreeNode node = test.remove(0);
			System.out.print(node.val);
			if (node.left != null) {
				test.add(node.left);
			}
			if (node.right != null) {
				test.add(node.right);
			}
		}
    }
}

