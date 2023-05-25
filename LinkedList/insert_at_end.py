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

  def search(self, x): #SEARCH FOR AN ELEMENT X IN THE LINKED LIST AND RETURN THE NODE COUNT OF THE ELEMENT
    n = self.head
    count = 0 #INITIALISE A VARIABLE COUNT
    while n is not None: #WHILE A NODE EXISTS
      count += 1 #count because you are returning the node count
      if n.data == x: #if the node data matches the element we are trying to find
        return count #return the node count
      else: #else
        n = n.ref #move to the next node and continue the iterative process
    
    return -1 #only return -1 if the element was not found

  def insert_begin(self, data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

  def insert_end(self, data): #Time Complexity of O(n)
    if self.head == None: #if LL IS empty, just return a new Node
      self.head = Node(data)
    else:
      n = self.head
      while n is not None: #while a node exists
        if n.ref == None: #and ref is None which is the last node in the LL
          new_node = Node(data) #create a new node
          n.ref = new_node #make the last node ref point to the next node
          break #break from the loop otherwise it will continue adding data into the nodes
        n = n.ref #if the if condition is not met then move to the next node until you find the one with the none value

LL1 = LinkedList()
LL1.insert(10)
LL1.insert(5)
LL1.insert(30)
LL1.insert_begin(23)
LL1.insert_end(75)
LL1.print_LL()
print(' ')
LL1.search(30)
