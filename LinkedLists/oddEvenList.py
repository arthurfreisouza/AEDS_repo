from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        before=head
        ahead=head.next
        saved_ahead=ahead
        while ahead and ahead.next:
            # changing the even values:
            before.next=ahead.next
            before=before.next
            ahead.next=before.next
            ahead=ahead.next
        before.next=saved_ahead
        return head

def create_linked_list(values:list):
    if len(values)==0 or not values:
        return None
    head=ListNode(val=values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head

def print_linked_list(head: ListNode):
    if not head:
        return None
    lst_nodes=[]
    curr=head
    while curr:
        lst_nodes.append(str(curr.val))
        curr=curr.next
    print('->'.join(lst_nodes))
    
if __name__=="__main__":
    list_values=[1,2,3,4,5]
    head=create_linked_list(values=list_values)
    # print_linked_list(head=head)
    sol=Solution()
    result=sol.oddEvenList(head=head)
    print_linked_list(head=head)