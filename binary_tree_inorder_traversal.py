# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is not None:
            output = Solution.inorderTraversal(self, root.left)
            output.append(root.val)
            output += Solution.inorderTraversal(self, root.right)
        return output


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None)))
    sol = Solution()
    print(sol.inorderTraversal(root))
