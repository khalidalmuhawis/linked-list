class Node:
    def __init__(self, year, highlight, next=None):
        self.year = year
        self.highlight = highlight
        self.next = next

    def get_year(self):
        return self.year

    def get_highlight(self):
        return self.highlight

    def get_next(self):
        return self.next

    def set_year(self, year):
        self.year = year

    def set_highlight(self, highlight):
        self.highlight = highlight

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self, year, highlight):
        self.head = Node(year, highlight)

    def get_head(self):
        return self.head

    def insert_start(self, year, highlight):
        new_node = Node(year, highlight)
        new_node.set_next(self.head)
        self.head = new_node

    def get_data(self):
        current_node = self.get_head()
        while current_node:
            if current_node.get_year() != None:
                print(f"{current_node.get_year()} - {current_node.get_highlight()}")
            current_node = current_node.get_next()



my_life = LinkedList(7, "I think I'm cool")
my_life.insert_start(2, "Walking")
my_life.insert_start(0, "Born")

current_node = my_life.get_head()
age = int(input("What is your age? "))

while current_node.get_year() < age:
    current_age = current_node.get_year() + 1
    if current_node.get_next() != None and current_node.get_next().get_year() == current_age:
        current_node = current_node.get_next()
    else:
        highlight = input("What is highlight: ")
        new_node = Node(current_age, highlight, current_node.get_next())
        current_node.set_next(new_node)
        current_node = new_node


my_life.get_data()
