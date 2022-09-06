'''
@@@@@@ Traverse a Tree @@@@@@

Pre-Order
Visit the root - Traverse Left Subtree - Traverse Right Subtree

In-Order
Traverse Left Subtree - Visit the root - Traverse Right Subtree

Post-Order
Traverse Left Subtree - Traverse Right Subtree - Visit the root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Binary Tree Pre-order Traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node):
            if node.left:
                result.append(node.left.val)
                traversal(node.left)
            if node.right:
                result.append(node.right.val)
                traversal(node.right)

        result = []
        if root is None:
            return result
        node = root
        result.append(node.val)
        if node.left or node.right:
            traversal(node)

        return result

# Binary Tree Pre-order Traversal (better)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(root):
            if root is None:
                return None
            output.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return output

# Binary Tree In-order Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #traverse left - visit root - traverse right
        def traversal(root):
            if root.left:
                traversal(root.left)
                result.append(root.val)
            else:
                result.append(root.val)
            if root.right:
                traversal(root.right)

        result = []
        if root is None:
            return result

        traversal(root)

        return result

# Binary Tree In-order Traversal (little bit better)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:       
        res = []       
        def in_order_search(res,node):           
            if not node:
                return
            in_order_search(res,node.left)
            res.append(node.val)
            in_order_search(res,node.right)    
            return
        
        in_order_search(res,root)
        
        return res

# Binary Tree Post-order Traversal
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #traverse left - traverse right - visit root
        result = []
        def dfs(root):
            if root is None:
                return None      
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
            
        dfs(root)
        return result

# Binary Tree Level-Order Traversal
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        result= []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                elem = queue.popleft()
                level.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            result.append(level)
        return result

'''
@@@@@@ Solve Problems Recursively @@@@@@

Top-down Solution
"Top-down" means that in each recursive call, 
visit the node - come up with some values - pass these values to its children
can be considered as a kind of "preorder" traversal

1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans


Bottom-up Solution

In each recursive call, 
Firstly call the function recursively for all the children nodes -
come up with the answer according to the returned values and the value of the current node itself.
can be regarded as a kind of postorder traversal.

1. return specific value for null node
2. left_ans = bottom_up(root.left)      // call function recursively for left child
3. right_ans = bottom_up(root.right)    // call function recursively for right child
4. return answers                       // answer <-- left_ans, right_ans, root.val
'''

# Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        if root == None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1

# Maximum Depth of Binary Tree (better)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))

#Symmetric Tree
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            a = self.check(left.left, right.right)
            b = self.check(left.right, right.left)
            return a and b

#Symmetric Tree (Iterative)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = collections.deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True

#Path Sum
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

'''
@@@@@@ Conclusion @@@@@@

When you meet a tree problem, ask yourself two questions: 
Can you determine some parameters to help the node know its answer? 
Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children? 

If the answers are both yes, 
try to solve this problem using a "top-down" recursive solution.

Or, you can think of the problem in this way: 
for a node in a tree, if you know the answer of its children, 
can you calculate the answer of that node? 

If the answer is yes, 
solving the problem recursively using a bottom up approach might be a good idea.
'''

# Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root = TreeNode(postorder.pop(), None, None)
            root_index = inorder.index(root.val)
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root

# Construct Binary Tree from Preorder and Inorder Traversal
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        def helper(preorder, inorder):
            if inorder:
                root = TreeNode(preorder.popleft(), None, None)
                idx = inorder.index(root.val)
                root.left = helper(preorder, inorder[:idx])
                root.right = helper(preorder, inorder[idx+1:])

                return root

        preorder = deque(preorder)
        return helper(preorder, inorder)

# Construct Binary Tree from Preorder and Inorder Traversal (another : need to study)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_mapping = { num : i for i, num in enumerate(inorder) }
        index = 0
        
        def dfs(min_index, max_index):
            nonlocal index, inorder_mapping
            if index >= len(preorder):
                return None
            inorder_index = inorder_mapping[preorder[index]]
            if inorder_index < min_index or max_index < inorder_index:
                return None
            
            curr_node = TreeNode(preorder[index])
            index += 1
            curr_node.left = dfs(min_index, inorder_index)
            curr_node.right = dfs(inorder_index, max_index)
            
            return curr_node
        return dfs(-1, len(preorder))

# Populating Next Right Pointers in Each Node (compatible with 2)
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                elem = queue.popleft()
                level.append(elem)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            for i in range(len(level)):
                try:
                    level[i].next = level[i+1]
                except:
                    pass
        return root

# Populating Next Right Pointers in Each Node (better) [need to study]
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, next = root, root.left if root else None
        while cur and next:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = next
                next = cur.left
        return root

# Lowest Common Ancestor of a binary tree
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root
        return right or left

# Serialize and Deserialize Binary Tree