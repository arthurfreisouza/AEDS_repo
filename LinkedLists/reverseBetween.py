from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        # Creating a dummy node to cover all the scenarios.
        dummy=ListNode(0,head)
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        
        curr=prev.next
        for i in range(right-left):
            aux_temp=curr.next
            curr.next=aux_temp.next
            aux_temp.next=prev.next
            prev.next=aux_temp
        return dummy.next

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
    left=int(input("Type here a value for left: "))
    right=int(input("Type here a value for right: "))
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.reverseBetween(head=head,left=left,right=right)
    print_linked_list(head=head_result)