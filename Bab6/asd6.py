class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtMiddle(self, middle_node, data):
        if middle_node is None:
            return
        new_node = Node(data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return
        while curr_node:
            if curr_node.data == data:
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

    #No 2
    def hitung_nodes(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    #No 3
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

# Dalam implementasi ini, kita menggunakan dua class yaitu Node dan LinkedList. 
# Class Node merepresentasikan setiap node dalam linked list, 
# sedangkan class LinkedList berisi method untuk mengatur dan mengelola linked list secara keseluruhan.

# Method insertAtEnd digunakan untuk menambahkan node baru ke akhir linked list. 
# Jika linked list kosong, maka node baru akan menjadi head. 
# Jika tidak, maka kita akan mencari node terakhir dan menambahkan node baru setelah itu.

# Method insertAtStart digunakan untuk menambahkan node baru di awal linked list. 
# Node baru akan menjadi head dan next dari node baru adalah node yang sebelumnya menjadi head.

# Method insertAtMiddle digunakan untuk menyisipkan node baru dengan nilai data sebelum middle_node. 
# Node baru akan memiliki next yang sama dengan middle_node dan next dari middle_node akan menjadi node baru.

# Method delete digunakan untuk menghapus node pertama dengan nilai data yang ditentukan dari linked list. 
# Jika linked list kosong, maka method tidak akan melakukan apa-apa. Jika node yang akan dihapus adalah head, 
# maka head akan berubah menjadi next dari node yang dihapus. Jika tidak, maka kita akan mencari node 
# dengan nilai data yang diinginkan dan menghapusnya dari linked list.

# Method print_list digunakan untuk mencetak isi linked list dari awal hingga akhir.

# Method hitung_nodes digunakan untuk menghitung jumlah node dalam linked list