
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(12)
    node4 = Node(20)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    headNode = node1
    while headNode:
        print(headNode.data, end="->")
        headNode = headNode.next
        
    print("null")

