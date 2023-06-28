#class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Khởi tạo biến tổng và con trỏ cho danh sách liên kết kết quả
        total = 0
        curr = result = ListNode(0)
        
        # Duyệt qua danh sách liên kết l1 và l2
        while l1 or l2 or total:
            # Cộng giá trị của nút đang xét vào tổng
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            # Tạo một nút mới với giá trị là tổng mod 10,
            # và cập nhật con trỏ của danh sách liên kết kết quả
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Cập nhật tổng, lặp lại quá trình cho đến khi hết nút cần duyệt
            total //= 10
        
        # Trả về danh sách liên kết kết quả từ phần tử thứ hai (phần tử đầu tiên là 0)
        return result.next
