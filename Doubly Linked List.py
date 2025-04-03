class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev 
        self.next = next

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_the_begining(self, data):
        node = Node(data, prev=None, next=self.head)
        if self.head is not None: #Important condition when the list is empty
            self.head.prev = node
        self.head = node

    def print_forward(self):
        # This method prints list in forward direction
        if self.head is None:
            print('Linked List is empty')
            return
    
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def print_backward(self):
        # This method print linked list in reverse direction
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        rev_llstr = ''
        while itr:
            rev_llstr += str(itr.data) + '-->'
            itr = itr.prev
        
        print(rev_llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, prev=None, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, prev=itr,next=None)
        itr.next = node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
            
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_the_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, prev=itr, next=itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        #Search for first occurance of data_after value in linked list
        #Now insert data_to_insert after data_after node
        if self.head is None:
            return
        
        inserted = False
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, prev=itr, next=itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                inserted = True
                break                
            itr = itr.next
        
        #If the loop is over and the target data was not found
        if not inserted:
            print (f"Insertion failed: Target data \"{data_after}\" not found")


    def remove_by_value(self, data):
        #Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                return
            itr = itr.next
        
        print (f"Removal failed: Target data \"{data}\" not found")

if __name__ == '__main__':
    ll = Doubly_Linked_List()
    ll.insert_values(['banana','mango','grapes','orange'])
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value('mango','apple') 
    ll.print_forward() 
    ll.remove_by_value("figs")
    ll.print_forward() 
    ll.remove_by_value('banana') 
    ll.remove_by_value('mango') 
    ll.remove_by_value('apple') 
    ll.remove_by_value('grapes') 
    ll.print_forward()
    ll.remove_by_value('orange')
    ll.print_forward()
    ll.remove_by_value('watermelon')
    ll.print_forward()

# Expected output:

# banana-->mango-->grapes-->orange-->
# orange-->grapes-->mango-->banana-->
# banana-->mango-->apple-->grapes-->orange-->
# Remotion failed: Target data "figs" not found
# banana-->mango-->apple-->grapes-->orange-->
# orange-->
# Linked List is empty
# Linked List is empty