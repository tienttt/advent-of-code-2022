class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

class DirNode(TreeNode):
    pass

class FileNode(TreeNode):


def is_dir_exist(TreeNode, DirNode):

def build_tree(filepath):
    root = TreeNode("")
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if(line.startswith('$')): #command
                command = line.split(' ')
                if(command[1] == "cd"):
                    node = DirNode(command[2]) 
                    if (command[2] == '/' and not is_dir_exist(root,node)):
                        root = node
                    if(not is_dir_exist(root, node)):
                        #current_dir = 
                elif (command[1] == "ls"):

            elif (line.startswith('dir')):#folder

            else: #file

build_tree("input.txt")
