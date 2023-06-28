#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        tail = dummy_head

        # Duyệt hai danh sách
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Ghép nối danh sách còn lại
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        # Bỏ qua node giả và trả về phần đầu của danh sách mới
        return dummy_head.next
# @lc code=end

