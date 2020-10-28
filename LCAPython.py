class Node:

    def initialize(node, key):
        node.key = key
        node.left = None
        node.right = None


def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    leftLca = findLCA(root.left, n1, n2)
    rightLca = findLCA(root.right, n1, n2)

    if leftLca and rightLca:
        return root

    return leftLca if leftLca is not None else rightLca


    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)