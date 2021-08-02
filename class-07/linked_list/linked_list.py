class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        """ String representation of the """
        current = self.head
        string = ""
        while current:
            string += str(current) + " -> "
            current = current.next
        string += "None"
        return string

    def append(self, value):
        """ Add a value to the end of the list """
        node = Node(value)

        current = self.head
        if current:
            while current.next:   
                current = current.next
            current.next = node
        else:
            self.head = node

    def insertAfter(self, value, key):
        """ Add a value to the list after a specified value """
        found = False

        node = Node(value)

        current = self.head
        
        while current:
            if current.data == key:
                # insert after procedure
                node.next = current.next
                current.next = node
                found = True
                break
            current = current.next
        if not found:
            raise Exception("Key not found")
    
    def insertBefore(self, value, key):
        """ Add a value to the list after a specified value """
        found = False

        node = Node(value)
        prev = self.head
        current = self.head
        
        while current:
            if current.data == key:
                # insert before procedure
                prev.next = node
                node.next = current
                found = True
                break
            prev = current
            current = current.next
        if not found:
            raise Exception("Key not found")
    

if __name__ == "__main__":
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    # Create linked list
    linked_list = LinkedList()
    linked_list.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    
    linked_list.append(11)
    ll =  LinkedList()
    ll.append("A")
    ll.append("B")
    assert ll.head.data == "A"
    assert ll.head.next.data == "B"
    assert ll.head.next.next == None
    print(ll)
    print(linked_list)

    ll2 = LinkedList()
    try:
        ll2.insertAfter(2,1)
    except Exception as e:
        print(e)
        assert str(e) == "Key not found"
        print("Test Passed")
    
    ll2.append(1)
    ll2.append(3)
    ll2.insertAfter(2,1)

    print(ll2)
    assert ll2.head.next.data == 2
    print("Inserted 2 after 1")

    try:
        ll2.insertAfter(2,8)
    except Exception as e:
        print(e)
        assert str(e) == "Key not found"
        print("Test Passed")


    ll3 = LinkedList()
    try:
        ll3.insertBefore(2,1)
    except Exception as e:
        print(e)
        assert str(e) == "Key not found"
        print("Test Passed")
    
    ll3.append(1)
    ll3.append(3)
    ll3.insertBefore(2,3)

    print(ll3)
    assert ll3.head.next.data == 2
    print("Inserted 2 Before 3")

    try:
        ll3.insertBefore(2,8)
    except Exception as e:
        print(e)
        assert str(e) == "Key not found"
        print("Test Passed")

