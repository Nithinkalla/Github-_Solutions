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
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        return mindepth(root);
    }
    public int mindepth(TreeNode root){
        if(root == null) return 0;
        int lefdep = mindepth(root.left);
        int rigdep = mindepth(root.right);
        if(root.left == null && root.right == null) return 1;
        if(root.left == null) return rigdep + 1;
        if(root.right == null) return lefdep + 1;
        return Math.min(lefdep,rigdep) + 1;
    }
}