from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # This implementation is correct! No changes needed.
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        width = length // k
        remaining = length % k
        
        result = []
        current = head
        for i in range(k):
            part_head = current
            part_size = width + (1 if i < remaining else 0)
            
            # Traverse to the node just before the split
            for j in range(part_size - 1):
                if current:
                    current = current.next
            
            # Split the list
            if current:
                next_head = current.next
                current.next = None
                current = next_head
            
            result.append(part_head)
        return result

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]):
    if not head:
        print("None")
        return
    
    result_str = []
    curr = head
    while curr:
        result_str.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(result_str))

if __name__ == "__main__":
    my_lst = []
    print("Enter numbers for the list. Type 400 to finish.")
    while True:
        try:
            num = int(input("Type here a number value: "))
            if num == 400:
                break
            my_lst.append(num)
        except ValueError:
            print("Please enter a valid integer.")
            
    k = int(input("Type here a value for k: "))
    
    head = build_linked_list(values=my_lst)
    print("\nOriginal List:")
    print_linked_list(head=head)
    
    sol = Solution()
    result = sol.splitListToParts(head=head, k=k)
    
    # SUGGESTION 1: Print the results in a more readable way.
    print("\n--- Split Lists ---")
    for i, part_head in enumerate(result):
        print(f"Part {i+1}: ", end="")
        print_linked_list(head=part_head)