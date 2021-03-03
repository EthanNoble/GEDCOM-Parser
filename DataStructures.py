from Containers import Individual
import GEDCOM
class Node:
    _parent = None
    _left = None
    _right = None
    _data = None
    _read = False

    def __init__(self, data, parent = None, left = None, right = None):
        self._parent = parent
        self._left = left
        self._right = right
        self._data = data

class Tree:
    _startNode = None
    _treeList = []
    _families = None

    def __init__(self, startNode, families, generations):
        self._startNode = startNode
        self._families = families
        self._generateTree(startNode)
        self._traverseTree([startNode], generations)
    
    def _traverseTree(self, nodes, depth = 5, currentGeneration = 0):
        #Level by level traversal
        if (depth == 0):
            return
        if (len(nodes) == 0):
            return

        if (len(nodes) == 1 and nodes[0] != None):
            self._treeList.append([])
            self._treeList[currentGeneration].append(nodes[0]._data)
            currentGeneration += 1

        self._treeList.append([])
        nextNodeLevel = []
        for i in range(0, len(nodes)):
            if (nodes[i] != None):
                nextNodeLevel.append(nodes[i]._left)
                nextNodeLevel.append(nodes[i]._right)
                if (nodes[i]._left != None):
                    if (nodes[i]._left._data != None):
                        self._treeList[currentGeneration].append(nodes[i]._left._data)
                else:
                    self._treeList[currentGeneration].append(Individual(None, None, None, "Unknown", None, None, None))
                if (nodes[i]._right != None):
                    if (nodes[i]._right._data != None):
                        self._treeList[currentGeneration].append(nodes[i]._right._data)
                else:
                    self._treeList[currentGeneration].append(Individual(None, None, None, "Unknown", None, None, None))

        self._traverseTree(nextNodeLevel, depth - 1, currentGeneration + 1)

        #Root, left, right traversal
        # if (currentNode._left != None):
        #     if (currentNode._left._data != None):
        #         if (not currentNode._left._read):
        #             print(currentNode._left._data._name)
        #         currentNode._left._read = True
        # else:
        #     return
        
        # if (currentNode._right != None):
        #     if (currentNode._right._data != None):
        #         if (not currentNode._right._read):
        #             print(currentNode._right._data._name)
        #         currentNode._right._read = True
        # else:
        #     return

        # self._traverseTree(families, currentNode._left)
        # self._traverseTree(families, currentNode._right)

    def _generateTree(self, startNode):
        if (startNode._left != None):
            startNode._left._parent = startNode
            if (startNode._left._data == None):
                return
            family = GEDCOM.searchFamilyByIdStatic(startNode._left._data._famcID, self._families)
            if (family != None):
                startNode._left._left = Node(family._husband)
                startNode._left._left._data = family._husband

                startNode._left._right = Node(family._wife)
                startNode._left._right._data = family._wife
                self._generateTree(startNode._left)

        if (startNode._right != None):
            startNode._right._parent = startNode
            if (startNode._right._data == None):
                return
            family = GEDCOM.searchFamilyByIdStatic(startNode._right._data._famcID, self._families)
            if (family != None):
                startNode._right._left = Node(family._husband)
                startNode._right._left._data = family._husband
                
                startNode._right._right = Node(family._wife)
                startNode._right._right._data = family._wife
                self._generateTree(startNode._right)