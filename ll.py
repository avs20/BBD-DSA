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

==============================
JAVA
==============================
class Node {
    int val;
    Node next;

    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    public LinkedList() {
        this.head = null;
    }

    public void add(Node node) {
        if (this.head == null) {
            this.head = node;
            return;
        }

        Node cur = this.head;
        while (cur.next != null) {
            cur = cur.next;
        }

        cur.next = node;
    }

    public boolean search(int x) {
        Node cur = this.head;
        while (cur != null) {
            if (cur.val == x) {
                return true;
            }
            cur = cur.next;
        }

        return false;
    }

    public void printList() {
        Node cur = this.head;
        while (cur != null) {
            System.out.println(cur.val);
            cur = cur.next;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.add(new Node(1));
        ll.add(new Node(2));
        System.out.println(ll.search(1));
        System.out.println(ll.search(5));
        ll.add(new Node(3));
        ll.printList();
    }
}

==============================
C++ 

#include <iostream>

class Node {
public:
    int val;
    Node* next;

    Node(int val) : val(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;

    LinkedList() : head(nullptr) {}

    void add(Node* node) {
        if (head == nullptr) {
            head = node;
            return;
        }

        Node* cur = head;
        while (cur->next != nullptr) {
            cur = cur->next;
        }

        cur->next = node;
    }

    bool search(int x) {
        Node* cur = head;
        while (cur != nullptr) {
            if (cur->val == x) {
                return true;
            }
            cur = cur->next;
        }

        return false;
    }

    void print() {
        Node* cur = head;
        while (cur != nullptr) {
            std::cout << cur->val << std::endl;
            cur = cur->next;
        }
    }
};

int main() {
    LinkedList ll;
    ll.add(new Node(1));
    ll.add(new Node(2));
    std::cout << std::boolalpha << ll.search(1) << std::endl;
    std::cout << ll.search(5) << std::endl;
    ll.add(new Node(3));
    ll.print();

    return 0;
}

==================================
// C
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int val;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
} LinkedList;

Node* createNode(int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

void initLinkedList(LinkedList* list) {
    list->head = NULL;
}

void add(LinkedList* list, Node* node) {
    if (list->head == NULL) {
        list->head = node;
        return;
    }

    Node* cur = list->head;
    while (cur->next != NULL) {
        cur = cur->next;
    }

    cur->next = node;
}

bool search(LinkedList* list, int x) {
    Node* cur = list->head;
    while (cur != NULL) {
        if (cur->val == x) {
            return true;
        }
        cur = cur->next;
    }
    return false;
}

void printList(LinkedList* list) {
    Node* cur = list->head;
    while (cur != NULL) {
        printf("%d\n", cur->val);
        cur = cur->next;
    }
}

int main() {
    LinkedList ll;
    initLinkedList(&ll);

    add(&ll, createNode(1));
    add(&ll, createNode(2));
    printf("%d\n", search(&ll, 1));
    printf("%d\n", search(&ll, 5));
    add(&ll, createNode(3));
    printList(&ll);

    return 0;
}