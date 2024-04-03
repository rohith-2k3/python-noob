# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# class LinkedList:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1

#     def print_list(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.value)
#             temp=temp.next

#     def append(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length +=1

#     def pop(self):
#         if self.length==0:
#             return None
#         position=self.head
#         temp=self.head
#         while(temp.next):
#             position=temp
#             temp=temp.next
#         self.tail=position
#         self.tail.next=None
#         self.length-=1
#         if self.length==0:
#             self.head=None
#             self.tail=None
#         return temp.value
    
#     def prepend(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             temp=self.head
#             self.head=new_node
#             self.head.next=temp
#             #new_node.next=self.head
#             #self.head=new_node
#         self.length+=1
#         return True
    
#     def pop_first(self):
#         if self.head is None:
#             return None
#         temp=self.head
#         self.head=temp.next
#         temp.next=None
#         self.length-=1
#         if self.length==0:
#             self.tail=None
#         return temp
#     def get_index(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp=self.head
#         for _ in range(index):
#             temp=temp.next
#         return temp
#     def set_value(self,index,value):
#         # if self.length==0:
#         #     return None
#         # new_value=value
#         # temp=self.head
#         # for _ in range(index):
#         #     temp=temp.next
#         # temp.value=new_value
#         temp=self.get_index(index)
#         if temp:
#             temp.value=value
#             return True
#         return False
    
#     def insert_value(self,index,value):
#         if index<0 or index>self.length:
#             return False
#         if index==self.length:
#             return self.append(value)
#         if index==0:
#             return self.prepend(value)
#         new_node=Node(value)
#         temp=self.get_index(index-1)
#         new_node.next=temp.next
#         temp.next=new_node
#         self.length+=1
#         return True
    
#     def remove_value(self,index):
#         if index<0 or index>self.length:
#             return None
#         if index==0:
#             return self.pop_first()
#         if index==self.length:
#             return self.pop()
#         prev=self.get_index(index-1)
#         temp=prev.next
#         prev.next=temp.next
#         temp.next=None
#         self.length-=1
#         return temp
    
#     def reverse(self):
#         temp=self.head
#         self.head=self.tail
#         self.tail=temp
#         before=None
#         for _ in range(self.length):
#             after=temp.next
#             temp.next=before
#             before=temp
#             temp=after
# ll=LinkedList(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.pop()
# ll.print_list()

"""
Lets goona start with Trees ,Stacks and queues are similar to LLs
"""
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        temp=self.root
        while (True):
            if temp.value==new_node.value:
                return False
            if temp.value > new_node.value:
                if temp.left is None:
                    temp.left =new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contains(self,value):
        temp=self.root
        while temp:
            if temp.value>value:
                temp=temp.left
            elif temp.value<value:
                temp=temp.right
            else:
                return True
        return False


tree_1=BST()
tree_1.insert(4)
tree_1.insert(5)
tree_1.insert(3)
tree_1.insert(6)
tree_1.insert(8)
tree_1.insert(1)
tree_1.insert(2)


# print(tree_1.root.value)
# print(tree_1.root.left.left.right.value)
# print(tree_1.root.right.value)
# print(tree_1.root.right.right.right.value)
print(tree_1.contains(8))
print(tree_1.contains(81))