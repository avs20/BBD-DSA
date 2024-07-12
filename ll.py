class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def add(self, node):
        if self.head is None:
            self.head = node 
            return 
    
        cur = self.head 
        while cur.next is not None:
            cur = cur.next 
        
        cur.next = node 
    
    def search(self, x):
        cur = self.head 
        while cur is not None:
            if cur.val == x:
                return True 
            cur = cur.next
        
        return False 

    def print(self):
        cur = self.head 
        while cur is not None:
            print(cur.val)
            cur = cur.next

def main():
    ll = LinkedList()
    ll.add(Node(1))
    ll.add(Node(2))
    print(ll.search(1))
    print(ll.search(5))
    ll.add(Node(3))
    ll.print()

if __name__ == '__main__':
    main()