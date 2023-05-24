#INSERT INT0 LINKEDLIST:Time Complexity of O(n) because we are inserting at the end of the LL
#PRINT INTO LINKEDLIST: Time Complexity of O(n) because we are traversing through the linkedlist
class Node(): #class node with data and a ref on None value which stands for the address of the next node
  def __init__(self, data):
    self.data = data
    self.ref = None

class LinkedList(): #class linkedlist which as a head node that has been initialized with a none value
  def __init__(self):
    self.head = None

  def insert(self, data): # insert data into the node
    if self.head is None: #if the head node is None then insert a node with data 
      self.head = Node(data)
    else: 
      current_node = self.head #if a node already exists then the current node is the head and we can insert after the head node
      while current_node.ref is not None: #this checks if the current nodes pointer which is ref has a value i.e. if there is another node in the linked list
        current_node = current_node.ref #if the condition is true we set the head/the current node to be the same as the ref/pointer which has the address of the next node. Basically the new node is the next node
      current_node.ref = Node(data) #if the condition is not true, that is if we have only one node in the LL we make the ref point to a new node that is just created with a specific data

  def print_LL(self): #print the linked list
    if self.head is None: #if there is no node in the LL
      print('Linked List is empty')
    else:
      n = self.head #initialise a variable for head / current node
      while n is not None: #if there is a Node
        print(n.data) #print the node data
        n = n.ref #make the new N the same as the pointer to the next node 

LL1 = LinkedList()
LL1.insert('A')
LL1.insert('B')
LL1.insert('C')
LL1.print_LL()