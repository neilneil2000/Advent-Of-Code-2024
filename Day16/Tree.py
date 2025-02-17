from dataclasses import dataclass, field


@dataclass
class Node:
    value: object
    parents: list["Node"] = field(default_factory=list)
    children: list["Node"] = field(default_factory=list)


class Tree:
    def __init__(self, value):
        self.root = Node(value)
        self.leaves = {self.root}

    def add_child(self, value, parent: Node):
        child = Node(value, [parent])
        parent.children.append(child)
        self.leaves.add(child)

    def prune(self, node: Node):
        # Remove all unique children
        for child in node.children:
            if child.parents == [node]:
                self.prune(child)

        # Remove all unique parents
        for parent in node.parents:
            if parent.children == [node]:
                self.prune(parent)

        # remove self
        del node
