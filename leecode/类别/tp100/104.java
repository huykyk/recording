
/**
*
104. Maximum Depth of Binary Tree
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*/
//java怎么写
 
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        else return Math.max(maxDepth(root.left),maxDepth(root.right))+1;
    }
}




/* //c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)  return 0;
        else return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};


/*