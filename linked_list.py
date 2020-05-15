class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Return "None" if position is not in the list."""
        count = 1
        current = self.head
        if current:
            while current.next and count != position:
                current = current.next
                count+=1
            return current
        else:
            return None
    def insert(self, new_element, position):
        """Insert a new node at the given position."""
        current = self.head
        count = 1
        if current:
            prev = None
            while current.next and count != position:
                prev = current
                current = current.next
                count+=1
            if prev:
                prev.next = new_element
                new_element.next = current
                return
            else:
                new_element.next = prev
                return
        else:
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current:
            prev = None
            while current.next:
                if value == current.value:
                    if prev:
                        prev.next = current.next
                        return
                    else:
                        self.head = current.next
                        return 
                prev = current
                current = current.next
        return
                    

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value