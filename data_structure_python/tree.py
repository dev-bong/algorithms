class Node():
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree():
    def __init__(self):
        self.root = None

    def size(self):
        pass

    def depth(self):
        pass

    
class BinaryTree(Tree):
    def in_order_traversal(self, node): # 왼쪽 자식 - 자기 자손 - 오른쪽 자손
        if node.left_child:
            self.in_order_traversal(node.left_child)
        print(node.item, end=" ")
        if node.right_child:
            self.in_order_traversal(node.right_child)
    
    def pre_order_traversal(self, node): # 자기 자신 - 왼족 자손 - 오른쪽 자손
        print(node.item, end=" ")
        if node.left_child:
            self.pre_order_traversal(node.left_child)
        if node.right_child:
            self.pre_order_traversal(node.right_child)
    
    def post_order_traversal(self, node): # 왼쪽 자손 - 오른쪽 자손 - 자기 자신
        if node.left_child:
            self.post_order_traversal(node.left_child)
        if node.right_child:
            self.post_order_traversal(node.right_child)
        print(node.item, end=" ")
    
    def level_order_traversal(self, node): # level 순으로
        queue = [node]

        while queue:
            pop_node = queue.pop(0)
            print(pop_node.item, end=" ")

            if pop_node.left_child:
                queue.append(pop_node.left_child)
            if pop_node.right_child:
                queue.append(pop_node.right_child)


class BinarySearchTree(Tree):
    pass


if __name__ == "__main__":
    tr = BinaryTree()
    tr.root = Node(8)
    tr.root.left_child = Node(3)
    tr.root.right_child = Node(10)
    tr.root.left_child.left_child = Node(1)
    tr.root.left_child.right_child = Node(6)
    tr.root.left_child.right_child.left_child = Node(4)
    tr.root.left_child.right_child.right_child = Node(7)
    tr.root.right_child.right_child = Node(14)
    tr.root.right_child.right_child.left_child = Node(13)

    tr.in_order_traversal(tr.root)
    print("")
    tr.pre_order_traversal(tr.root)
    print("")
    tr.post_order_traversal(tr.root)
    print("")
    tr.level_order_traversal(tr.root)
    print("")