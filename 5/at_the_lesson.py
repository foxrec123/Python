class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        print('Bin has been created!')

    def put_item(self, item):
        if self.capacity >= item.volume:
            self.capacity = self.capacity - item.volume
            print("The item has put into this object! " + str(self.capacity) + ' places left.')
        else:
            print('There is impossible to put the item into this object!')
            print(str(self.capacity) + ' places left')
            print('Required volume is ' + str(item.volume))

class Package(Bin):
    def __init__(self, capacity):
        self.capacity = capacity
        print('Package has been created!')

class Item:
    def __init__(self, volume):
        self.volume = volume

bin_1 = Bin(3)
bin_2 = Bin(5)
package1 = Package(1)

item_1 = Item(1)
item_2 = Item(2)



bin_2.put_item(item_2)
bin_2.put_item(item_1)
bin_2.put_item(item_1)
bin_2.put_item(item_2)


