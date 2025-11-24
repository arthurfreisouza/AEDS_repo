# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        iterator_1=list1.head
        iterator_2=list2.head
        while iterator_1.next and iterator_2.next:
            while iterator_1<=iterator_2:
                new_node=ListNode(iterator_1.value)
            while iterator_1>iterator_2:
                new_node=ListNode(iterator_2.value)

            new_node=ListNode()

# if __name__=="__main__":
#     head=input("Type here a value for the head node: ")
#     sol=Solution()
#     result=sol.middleNode(head=head)