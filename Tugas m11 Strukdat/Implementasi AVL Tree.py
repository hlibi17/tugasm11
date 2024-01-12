class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def preOrderTraversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)


# Contoh penggunaan AVL Tree
avl_tree = AVLTree()
root = None

keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys:
    root = avl_tree.insert(root, key)

print("Preorder Traversal of AVL Tree:")
avl_tree.preOrderTraversal(root)
