#!/usr/bin/env python

import json   # Used when TRACE=jsonp
import os     # Used to get the TRACE environment variable
import re     # Used when TRACE=jsonp
import sys    # Used to smooth over the range / xrange issue.

# Python 3 doesn't have xrange, and range behaves like xrange.
if sys.version_info >= (3,):
    xrange = range

# Circuit verification library.

class Wire(object):
  """A wire in an on-chip circuit.
  
  Wires are immutable, and are either horizontal or vertical.
  """
  
  def __init__(self, name, x1, y1, x2, y2):
    """Creates a wire.
    
    Raises an ValueError if the coordinates don't make up a horizontal wire
    or a vertical wire.
    
    Args:
      name: the wire's user-visible name
      x1: the X coordinate of the wire's first endpoint
      y1: the Y coordinate of the wire's first endpoint
      x2: the X coordinate of the wire's last endpoint
      y2: the Y coordinate of the wire's last endpoint
    """
    # Normalize the coordinates.
    if x1 > x2:
      x1, x2 = x2, x1
    if y1 > y2:
      y1, y2 = y2, y1
    
    self.name = name
    self.x1, self.y1 = x1, y1
    self.x2, self.y2 = x2, y2
    self.object_id = Wire.next_object_id()
    
    if not (self.is_horizontal() or self.is_vertical()):
      raise ValueError(str(self) + ' is neither horizontal nor vertical')
  
  def is_horizontal(self):
    """True if the wire's endpoints have the same Y coordinates."""
    return self.y1 == self.y2
  
  def is_vertical(self):
    """True if the wire's endpoints have the same X coordinates."""
    return self.x1 == self.x2
  
  def intersects(self, other_wire):
    """True if this wire intersects another wire."""
    # NOTE: we assume that wires can only cross, but not overlap.
    if self.is_horizontal() == other_wire.is_horizontal():
      return False 
    
    if self.is_horizontal():
      h = self
      v = other_wire
    else:
      h = other_wire
      v = self
    return v.y1 <= h.y1 and h.y1 <= v.y2 and h.x1 <= v.x1 and v.x1 <= h.x2
  
  def __repr__(self):
    # :nodoc: nicer formatting to help with debugging
    return('<wire ' + self.name + ' (' + str(self.x1) + ',' + str(self.y1) + 
           ')-(' + str(self.x2) + ',' + str(self.y2) + ')>')
  
  def as_json(self):
    """Dict that obeys the JSON format restrictions, representing the wire."""
    return {'id': self.name, 'x': [self.x1, self.x2], 'y': [self.y1, self.y2]}

  # Next number handed out by Wire.next_object_id()
  _next_id = 0
  
  @staticmethod
  def next_object_id():
    """Returns a unique numerical ID to be used as a Wire's object_id."""
    id = Wire._next_id
    Wire._next_id += 1
    return id

class WireLayer(object):
  """The layout of one layer of wires in a chip."""
  
  def __init__(self):
    """Creates a layer layout with no wires."""
    self.wires = {}
  
  def wires(self):
    """The wires in the layout."""
    self.wires.values()
  
  def add_wire(self, name, x1, y1, x2, y2):
    """Adds a wire to a layer layout.
    
    Args:
      name: the wire's unique name
      x1: the X coordinate of the wire's first endpoint
      y1: the Y coordinate of the wire's first endpoint
      x2: the X coordinate of the wire's last endpoint
      y2: the Y coordinate of the wire's last endpoint
    
    Raises an exception if the wire isn't perfectly horizontal (y1 = y2) or
    perfectly vertical (x1 = x2)."""
    if name in self.wires:
        raise ValueError('Wire name ' + name + ' not unique')
    self.wires[name] = Wire(name, x1, y1, x2, y2)
  
  def as_json(self):
    """Dict that obeys the JSON format restrictions, representing the layout."""
    return { 'wires': [wire.as_json() for wire in self.wires.values()] }
  
  @staticmethod
  def from_file(file):
    """Builds a wire layer layout by reading a textual description from a file.
    
    Args:
      file: a File object supplying the input
    
    Returns a new Simulation instance."""

    layer = WireLayer()
    
    while True:
      command = file.readline().split()
      if command[0] == 'wire':
        coordinates = [float(token) for token in command[2:6]]
        layer.add_wire(command[1], *coordinates)
      elif command[0] == 'done':
        break
      
    return layer

