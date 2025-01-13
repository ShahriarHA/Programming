class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def TraverseAndPrint(head):
    headNode = head
    while headNode:
        print(headNode.data,end="->")
        headNode = headNode.next
    print("null")

if __name__ == "__main__":
    _node1 = Node(4)
    _node2 = Node(9)
    _node3 = Node(20)
    _node4 = Node(27)

    _node1.next = _node2
    _node2.next = _node3
    _node3.next = _node4

    TraverseAndPrint(_node1)
     