# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iterator_=head
        count+=1
        while iterator_.next:
            count+=1
            iterator_=iterator_.next
        if count%2 !=0:
            middle=(iterator_+1)//2
        else:
            middle=iterator_//2
        iterator_=head
        lst_=[]
        count2=0
        while iterator_.next:
            if count2>=middle:
                lst_.append(iterator_.value)
        return lst_
if __name__=="__main__":
    head=input("Type here a value for the head node: ")
    sol=Solution()
    result=sol.middleNode(head=head)