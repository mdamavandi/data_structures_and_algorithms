

class ChainingHashTable:
    """
    hash table data structure using chaining
    """
    def __init__(self, initial_capacity=10):
        """
        constructor with optional initial capacity parameter
        assigns all buckets with an empty list
        :param initial_capacity:
        """
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, item):
        """
        inserts a new item into the hash table
        :param item: an object
        :return: None
        """
        # get the bucket list where this item will go
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item at the end of the bucket list
        bucket_list.append(item)

    def search(self, key):
        """
        searches for an item with matching key in the hash table
        returns the item if found, or None if not found
        :param key: an object
        :return: the key (if found), else None
        """
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key wasn't found
            return None

    def remove(self, key):
        """
        removes an item with matching key from the has table
        :param key: item to be removed
        :return: None
        """
        # get the bucket list this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        if key in bucket_list:
            bucket_list.remove(key)

if __name__ == '__main__':
    # Main program to create a couple of HashTable objects, showing how
    # the 'capacity' constructor argument works.
    ht1 = ChainingHashTable()
    print('ht1:', ht1.table)

    ht1.insert(10)
    ht1.insert('car')
    ht1.insert(5.2)
    ht1.remove(5.2)

    print('ht1:', ht1.table)

    ht2 = ChainingHashTable(5)
    print('ht2:', ht2.table)

    ht2.insert(10)
    ht2.insert('car')
    ht2.insert(5.2)

    print('ht2:', ht2.table)