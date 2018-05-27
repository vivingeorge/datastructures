import random


class Ds:

    def __init__(self):
        self.hash = {}
        self.dict = {}

    def insert(self, value):

        if value not in self.hash:
            n = len(self.dict)
            self.dict[n] = value
            self.hash[value] = n
            print("Inserted")

    def delete(self, value):

        if value in self.hash:
            n = len(self.dict)
            last_value = self.dict[n-1]
            value_position = self.hash[value]
            self.dict[self.hash[value]] = last_value
            del self.dict[n-1]
            del self.hash[value]
            self.hash[last_value] = value_position
            print("Deleted")

    def search(self, value):

        if value in self.hash:
            print(value, " is found at position ", self.hash[value], " at 2nd associative array")
        else:
            print("Not found")

    def getRandom(self):
        n = len(self.dict)
        if n > 0:
            k = random.randint(0, n-1)
            print(self.dict[k])

    def show_all(self):
        print(self.hash)
        print(self.dict)



ds = Ds()
ds.insert("banana")
ds.insert("orange")
ds.insert("mango")
ds.insert("rambuttan")
ds.insert("apple")
ds.show_all()
ds.search("mango")
ds.getRandom()
ds.getRandom()
ds.getRandom()
ds.getRandom()
ds.getRandom()
ds.getRandom()
ds.getRandom()
ds.show_all()
ds.delete("mango")
ds.show_all()
ds.insert("mango")
ds.show_all()
print("==============================")