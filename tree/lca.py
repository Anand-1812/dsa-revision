class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      if root == None or root == p or root == q:
        return root
      
      left = self.lowestCommonAncestor(root.left, p, q)
      right = self.lowestCommonAncestor(root.right, p, q)

      if left is None:
        return right
      elif right is None:
        return left
      else:
        return root

