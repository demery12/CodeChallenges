class Node:
  def __init__(self,value):
    self.value=value
    self.left = None
    self.right = None
    self.parent = None
  def __repr__(self):
    return str(self.value)
class BSTRangeIndex(object):
  def __init__(self):
    """Start an empty tree"""
    self.root=Node(None)
  def add(self,key):
    if key is None:
        raise ValueError('Cannot insert nil in the index')
    if self.root.value==None:
      self.root=Node(key)
    else:
      self._add(key,self.root)
  def _add(self,key,node):
    if key<node.value:
      #go left
      if node.left==None:
        node.left=Node(key)
        node.left.parent=node
      else:
        self._add(key,node.left)
    else:
      #go right
      if node.right==None:
        node.right=Node(key)
        node.right.parent=node
      else:
        self._add(key,node.right)
  def remove(self,key):
    if self.root.value==None:
      raise KeyError('RangeIndex is empty, cannot remove: '+ str(key))
    if self.root.value == key and 1==5:
      print self,key
      if self.root.right.value == None and self.root.left.value == None:
        #Nice, this is the easy case
        self.root.value=None
      if self.root.right.value != None:
        successor = self._successor(self.root)
        print "I am not just going to stand here and pretend this works"
        print cat

    else:
      self._remove(key,self.root)
  def _remove(self,key,node):
    print "tryint to remove",key
    if key == node.value:
      successor = self._successor(node)
      if successor != None:
        node.value=successor.value
        if successor.value==node.right.value:
          node.right=successor.right
        else:
          successor.parent.left = successor.right
      else:
        if node.right==None and node.left==None:
          if node.parent == None:
            self.root=Node(None)
          elif node.parent.left!= None and node.parent.left.value==node.value:
            node.parent.left=None
          else:
            node.parent.right=None
          node=None
        else:
          node.value=node.left.value
          node.left=node.left.left
          if node.right != None:
            node.right=node.right.right

    elif key<node.value:
      #go left
      self._remove(key,node.left)
    else:
      #go right
      self._remove(key,node.right)
  def _successor(self,node):
    if node.right == None:
      return None
    else:
      node = node.right
      while node.left != None:
        node = node.left
      return node 
  def __repr__(self):
    return str(self.root)+str(self.root.left)+str(self.root.right)
  def _print_tree(self,node,depth):
    if node.right != None:
      self._print_tree(node.right,depth+1)
    print (2*depth)*" "+str(node.value)
    if node.left != None:
      self._print_tree(node.left,depth+1)
  def list(self, first_key, last_key):
    """List of values for the keys that fall within [first_key, last_key]."""
    return self._list(first_key,last_key,self.root,[])
  def _list(self,first_key,last_key,node,the_list):
    #in order traversal
    if node.left != None and node.value>=first_key:
      self._list(first_key,last_key,node.left,the_list)
    if node.value>=first_key and node.value<=last_key:
      the_list.append(node.value)
    if node.right != None and node.value<=last_key:
      self._list(first_key,last_key,node.right,the_list)
    return the_list
  def count(self,first_key,last_key):
    return self._count(first_key,last_key,self.root,0)
  def _count(self,first_key,last_key,node,count):
    if node.left != None and node.value>=first_key:
      count = self._count(first_key,last_key,node.left,count)
    if node.value>=first_key and node.value<=last_key:
      count += 1
    if node.right != None and node.value<=last_key:
      count = self._count(first_key,last_key,node.right,count)
    return count

mytree = BSTRangeIndex()
mytree.add(44)
mytree.add(17)
mytree.add(32)
mytree.add(78)
mytree.add(88)
mytree.add(50)
mytree.add(48)
mytree.add(62)
mytree.add(84)
mytree.add(80)
mytree.add(82)
mytree.add(92)
mytree.add(81)
mytree.add(83)
print "whole tree"
mytree._print_tree(mytree.root,0)
mytree.remove(78)
print "remove 78"
mytree._print_tree(mytree.root,0)
mytree.remove(32)
print "remove 32"
mytree._print_tree(mytree.root,0)
mytree.remove(83)
print "remove 83"
mytree._print_tree(mytree.root,0)
mytree.remove(81)
print "remove 81"
mytree._print_tree(mytree.root,0)
mytree.remove(17)
print "remove 17"
mytree._print_tree(mytree.root,0)
mytree.remove(44)
print "remove 44"

mytree._print_tree(mytree.root,0)
print mytree.list(0,100)
print mytree.count(45,85)
mytree._print_tree(mytree.root,0)
print "New Adventure"
newtree= BSTRangeIndex()
newtree.add(-100)
newtree.add(-50)
newtree.add(0)
newtree._print_tree(newtree.root,0)
newtree.remove(-100)
newtree._print_tree(newtree.root,0)
newtree.remove(-50)
newtree._print_tree(newtree.root,0)
newtree.remove(0)
newtree._print_tree(newtree.root,0)
newtree.add(50)
newtree.add(25)
newtree.remove(50)
newtree._print_tree(newtree.root,0)

