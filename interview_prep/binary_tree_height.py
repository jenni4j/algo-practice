class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       # this is a node of the tree , which contains info as data, left , right

def height(root):
    if root is None:
        return -1 
    else:
        return 1 + max(height(root.right), height(root.left))
    


# recursion review


# arr = [1,2,3]
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        # 1 + sum[2, 3]
        # 1 + 2 + sum[3]
        # 1 + 2 + 3
        return arr[0] + sum(arr[1:])
