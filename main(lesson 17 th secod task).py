# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def prepend(self, data):
#         new_node = Node(data)

#         new_node.next = self.head
#         self.head = new_node

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head

#         while current.next:
#             current = current.next

#         current.next = new_node

#     def delete(self, data):
#         current = self.head

#         if current and current.data == data:
#             self.head = current.next
#             current = None
#             return

#         prev = None

#         while current and current.data != data:
#             prev = current
#             current = current.next

#         if current is None:
#             return

#         prev.next = current.next
#         current = None

#     def print_list(self):

#         current = self.head

#         while current:
#             print(current.data, end=" -> " if current.next else "\n")
#             current = current.next

# # 7 -> 8 -> 6 -> 4

# ll = LinkedList()
# ll.append(8)
# ll.append(6)
# ll.append(4)
# ll.append(10)
# ll.prepend(7)
# ll.prepend(5)

# ll.print_list()

# ll.delete(8)

# ll.print_list()


# # ll.delete(8)














# ლექციაზე დაწერილ LinkedList კლასში დაამატეთ search მეთოდი რომელიც გადაცემული ელემენტის მიხედვით წაშლის ელემენტს.


def search(self, data):
    current = self.head

    # თუ პირველი ელემენტი ემთხვევა
    if current.data == data:
        self.head = current.next
        current = None
        return "ელემენტი აღმოჩნდა ჰედი, და ის წაიშალა"

    prev = None

    # სიაში ძებნა
    while current.data != data:
        prev = current
        current = current.next


    if current is None:
        return "ვერ მოიძებნა"


    prev.next = current.next
    current = None

    return "ელემენტი წაიშალა"
