from dataclasses import dataclass

@dataclass
class Node:
  value:object
  parent:'Node'=None
  children:list['Node'] =[]

class Tree:
  def __init__(self, root:object, value):
    self.root = Node(value)
    self.leaves = {self.root}


  def add_child(self, value, parent:Node):
    child = Node(value, parent)
    parent.children.append(child)
    self.leaves.add(child)

  def list_nodes_to_root(self, leaf:Node):
    values=[leaf.value]
    while leaf.parent:
      leaf = leaf.parent
      values.append(leaf.value)
    return values

    