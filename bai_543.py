#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Hàm đệ quy để tính chiều cao của cây con với node == nút
        def height(node):
            if not node:
                return 0
            # Tính chiều cao bên trái và bên phải của cây con 
            left_height = height(node.left)
            right_height = height(node.right)

            # Tính toán chiều cao của cây con được gắn vào `node` hiện tại 
            # bằng cách lấy giá trị lớn nhất giữa chiều cao của cây con bên trái và cây con bên phải, sau đó cộng thêm 1 (đại diện cho `node` hiện tại).
            self.diameter = max(self.diameter, left_height + right_height)
            
            return max(left_height, right_height) + 1

        self.diameter = 0

        # Gọi hàm `height` để tính toán chiều cao của cây `root`. Khi thực hiện việc này, biến `diameter` sẽ được cập nhật bằng đường kính lớn nhất trong cây.
        height(root)
        
        return self.diameter


# @lc code=end