class RangeIndexBad(object):
  """Array-based range index implementation."""
  
  def __init__(self):
    """Initially empty range index."""
    self.data = []
  
  def add(self, key):
    """Inserts a key in the range index."""
    if key is None:
        raise ValueError('Cannot insert nil in the index')
    self.data.append(key)
  
  def remove(self, key):
    """Removes a key from the range index."""
    self.data.remove(key)
  
  def list(self, first_key, last_key):
    """List of values for the keys that fall within [first_key, last_key]."""
    return [key for key in self.data if first_key <= key <= last_key]
  
  def count(self, first_key, last_key):
    """Number of keys that fall within [first_key, last_key]."""
    result = 0
    for key in self.data:
      if first_key <= key <= last_key:
        result += 1
    return result




class Node:
  def __init__(self,value):
    self.value=value
    self.left = None
    self.right = None
    self.parent = None
  def __repr__(self):
    return str(self.value)

class RangeIndex(object):
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
    #print "tryint to remove",key
    if node == None:
      return
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


class TracedRangeIndex(RangeIndex):
  """Augments RangeIndex to build a trace for the visualizer."""
  
  def __init__(self, trace):
    """Sets the object receiving tracing info."""
    RangeIndex.__init__(self)
    self.trace = trace
  
  def add(self, key):
    self.trace.append({'type': 'add', 'id': key.wire.name})
    RangeIndex.add(self, key)
  
  def remove(self, key):
    self.trace.append({'type': 'delete', 'id': key.wire.name})
    RangeIndex.remove(self, key)
  
  def list(self, first_key, last_key):
    result = RangeIndex.list(self, first_key, last_key)
    self.trace.append({'type': 'list', 'from': first_key.key,
                       'to': last_key.key,
                       'ids': [key.wire.name for key in result]}) 
    return result
  
  def count(self, first_key, last_key):
    result = RangeIndex.count(self, first_key, last_key)
    self.trace.append({'type': 'list', 'from': first_key.key,
                       'to': last_key.key, 'count': result})
    return result

class ResultSet(object):
  """Records the result of the circuit verifier (pairs of crossing wires)."""
  
  def __init__(self):
    """Creates an empty result set."""
    self.crossings = []
  
  def add_crossing(self, wire1, wire2):
    """Records the fact that two wires are crossing."""
    self.crossings.append(sorted([wire1.name, wire2.name]))
  
  def write_to_file(self, file):
    """Write the result to a file."""
    for crossing in self.crossings:
      file.write(' '.join(crossing))
      file.write('\n')

class TracedResultSet(ResultSet):
  """Augments ResultSet to build a trace for the visualizer."""
  
  def __init__(self, trace):
    """Sets the object receiving tracing info."""
    ResultSet.__init__(self)
    self.trace = trace
    
  def add_crossing(self, wire1, wire2):
    self.trace.append({'type': 'crossing', 'id1': wire1.name,
                       'id2': wire2.name})
    ResultSet.add_crossing(self, wire1, wire2)

class KeyWirePair(object):
  """Wraps a wire and the key representing it in the range index.
  
  Once created, a key-wire pair is immutable."""
  
  def __init__(self, key, wire):
    """Creates a new key for insertion in the range index."""
    self.key = key
    if wire is None:
      raise ValueError('Use KeyWirePairL or KeyWirePairH for queries')
    self.wire = wire
    self.wire_id = wire.object_id

  def __lt__(self, other):
    # :nodoc: Delegate comparison to keys.
    return (self.key < other.key or
            (self.key == other.key and self.wire_id < other.wire_id))
  
  def __le__(self, other):
    # :nodoc: Delegate comparison to keys.
    return (self.key < other.key or
            (self.key == other.key and self.wire_id <= other.wire_id))  

  def __gt__(self, other):
    # :nodoc: Delegate comparison to keys.
    return (self.key > other.key or
            (self.key == other.key and self.wire_id > other.wire_id))
  
  def __ge__(self, other):
    # :nodoc: Delegate comparison to keys.
    return (self.key > other.key or
            (self.key == other.key and self.wire_id >= other.wire_id))

  def __eq__(self, other):
    # :nodoc: Delegate comparison to keys.
    if self.key == None and other== None:
      return True
    elif other == None:
      return False
    return self.key == other.key and self.wire_id == other.wire_id
  
  def __ne__(self, other):
    # :nodoc: Delegate comparison to keys.
    if self.key == None and other== None:
      return False
    elif other == None:
      return True
    return self.key == other.key and self.wire_id == other.wire_id

  def __hash__(self):
    # :nodoc: Delegate comparison to keys.
    return hash([self.key, self.wire_id])

  def __repr__(self):
    # :nodoc: nicer formatting to help with debugging
    return '<key: ' + str(self.key) + ' wire: ' + str(self.wire) + '>'

class KeyWirePairL(KeyWirePair):
  """A KeyWirePair that is used as the low end of a range query.
  
  This KeyWirePair is smaller than all other KeyWirePairs with the same key."""
  def __init__(self, key):
    self.key = key
    self.wire = None
    self.wire_id = -1000000000

