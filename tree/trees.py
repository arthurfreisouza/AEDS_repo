from collections import deque

# ----------------------------------------------------------------------
# 1. SETUP: TREENODE CLASS AND EXAMPLE TREE
# ----------------------------------------------------------------------

class TreeNode:
    """A simple TreeNode class for a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        # Helper for printing
        return f"TreeNode({self.val})"

def build_example_tree():
    """
    Builds the example tree:
          ('F')
         /     \
        ('B')   ('G')
       /   \       \
     ('A') ('D')     ('I')
           /   \
          ('C') ('E')
    """
    root = TreeNode('F')
    root.left = TreeNode('B')
    root.right = TreeNode('G')
    root.left.left = TreeNode('A')
    root.left.right = TreeNode('D')
    root.right.right = TreeNode('I')
    root.left.right.left = TreeNode('C')
    root.left.right.right = TreeNode('E')
    return root

# ----------------------------------------------------------------------
# 2. DEPTH-FIRST SEARCH (DFS) - RECURSIVE
# ----------------------------------------------------------------------
# These use a nested helper function to make the main function call
# cleaner (so you don't have to pass an empty list).

def dfs_pre_order_recursive(root):
    """DFS Pre-Order (Recursive): Root -> Left -> Right"""
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)  # Visit Root
        traverse(node.left)      # Go Left
        traverse(node.right)     # Go Right
    
    traverse(root)
    return result

def dfs_in_order_recursive(root):
    """DFS In-Order (Recursive): Left -> Root -> Right"""
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # Go Left
        result.append(node.val)  # Visit Root
        traverse(node.right)     # Go Right
    
    traverse(root)
    return result

def dfs_post_order_recursive(root):
    """DFS Post-Order (Recursive): Left -> Right -> Root"""
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # Go Left
        traverse(node.right)     # Go Right
        result.append(node.val)  # Visit Root
    
    traverse(root)
    return result

# ----------------------------------------------------------------------
# 3. DEPTH-FIRST SEARCH (DFS) - ITERATIVE (Stack-based)
# ----------------------------------------------------------------------

def dfs_pre_order_iterative(root):
    """DFS Pre-Order (Iterative): Root -> Left -> Right"""
    if not root:
        return []
    
    stack = [root]  # Our stack for traversal
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)  # Visit Root
        
        # Push RIGHT child first, then LEFT.
        # This way, LEFT is processed next (LIFO).
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result

def dfs_in_order_iterative(root):
    """DFS In-Order (Iterative): Left -> Root -> Right"""
    stack = []
    result = []
    curr = root
    
    # Loop while we still have nodes to process OR stack is not empty
    while curr or stack:
        # 1. Go all the way left, pushing nodes onto the stack
        while curr:
            stack.append(curr)
            curr = curr.left
            
        # 2. Backtrack: curr is None. Pop, visit, and go right.
        curr = stack.pop()
        result.append(curr.val)  # Visit Root
        
        # 3. Move to the right child
        curr = curr.right
        
    return result

def dfs_post_order_iterative(root):
    """DFS Post-Order (Iterative): Left -> Right -> Root"""
    # This clever method is a modified Pre-Order (Root->Right->Left)
    # and then the result is reversed.
    if not root:
        return []
        
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val) # Add root
        
        # Push LEFT first, then RIGHT
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    # Reversing the (Root -> Right -> Left) traversal
    # gives (Left -> Right -> Root)
    return result[::-1]

# ----------------------------------------------------------------------
# 4. BREADTH-FIRST SEARCH (BFS) - ITERATIVE (Queue-based)
# ----------------------------------------------------------------------

def bfs_level_order(root):
    """BFS (Level-Order): Visits all nodes in a single list."""
    if not root:
        return []
        
    queue = deque([root]) # Use a deque for an efficient O(1) popleft()
    result = []
    
    while queue:
        # Dequeue the node from the front
        node = queue.popleft()
        result.append(node.val) # Visit it
        
        # Enqueue its children (if they exist) to the back
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

def bfs_level_by_level(root):
    """BFS variation: Returns a list of lists, grouped by level."""
    if not root:
        return []
        
    queue = deque([root])
    result = []
    
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level = []
        
        # Process all nodes for this level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        # Add the completed level to the main result
        result.append(current_level)
        
    return result

# ----------------------------------------------------------------------
# 5. MAIN EXECUTION: RUN ALL TRAVERSALS
# ----------------------------------------------------------------------

if __name__ == "__main__":
    tree_root = build_example_tree()
    
    print("--- 🌳 Example Tree ---")
    print("      ('F')")
    print("     /     \\")
    print("    ('B')   ('G')")
    print("   /   \\       \\")
    print(" ('A') ('D')     ('I')")
    print("       /   \\")
    print("      ('C') ('E')")
    print("------------------------\n")
    
    print("--- 🚀 DEPTH-FIRST SEARCH (DFS) ---")
    
    print("\n[Recursive]")
    print("Pre-Order: ", dfs_pre_order_recursive(tree_root))
    print("In-Order:  ", dfs_in_order_recursive(tree_root))
    print("Post-Order:", dfs_post_order_recursive(tree_root))
    
    print("\n[Iterative]")
    print("Pre-Order: ", dfs_pre_order_iterative(tree_root))
    print("In-Order:  ", dfs_in_order_iterative(tree_root))
    print("Post-Order:", dfs_post_order_iterative(tree_root))
    
    print("\n--- ➡️ BREADTH-FIRST SEARCH (BFS) ---")
    print("Level-Order (Single List):", bfs_level_order(tree_root))
    print("Level-by-Level (Grouped): ", bfs_level_by_level(tree_root))