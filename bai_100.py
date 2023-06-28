#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        # Nếu một trong hai cây rỗng hoặc giá trị của nút hiện tại khác nhau
        if not p or not q or p.val != q.val:
            return False
        
        # Kiểm tra cùng lúc cả cây con trái và cây con phải
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

