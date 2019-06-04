// easy
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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        // return t1 ? t1 : t2;
        if(t1==NULL and t2==NULL) return NULL;
        if(t1==NULL and t2!=NULL) return t2;
        if(t1!=NULL and t2==NULL) return t1;
        else{
            int tmp = t1->val+t2->val;
            // TreeNode* node(tmp);
            t1->val = tmp;
            t1->left = mergeTrees(t1->left, t2->left);
            t1->right = mergeTrees(t1->right, t2->right);
            return t1;
        }
    }
};
