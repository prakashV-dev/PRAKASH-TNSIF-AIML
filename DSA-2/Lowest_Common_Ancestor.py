class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

root = TreeNode(3)
p = TreeNode(5)
q = TreeNode(1)
root.left = p
root.right = q

lca = lowest_common_ancestor(root, p, q)
print(lca.val)
