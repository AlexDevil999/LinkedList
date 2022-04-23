from node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert(self,data,pos = "end"):
        
        if pos == "start":
            node = Node(data,self.head)
            self.head = node
        if pos == "end":
            if self.head is None:
                self.head = Node(data,None)
                return
            
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data,None)
            
    def insert_index(self,index,data):
        
        if index < 0 or index > self.count():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert(data,"start")
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count+=1      
        
        
            
    def insert_values(self,datas):
        self.head = None
        
        for data in datas:
            self.insert(data)
            
            
    def count(self):
        count = 0
        itr = self.head
        
        while itr:
            count+=1
            itr = itr.next            
        return count
    
    def remove(self,index):
        if index < 0 or index >= self.count():
            raise Exception("Error")
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
        
    def print(self):
        if self.head == None:
            print("Empty")
        else:
            list_el = list()
            itr = self.head
            while itr:
                list_el.append(itr.data)
                itr = itr.next
            print(list_el)
                