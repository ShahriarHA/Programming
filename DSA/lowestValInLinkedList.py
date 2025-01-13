class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def FindLowestVal(head):
    minVal = head.data
    headNode = head
    while headNode:
        if headNode.data < minVal:
            minVal = headNode.data
        headNode = headNode.next
    return minVal

if __name__ == "__main__":
    _node1 = Node(10)
    _node2 = Node(9)
    _node3 = Node(20)
    _node4 = Node(1)
    _node5 = Node(0)

    _node1.next = _node2
    _node2.next = _node3
    _node3.next = _node4
    _node4.next = _node5

    result = FindLowestVal(_node1)
    print(result)
     