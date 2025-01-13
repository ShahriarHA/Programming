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

def DeleteNode(head,NodeToBeDel):
    if head == NodeToBeDel:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != NodeToBeDel:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

if __name__ == "__main__":
    _node1 = Node(4)
    _node2 = Node(9)
    _node3 = Node(20)
    _node4 = Node(27)
    _node5 = Node(50)

    _node1.next = _node2
    _node2.next = _node3
    _node3.next = _node4
    _node4.next = _node5

    # before deleting the node
    TraverseAndPrint(_node1)

    # delete 3rd node
    DeleteNode(_node1,_node5)

    # after deletion
    TraverseAndPrint(_node1)






     