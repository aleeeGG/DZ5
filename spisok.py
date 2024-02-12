class LinkedList:

    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None
    
    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item

    def reverse(self): #Функция разворота списка
        pred = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = pred
            pred = current
            current = next
        self.head = pred

    def RemuveFirst(self):   #Удаление превого элемента списка
        self.head = self.head.next

    def RemuveLast(self):     # Удаление последнего элемента с развотом
        my_list.reverse()
        self.head = self.head.next
        my_list.reverse()

    def RemuveLast2(self):    # Второй способ удаления последнего элемента, если первый не понравится
                current = self.head
                while current.next.next is not None:
                    current = current.next

                current.next = None


    def RemuveIndex(self, index):   # удаление по индексу
        if index < 0:
            print("index не может быть меньше 0")
            return
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        pred = None
        ind = 0

        while ind < index and current is not None:
            pred = current
            current = current.next
            ind +=1

        if current is None:
                return
        pred.next = current.next
        current.next = None




    def RemoveFirstValue(self,rm):            #удаление по значению превого элемента
        current = self.head

        if current is not None:
            if current.value==rm:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.value==rm:
                break
            last = current
            current = current.next
        if current == None:
            return
        last.next = current.next
        current = None


    def RemoveLastValue(self,rm):
        my_list.reverse() #Разворачиваем список
        current = self.head  

        if current is not None:
            if current.value==rm:
                self.head = current.next
                current = None
                return
        while current is not None:    #Удаляем первый найденый элемент 
            if current.value==rm:
                break
            last = current
            current = current.next
        if current == None:
            return
        last.next = current.next
        current = None
        my_list.reverse() #Разворачиваем список обратно

    def get_item(self):
        current = self.head
        while current != None:
            yield current.value
            current = current.next

my_list = LinkedList()
my_list.append_end(1)
# my_list.append_end(0)
my_list.append_end(2)
# my_list.append_end(0)
my_list.append_end(3)
# my_list.append_end(0)
my_list.append_end(4)

# my_list.RemuveFirst()
# my_list.RemuveLast()
# my_list.RemuveLast2()
# my_list.RemoveFirstValue(0)
# my_list.RemoveLastValue(0)
my_list.RemuveIndex(1)

for value in my_list.get_item():
    print(value)