class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def get_min(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.l)
            print(str(node.v))
            self._print_tree(node.r)

    def __str__(self):
        if self.root is not None:
            self._print_tree(self.root.l)
            print(str(self.root.v))
            self._print_tree(self.root.r)
        return ""

    def __iter__(self):
        current_level = [self]

        while len(current_level) > 0:
            next_level = []
            for node in current_level:
                yield node
                if node.root.l is not None and type(node) == Node:
                    next_level.append(node.root.l)
                if node.root.r is not None and type(node) == Node:
                    next_level.append(node.root.r)
            current_level = next_level


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
# print(tree)
# print(tree.find(3).v)
# print(tree.find(10))
# mas = []  --- I don't know why appending to the list doesn't work
for i in tree:
    print(i)
