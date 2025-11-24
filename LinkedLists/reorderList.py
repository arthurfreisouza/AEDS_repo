from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1 verifying if the list has a unique value or is empty.
        if not head or not head.next:
            return None

        # 2 finding the middle of the linked list.
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        slow.next=None # Separating the 2 linked lists

        # 3 reverting the linked list
        prev=None
        current=head2 # Will contain the middle of the linked list
        while current:
            aux_temp=current.next
            current.next=prev
            prev=current
            current=aux_temp
        head2=prev

        # 4 merging the linked lists together
        first = head
        second = head2
        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head
def print_linked_list(head):
    if not head:
        return None
    result=[]
    curr=head
    while curr:
        result.append(str(curr.val))
        curr=curr.next
    print('->'.join(result))

if __name__=="__main__":
    my_lst=[]
    while True:
        num=int(input("Type here a number value: "))
        if num==400:
            break
        my_lst.append(num)
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.reorderList(head=head)
    print_linked_list(head=head_result)