class KeyWirePairH(KeyWirePair):
  """A KeyWirePair that is used as the high end of a range query.
  
  This KeyWirePair is larger than all other KeyWirePairs with the same key."""
  def __init__(self, key):
    self.key = key
    self.wire = None
    # HACK(pwnall): assuming 1 billion objects won't fit into RAM.
    self.wire_id = 1000000000

class CrossVerifier(object):
  """Checks whether a wire network has any crossing wires."""
  
  def __init__(self, layer):
    """Verifier for a layer of wires.
    
    Once created, the verifier can list the crossings between wires (the 
    wire_crossings method) or count the crossings (count_crossings)."""

    self.events = []
    self._events_from_layer(layer)
    self.events.sort() #key = lambda x: (x[0], x[3])
    self.index = RangeIndex()
    self.result_set = ResultSet()
    self.performed = False
  
  def count_crossings(self):
    """Returns the number of pairs of wires that cross each other."""
    if self.performed:
      raise 
    self.performed = True
    return self._compute_crossings(True)

  def wire_crossings(self):
    """An array of pairs of wires that cross each other."""
    if self.performed:
      raise 
    self.performed = True
    return self._compute_crossings(False)
  '''
  def _events_from_layer(self, layer):
    """Populates the sweep line events from the wire layer."""
    left_edge = min([wire.x1 for wire in layer.wires.values()])
    print left_edge, "dya left_edge"
    for wire in layer.wires.values():
      if wire.is_horizontal():
        self.events.append([left_edge, 0, wire.object_id, 'add', wire])

      else:
        self.events.append([wire.x1, 1, wire.object_id, 'query', wire])
    print self.events, "dylan"
  '''
  def _events_from_layer(self, layer):
    """Populates the sweep line events from the wire layer."""
    #left_edge = min([wire.x1 for wire in layer.wires.values()])
    for wire in layer.wires.values():
      if wire.is_horizontal():
        self.events.append([wire.x1, 0, wire.object_id, 'add', wire])
        self.events.append([wire.x2, 2, wire.object_id, 'remove', wire])

      else:
        self.events.append([wire.x1, 1, wire.object_id, 'query', wire])

  def _compute_crossings(self, count_only):
    """Implements count_crossings and wire_crossings."""
    if count_only:
      result = 0
    else:
      result = self.result_set
    #print self.events
    for event in self.events:
      #self.index._print_tree(self.index.root,0)
      #print ""
      event_x, event_type, wire = event[0], event[3], event[4]
      self.trace_sweep_line(event_x)
      if event_type == 'add':
        self.index.add(KeyWirePair(wire.y1, wire))
      elif event_type == 'remove':
        #print "called remove"
        self.index.remove(KeyWirePair(wire.y1, wire))
      elif event_type == 'query':
        cross_wires = []
        if count_only:
            #print self.index.count(KeyWirePairL(wire.y1),KeyWirePairH(wire.y2))
            result += self.index.count(KeyWirePairL(wire.y1),
                                       KeyWirePairH(wire.y2))
        else:         
          for kwp in self.index.list(KeyWirePairL(wire.y1),
                                     KeyWirePairH(wire.y2)):
            if wire.intersects(kwp.wire):
              result.add_crossing(wire, kwp.wire)
    return result
  
  def trace_sweep_line(self, x):
    """When tracing is enabled, adds info about where the sweep line is.
    
    Args:
      x: the coordinate of the vertical sweep line
    """
    # NOTE: this is overridden in TracedCrossVerifier
    pass

class TracedCrossVerifier(CrossVerifier):
  """Augments CrossVerifier to build a trace for the visualizer."""
  
  def __init__(self, layer):
    CrossVerifier.__init__(self, layer)
    self.trace = []
    self.index = TracedRangeIndex(self.trace)
    self.result_set = TracedResultSet(self.trace)
    
  def trace_sweep_line(self, x):
    self.trace.append({'type': 'sweep', 'x': x})
    
  def trace_as_json(self):
    """List that obeys the JSON format restrictions with the verifier trace."""
    return self.trace

# Command-line controller.
if __name__ == '__main__':
    import sys
    layer = WireLayer.from_file(sys.stdin)
    verifier = CrossVerifier(layer)
    
    if os.environ.get('TRACE') == 'jsonp':
      verifier = TracedCrossVerifier(layer)
      result = verifier.wire_crossings()
      json_obj = {'layer': layer.as_json(), 'trace': verifier.trace_as_json()}
      sys.stdout.write('onJsonp(')
      json.dump(json_obj, sys.stdout)
      sys.stdout.write(');\n')
    elif os.environ.get('TRACE') == 'list':
      verifier.wire_crossings().write_to_file(sys.stdout)
    else:
      sys.stdout.write(str(verifier.count_crossings()) + "\n")
