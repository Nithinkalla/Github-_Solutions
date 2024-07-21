/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> lst = new ArrayList<>();
        Queue<TreeNode> que = new LinkedList<>();
        if(root == null) return lst;
        que.add(root);
        while(!que.isEmpty()){
            List<Integer> temp = new ArrayList<>();
            int x = que.size();
            for(int i = 0;i < x;i++){
                TreeNode node = que.poll();
                temp.add(node.val);
                if(node.left != null) que.add(node.left);
                if(node.right != null) que.add(node.right);
            }
            lst.add(temp);
        }
        Collections.reverse(lst);
        return lst;
    }
}