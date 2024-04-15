class Base:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.length = 0

    def initiateData(self, data_list):
        for data in data_list:
            if self.head is None:
                self.head = self.Node(data)
                self.length += 1
            else:
                self.head.next = self.Node(data)
                self.length += 1

    def getData(self, index):
        if self.length > 0 and self.length > index:
            for _ in range(index):
                head = self.head
                print(head.data, ">>>")
                head = head.next
        if self.length <= index:
            print("Index out of range")

    def getAllData(self):
        for _ in range(self.length):
            head = self.head
            print(head.data, ">>>")
            head = head.next

    def popFirstData(self):
        if self.length > 0:
            head = self.head
            print(head.data)
            self.head = head.next
            self.length -= 1
        else:
            print("List is empty")

    def appendData(self, data):
        if self.length == 0:
            self.head = self.Node(data)
        else:
            for _ in range(self.length):
                head = self.head
                print(head.data)
                head = head.next