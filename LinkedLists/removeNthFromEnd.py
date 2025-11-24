from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        
        # 1. First reversal
        prev = None
        current = head
        while current:
            aux_temp = current.next
            current.next = prev
            prev = current
            current = aux_temp
        rev_head = prev
        
        # 2. Remove the Nth node from the now reversed list
        dummy_node = ListNode(0)
        dummy_node.next = rev_head
        ptr = dummy_node
        for _ in range(n - 1):
            ptr = ptr.next
        
        # Bypass the node to be removed
        if ptr.next:
            ptr.next = ptr.next.next
        
        # 3. Second reversal to restore the order
        prev = None
        current = dummy_node.next  # Start from the head of the modified list
        while current:
            aux_temp = current.next
            current.next = prev
            prev = current
            current = aux_temp
            
        return prev

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
    n=int(input("Type here a value for N: "))
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.removeNthFromEnd(head=head,n=n)
    print_linked_list(head=head_result)


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
    n=int(input("Type here a value for N: "))
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.removeNthFromEnd(head=head,n=n)
    print_linked_list(head=head_result)