# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}

        for i in range(len(inorder)):
            index[inorder[i]] = i

        pre_idx = [0]

        def build(left,right):
            if left > right:
                return None

            root_val = preorder[pre_idx[0]]
            pre_idx[0] +=1

            root = TreeNode(root_val)

            mid = index[root_val]

            root.left = build(left,mid - 1)
            root.right = build(mid + 1,right)

            return root
        return build(0,len(inorder)-1)


