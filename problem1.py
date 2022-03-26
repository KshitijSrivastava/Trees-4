

class Solution:

    """ 1st method
    Time Complexity: O(N) where n is the number of nodes
    Space Complexity: O(h) fucntion frames 
    where h is the height of binary tree
    """
    
    def kthSmallest_recur(self, root, k):
        #print(root.val, k)
        
        #go to the left of node if it exists
        if root.left:
            self.kthSmallest_recur(root.left, k)
        
        #seen the first smallest element
        #decrement the count

        self.k += 1
        #if seen the kth smallest element, save it 
        if self.k == k:
            self.ans = root.val
            return
        
        #if root's right exists then go to that node
        if root.right:
            self.kthSmallest_recur(root.right, k)
    
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #nodes to keep track of the smallest nodes and answer
        self.k = 0
        self.ans = 0
        self.kthSmallest_recur(root, k)
        return self.ans

    """
    2nd method

    Time Complexity: O(N) where n is the number of nodes in tree
    Space Complexity: O(N) where n is the number of nodes in tree
    """


def inorder(self, root, sorted_arr):
    #keep adding the answer in the sorted order
        if root is None:
            return 
        
        self.inorder(root.left, sorted_arr)
        sorted_arr.append(root.val)
        self.inorder(root.right, sorted_arr)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_arr = []
        self.inorder(root, sorted_arr)
        #return the arra
        return sorted_arr[k-1]