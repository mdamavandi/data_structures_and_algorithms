

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

class EmptyBucket:
    """
    class to represent empty bucket
    """
    pass

class LinearProbingHashTable:
    """
    HashTable class definition using linear probing
    """
    def __init__(self, initial_capacity=10):
        """
        constructor with optional initial capacity
        all buckets are assigned with an EmptyBucket() instance called self.EMPTY_SINCE_START
        :param initial_capacity: size of hash table
        """

        # special constants to be used as the two types of empty buckets
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # initialize all the table buckets to be EMPTY_SINCE_START
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

    def insert(self, item):
        """
        inserts a new item into the hash table
        :param item: item to be inserted
        :return: boolean
        """

        # find initial bucket we would like to insert the item into
        bucket = hash(item) % len(self.table)
        buckets_probed = 0

        # start linearly probing the buckets
        while buckets_probed < len(self.table):
            # if the bucket is empty, the item can be inserted at that index
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                return True

            # the bucket was occupied, continue probing to next index in the table
            bucket = (bucket + 1) % len(self.table)
            buckets_probed += 1

        # the entire table was full and the key could not be inserted
        return False

    def remove(self, key):
        """
        removes an item with a matching key from the hash table
        :param key: item to be removed
        :return: None
        """

        # find initial bucket to be looked in
        bucket = hash(key) % len(self.table)
        buckets_probed = 0

        # start linearly probing the buckets
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            # if we find the item, set that bucket to EMPTY_AFTER_REMOVAL
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL

            # the bucket was occupied (now or previously), so continue probing
            bucket = (bucket + 1) % len(self.table)
            buckets_probed += 1

    def search(self, key):
        """
        searches for an item with a matching key in the hash table
        returns the item if found or None if not found
        :param key: item to be searched for
        :return: the found item or None if not found
        """

        # find initial bucket to be looked in
        bucket = hash(key) % len(self.table)
        buckets_probed = 0

        # start linearly probing the buckets
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            # if we find the item, return it
            if self.table[bucket] == key:
                return self.table[bucket]

            # the bucket was occupied (now or previously), so continue probing
            bucket = (bucket + 1) % len(self.table)
            buckets_probed += 1

        # the entire table was probed or an EMPTY_SINCE_START bucket was found
        return None

if __name__ == '__main__':
    # Main program to create a couple of HashTable objects
    ht1 = ChainingHashTable()
    print(f'ht1: {ht1.table}')

    ht1.insert(10)
    ht1.insert('car')
    ht1.insert(5.2)
    ht1.remove(5.2)

    print(f'ht1: {ht1.table}')

    ht2 = ChainingHashTable(5)
    print(f'ht2: {ht2.table}')

    ht2.insert(10)
    ht2.insert('car')
    ht2.insert(5.2)

    print(f'ht2: {ht2.table}')

    ht3 = LinearProbingHashTable()
    ht3.insert('foo')
    ht3.insert('bar')
    print(ht3.search('bar'))
    ht3.remove('bar')

    print(f'ht3: {ht3.table}')