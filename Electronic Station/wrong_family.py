#!/usr/bin/env checkio --domain=py run wrong-family

# Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of it.
# 
# Michael should figure this out. He's spent almost a month parsing the family archives. He has all father-son connections of his entire family collected in one place.
# 
# With all that data Michael can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let's see.
# 
# You have a list of family ties between father and son. Each element on this list has two elements. The first is the father's name, the second is the son's name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.
# 
# Input:list of lists. Each element has two strings. The list has at least one element
# 
# Output:bool. Is the family tree correct.
# 
# 
# 
# 
# Precondition:1<= len(tree)<100
# 
# 
# END_DESC
import numpy as np
from itertools import combinations

def is_family(tree):
    # return all([is_son(candid, tree) for candid in tree])
    arTree = np.array(tree)
    print(arTree)
    everyone = arTree.flatten()
    parents = arTree[:, 0]
    children = arTree[:, 1]

    if len(everyone) == 2: return True
    if any([elem[0] == elem[1] for elem in tree]): return False

    if any([countif(elem[1], children) > 1 for elem in tree]): return False
    if all([countif(elem[1], everyone) > 1 for elem in tree]): return False
    if any([countif(elem[0], everyone) == 1 and countif(elem[1], everyone) == 1 for elem in tree]): return False
    if any([set(x) == set(y) for (x, y) in combinations(tree, 2)]): return False

    return True

def countif(target, ls):
  return sum(map(lambda x: x == target, ls))


# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.children = []
  
#   def add_Node(self, value):
#     self.children.append(Node(value))

#   def insert(self, value):
#     if self == None: self = Node(value)
#     while True:
#       if len(self.children) > 0:
#         self.children.append(self.insert(value))
#         break
#       else:
#         self.children.append(Node(value))
#         break
#     # insert(node, value)
#     # node.add_Node(Node(value))
#     for i in range(len(self.children)): print(str(i) + " " + self.children[i].data)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")