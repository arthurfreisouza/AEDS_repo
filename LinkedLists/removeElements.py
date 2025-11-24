from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(val+1) # Adding the dummy node in the case if is necessary
        dummy.next=head
        head=dummy
        prev=None
        current=head
        while current:
            if current.val==val:
                prev.next=current.next
            else:
                prev=current
            current=current.next
        head=head.next # Removing the dummy node
        return head
               
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
    val=int(input("Type here a val: "))
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.removeElements(head=head,val=val)
    print_linked_list(head=head_result)