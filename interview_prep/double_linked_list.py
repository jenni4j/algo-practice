from typing import List
import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#
#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

# A -> B -> C -> D
# D -> C -> B -> A -> None
def reverse(llist):
    
    if llist is None or llist.next is None:
        return llist
    
    next_node = llist.next
    llist.next = None
    llist.prev = next_node

    while next_node is not None:
        curr_node = next_node
        next_node = curr_node.next
        curr_node.next = curr_node.prev
        curr_node.prev = next_node
    

    return curr_node        

    

"""in main

#llist = DoublyLinkedList()

#        for _ in range(llist_count):
#            llist_item = int(input())
#            llist.insert_node(llist_item)

 #       llist1 = reverse(llist.head)

 """